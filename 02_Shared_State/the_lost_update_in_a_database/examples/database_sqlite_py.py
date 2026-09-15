"""The lost update in a database. Two connections, A and B, to one SQLite file,
each adding to the same row: A adds 5 and B adds 10, so the total should end at
15. No threads are needed to lose one of them. The program runs the statements
of the two connections in the interleaving that loses an update -- both read
before either writes -- and prints each statement as it runs it.

`timeout=0` makes a connection that finds the database locked fail at once
instead of waiting, and `autocommit=True` (Python 3.12 and later) means each
statement is its own transaction unless the connection says BEGIN.

    python3 database_sqlite_py.py
"""

import os
import sqlite3
import tempfile

workdir = tempfile.TemporaryDirectory()
path = os.path.join(workdir.name, "counter.db")

setup = sqlite3.connect(path, autocommit=True)
setup.execute(
    "CREATE TABLE counter (id INTEGER PRIMARY KEY, total INTEGER NOT NULL, version INTEGER NOT NULL)"
)
setup.execute("INSERT INTO counter VALUES (1, 0, 0)")
setup.close()

a = sqlite3.connect(path, timeout=0, autocommit=True)
b = sqlite3.connect(path, timeout=0, autocommit=True)
name = {a: "A", b: "B"}


def run(conn: sqlite3.Connection, sql: str, *params: int):
    """Run one statement and print it with its parameters filled in.

    Returns the first row of a query, the number of rows an UPDATE changed, or
    "refused" when SQLite refuses the statement.
    """
    shown = sql
    for p in params:
        shown = shown.replace("?", str(p), 1)
    try:
        cursor = conn.execute(sql, params)
    except sqlite3.OperationalError as e:
        print(f"  {name[conn]}: {shown}  -> refused: {e} ({e.sqlite_errorname})")
        return "refused"
    if sql.startswith("SELECT"):
        row = cursor.fetchone()
        print(f"  {name[conn]}: {shown}  -> {', '.join(map(str, row))}")
        return row if len(row) > 1 else row[0]
    if sql.startswith("UPDATE") and "version" in sql:
        print(f"  {name[conn]}: {shown}  -> {cursor.rowcount} row(s) changed")
        return cursor.rowcount
    print(f"  {name[conn]}: {shown}")
    return None


def reset(title: str) -> None:
    a.execute("UPDATE counter SET total = 0, version = 0 WHERE id = 1")
    print(title)


def total() -> int:
    return a.execute("SELECT total FROM counter WHERE id = 1").fetchone()[0]


reset("1. Read the total, add in Python, write the sum back")
seen_a = run(a, "SELECT total FROM counter WHERE id = 1")
seen_b = run(b, "SELECT total FROM counter WHERE id = 1")
run(a, "UPDATE counter SET total = ? WHERE id = 1", seen_a + 5)
run(b, "UPDATE counter SET total = ? WHERE id = 1", seen_b + 10)
print(f"  the total is {total()}, not 15\n")

reset("2. Let the database do the addition, in one statement")
run(a, "UPDATE counter SET total = total + ? WHERE id = 1", 5)
run(b, "UPDATE counter SET total = total + ? WHERE id = 1", 10)
print(f"  the total is {total()}\n")

reset("3. Read and write inside a transaction")
run(a, "BEGIN")
seen_a = run(a, "SELECT total FROM counter WHERE id = 1")
run(b, "BEGIN")
seen_b = run(b, "SELECT total FROM counter WHERE id = 1")
run(a, "UPDATE counter SET total = ? WHERE id = 1", seen_a + 5)
if run(b, "UPDATE counter SET total = ? WHERE id = 1", seen_b + 10) == "refused":
    run(b, "ROLLBACK")
run(a, "COMMIT")
print("  B starts again, from the beginning:")
run(b, "BEGIN")
seen_b = run(b, "SELECT total FROM counter WHERE id = 1")
run(b, "UPDATE counter SET total = ? WHERE id = 1", seen_b + 10)
run(b, "COMMIT")
print(f"  the total is {total()}\n")

reset("4. Take the write lock before reading: BEGIN IMMEDIATE")
run(a, "BEGIN IMMEDIATE")
seen_a = run(a, "SELECT total FROM counter WHERE id = 1")
run(b, "BEGIN IMMEDIATE")
run(a, "UPDATE counter SET total = ? WHERE id = 1", seen_a + 5)
run(a, "COMMIT")
run(b, "BEGIN IMMEDIATE")
seen_b = run(b, "SELECT total FROM counter WHERE id = 1")
run(b, "UPDATE counter SET total = ? WHERE id = 1", seen_b + 10)
run(b, "COMMIT")
print(f"  the total is {total()}\n")

reset("5. Write only if nobody has written since the read: a version column")
total_a, version_a = run(a, "SELECT total, version FROM counter WHERE id = 1")
total_b, version_b = run(b, "SELECT total, version FROM counter WHERE id = 1")
run(a, "UPDATE counter SET total = ?, version = ? WHERE id = 1 AND version = ?",
    total_a + 5, version_a + 1, version_a)
if run(b, "UPDATE counter SET total = ?, version = ? WHERE id = 1 AND version = ?",
       total_b + 10, version_b + 1, version_b) == 0:
    print("  B changed nothing, so B reads again and retries:")
    total_b, version_b = run(b, "SELECT total, version FROM counter WHERE id = 1")
    run(b, "UPDATE counter SET total = ?, version = ? WHERE id = 1 AND version = ?",
        total_b + 10, version_b + 1, version_b)
print(f"  the total is {total()}")

a.close()
b.close()
workdir.cleanup()
