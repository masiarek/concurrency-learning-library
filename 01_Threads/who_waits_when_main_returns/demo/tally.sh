#!/usr/bin/env bash
# Build two_workers.rs, run it N times (default 300), and count each distinct
# transcript. Newlines are shown as | so that a transcript fits on one line:
# one that does not end in | was cut off in the middle of a line.
#
#   bash demo/tally.sh          # from the lesson folder
#   bash demo/tally.sh 1000
set -eu
cd "$(dirname "$0")"
runs=${1:-300}
dir=$(mktemp -d)
trap 'rm -rf "$dir"' EXIT
rustc --edition 2024 two_workers.rs -o "$dir/two_workers"
for _ in $(seq "$runs"); do
    "$dir/two_workers" | tr '\n' '|'
    echo
done | sort | uniq -c | sort -rn
