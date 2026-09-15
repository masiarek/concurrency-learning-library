#!/usr/bin/env bash
# The lesson's scenarios against PostgreSQL, which CI does not run. Two psql
# sessions, A and B, share one row. A starts first and holds its transaction
# open for three seconds; B starts one second later, while A still holds it.
# Each session's transcript is printed after both have finished. A statement
# that had to wait for the other session is followed by how long it waited.
#
#   bash demo/postgres.sh                    # from the lesson folder; needs Docker
#   bash demo/postgres.sh postgres:17
set -eu
image=${1:-postgres:latest}
name=lost-update-demo-$$
dir=$(mktemp -d)

docker run --rm -d --name "$name" --ulimit fsize=104857600 \
    -e POSTGRES_HOST_AUTH_METHOD=trust "$image" >/dev/null
trap 'docker stop "$name" >/dev/null; rm -rf "$dir"' EXIT

# The image's first start runs a temporary server on a Unix socket only, so a
# TCP connection succeeds only once the real server is up.
psql() { docker exec -i "$name" psql -X -q -t -A -U postgres -h 127.0.0.1 "$@"; }
until psql -c 'SELECT 1' >/dev/null 2>&1; do sleep 1; done
psql -c 'CREATE TABLE counter (id int PRIMARY KEY, total int NOT NULL)'
psql -c 'INSERT INTO counter VALUES (1, 0)'
echo "PostgreSQL $(psql -c 'SHOW server_version' | cut -d' ' -f1), in Docker $image"

# Turn one session's statements into a psql script. `hold N` keeps the
# transaction open for N seconds. Every other line is echoed, then run; psql's
# \timing reports how long it took, and awk keeps only waits of half a second
# or more. `\gset` stores a SELECT's column in a psql variable, here :total.
session() {
    {
        echo '\timing on'
        while IFS= read -r stmt; do
            case $stmt in
            'hold '*)
                echo "\\echo '   ... keeps the transaction open for ${stmt#hold } seconds'"
                echo '\timing off'
                echo "SELECT pg_sleep(${stmt#hold }) \\g /dev/null"
                echo '\timing on'
                ;;
            *)
                echo "\\echo '>>> $(printf '%s' "$stmt" | sed 's/\\/\\\\/g')'"
                echo "$stmt"
                echo '\if :ERROR'
                echo "\\echo '   error:' :LAST_ERROR_MESSAGE"
                echo '\endif'
                case $stmt in *'\gset'*) echo "\\echo '   loaded' :total" ;; esac
                ;;
            esac
        done
    } | psql -v ON_ERROR_STOP=0 2>/dev/null | awk '
        /^Time: / { if ($2 >= 500) printf "   waited %.1f s\n", $2 / 1000; next }
        /^>>> /   { print substr($0, 5); next }
        /^   /    { print; next }
                  { print "   returned " $0 }'
}

scenario() {
    title=$1 a=$2 b=$3
    psql -c 'UPDATE counter SET total = 0' >/dev/null
    echo
    echo "$title"
    printf '%s\n' "$a" | session >"$dir/a" &
    sleep 1
    printf '%s\n' "$b" | session >"$dir/b" &
    wait
    sed 's/^/  A: /' "$dir/a"
    sed 's/^/  B: /' "$dir/b"
    echo "  the total is $(psql -c 'SELECT total FROM counter')"
}

scenario "1. Let the database do the addition, in one statement" \
"BEGIN;
UPDATE counter SET total = total + 5 WHERE id = 1;
hold 3
COMMIT;" \
"UPDATE counter SET total = total + 10 WHERE id = 1 RETURNING total;"

scenario "2. Read and write inside a transaction, at the default READ COMMITTED" \
"BEGIN;
SELECT total FROM counter WHERE id = 1 \\gset
UPDATE counter SET total = :total + 5 WHERE id = 1;
hold 3
COMMIT;" \
"BEGIN;
SELECT total FROM counter WHERE id = 1 \\gset
UPDATE counter SET total = :total + 10 WHERE id = 1;
COMMIT;"

scenario "3. The same, at REPEATABLE READ" \
"BEGIN ISOLATION LEVEL REPEATABLE READ;
SELECT total FROM counter WHERE id = 1 \\gset
UPDATE counter SET total = :total + 5 WHERE id = 1;
hold 3
COMMIT;" \
"BEGIN ISOLATION LEVEL REPEATABLE READ;
SELECT total FROM counter WHERE id = 1 \\gset
UPDATE counter SET total = :total + 10 WHERE id = 1;
ROLLBACK;"

scenario "4. Lock the row when reading it: SELECT ... FOR UPDATE" \
"BEGIN;
SELECT total FROM counter WHERE id = 1 FOR UPDATE \\gset
UPDATE counter SET total = :total + 5 WHERE id = 1;
hold 3
COMMIT;" \
"BEGIN;
SELECT total FROM counter WHERE id = 1 FOR UPDATE \\gset
UPDATE counter SET total = :total + 10 WHERE id = 1;
COMMIT;"
