#!/usr/bin/env bash
# The program a reader writes first: ten scoped threads, each doing `total += 1`
# on one plain integer. rustc refuses to build it. The full diagnostic draws
# arrows at columns that can move between compiler versions, so this script
# keeps the error's first line and rustc's exit status.
set -u

dir=$(mktemp -d)
trap 'rm -rf "$dir"' EXIT

cat >"$dir/plain.rs" <<'RS'
use std::thread;

fn main() {
    let mut total = 0;
    thread::scope(|s| {
        for _ in 0..10 {
            s.spawn(|| total += 1);
        }
    });
    println!("the total is {total}");
}
RS

say() { printf '$ %s\n' "$*"; }

say 'rustc --edition 2024 plain.rs'
(cd "$dir" && rustc --edition 2024 plain.rs 2>diagnostic.txt)
status=$?
grep '^error\[' "$dir/diagnostic.txt"
echo "rustc exit status $status"
if [ -e "$dir/plain" ]; then
    echo "and yet a binary was built"
else
    echo "no binary was built"
fi
