#!/usr/bin/env bash
# Two threads, one variable, and both threads write the same value: the answer
# never varies, so there is no race condition -- and rustc still refuses to
# build it. The full diagnostic draws arrows at columns that can move between
# compiler versions, so this script keeps the error's first line, rustc's exit
# status, and whether a binary appeared.
set -u

dir=$(mktemp -d)
trap 'rm -rf "$dir"' EXIT

cat >"$dir/same_value.rs" <<'RS'
use std::thread;

fn main() {
    let mut shared = 0;
    thread::scope(|s| {
        for _ in 0..2 {
            s.spawn(|| shared = 1); // both threads write the same 1
        }
    });
    println!("shared is {shared}");
}
RS

say() { printf '$ %s\n' "$*"; }

say 'rustc --edition 2024 same_value.rs'
(cd "$dir" && rustc --edition 2024 same_value.rs 2>diagnostic.txt)
status=$?
grep '^error\[' "$dir/diagnostic.txt"
echo "rustc exit status $status"
if [ -e "$dir/same_value" ]; then
    echo "and yet a binary was built"
else
    echo "no binary was built"
fi
