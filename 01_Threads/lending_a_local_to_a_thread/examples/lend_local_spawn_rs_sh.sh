#!/usr/bin/env bash
# The same two-thread sum written with thread::spawn instead of thread::scope.
# Nothing else changes, and it does not build: a spawned thread may outlive the
# function that started it, so what it captures must live for 'static, and eight
# numbers on a stack frame do not. The diagnostic draws arrows at columns that
# can move between compiler versions, so this script keeps the error's first
# line, the line that names the bound it could not meet, and rustc's exit
# status. The note pointing into std's own source is left out: it prints the
# source line only where the rust-src component is installed.
set -u

dir=$(mktemp -d)
trap 'rm -rf "$dir"' EXIT

cat >"$dir/spawned.rs" <<'RS'
use std::thread;

fn sum_on_two_threads() -> i64 {
    let samples: [i64; 8] = [3, 1, 4, 1, 5, 9, 2, 6];
    let (left, right) = samples.split_at(4);

    let a = thread::spawn(|| left.iter().sum::<i64>());
    let b = thread::spawn(|| right.iter().sum::<i64>());

    a.join().unwrap() + b.join().unwrap()
}

fn main() {
    println!("the total is {}", sum_on_two_threads());
}
RS

say() { printf '$ %s\n' "$*"; }

say 'rustc --edition 2024 spawned.rs'
(cd "$dir" && rustc --edition 2024 spawned.rs 2>diagnostic.txt)
status=$?
grep '^error\[' "$dir/diagnostic.txt"
sed -n 's/.*argument requires that \(.*\)$/    ...argument requires that \1/p' "$dir/diagnostic.txt"
echo "rustc exit status $status"
if [ -e "$dir/spawned" ]; then
    echo "and yet a binary was built"
else
    echo "no binary was built"
fi
