#!/usr/bin/env bash
# Go's race detector against two versions of the forced lost update: one with a
# plain int64, one with the atomic.Int64 of lost_update_go.go. Both lose nine of
# ten additions. The detector's report names goroutine numbers and addresses
# that vary from run to run, so this script keeps whether a report appeared,
# the program's last line, and the exit status.
set -u

dir=$(mktemp -d)
trap 'rm -rf "$dir"' EXIT

# lost_update_go.go with its atomic.Int64 swapped for a plain int64.
sed -e 's/var total atomic.Int64/var total int64/' \
    -e 's/seen := total.Load()/seen := total/' \
    -e 's/total.Store(seen + 1)/total = seen + 1/' \
    -e 's/total.Load(), handlers/total, handlers/' \
    -e '/"sync\/atomic"/d' \
    lost_update_go.go >"$dir/plain.go"

say() { printf '$ %s\n' "$*"; }

run() {
    name=$1
    say "go build -race -o $name $name.go"
    (cd "$dir" && "${GO:-go}" build -race -o "$name" "$name.go") || exit 1
    say "./$name"
    (cd "$dir" && "./$name" >stdout.txt 2>stderr.txt)
    status=$?
    tail -n 1 "$dir/stdout.txt"
    if grep -q '^WARNING: DATA RACE$' "$dir/stderr.txt"; then
        echo "the race detector printed WARNING: DATA RACE"
    else
        echo "the race detector printed nothing"
    fi
    echo "exit status $status"
}

cp lost_update_go.go "$dir/atomic.go"
run plain
run atomic
