#!/usr/bin/env bash
# The lost update without any barrier: four threads each add 1 to a shared total
# a million times (Python: 200,000 times), with nothing coordinating them. Each
# program is built the way tools/run_examples.py builds an example, run N times
# (default 5), and prints how many additions it lost.
#
#   bash demo/unforced.sh          # from the lesson folder
#   bash demo/unforced.sh 20
set -eu
cd "$(dirname "$0")"
runs=${1:-5}
dir=$(mktemp -d)
trap 'rm -rf "$dir"' EXIT

rustc --edition 2024 count_rs.rs -o "$dir/count_rs"
go build -trimpath -o "$dir/count_go" count_go.go
cc -std=c17 -Wall -Wextra -pedantic -pthread count_c.c -o "$dir/count_c"
c++ -std=c++20 -O2 -Wall -Wextra -Wpedantic -pthread count_cpp.cpp -o "$dir/count_cpp"

tally() {
    label=$1
    shift
    printf '%-44s' "$label"
    for _ in $(seq "$runs"); do
        printf ' %9s' "$("$@")"
    done
    echo
}

echo "additions lost per run, out of 4,000,000 (Python: 800,000)"
tally "Rust    load(), then store(load + 1)" "$dir/count_rs"
tally "Go      total++" "$dir/count_go"
tally "C       total += 1, built without -O" "$dir/count_c"
tally "C++     total += 1, built with -O2" "$dir/count_cpp"
tally "Java    total += 1" java count_java.java
tally "Python  total += 1" python3 -I count_py.py plain
tally "Python  total = total + one()" python3 -I count_py.py call
