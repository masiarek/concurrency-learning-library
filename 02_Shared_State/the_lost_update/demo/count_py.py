"""Four threads, 200,000 additions each, to a module-level int with nothing
guarding it. Prints how many additions were lost.

    python3 count_py.py plain    # total += 1
    python3 count_py.py call     # total = total + one(): a call between the load and the store
"""

import sys
import threading

THREADS = 4
EACH = 200_000

total = 0


def one() -> int:
    return 1


def plain() -> None:
    global total
    for _ in range(EACH):
        total += 1


def call() -> None:
    global total
    for _ in range(EACH):
        total = total + one()


work = {"plain": plain, "call": call}[sys.argv[1]]
threads = [threading.Thread(target=work) for _ in range(THREADS)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(THREADS * EACH - total)
