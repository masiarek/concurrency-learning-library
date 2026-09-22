#!/usr/bin/env bash
# The same two-goroutine sum in Go, where a goroutine may outlive the function
# that started it and borrowing a local is allowed anyway. The compiler settles
# it by moving the variable: `go build -gcflags=-m` reports what it decided.
# Its lines are prefixed with file and line numbers, which move whenever the
# program is edited, so this script keeps the decisions and drops the prefixes.
set -u

dir=$(mktemp -d)
trap 'rm -rf "$dir"' EXIT

cat >"$dir/lend.go" <<'GO'
package main

import (
	"fmt"
	"sync"
)

func sumOnTwoGoroutines() int {
	samples := [8]int{3, 1, 4, 1, 5, 9, 2, 6} // a local, as in the other two
	left, right := samples[:4], samples[4:]

	var a, b int
	var wg sync.WaitGroup
	wg.Go(func() {
		for _, n := range left {
			a += n
		}
	})
	wg.Go(func() {
		for _, n := range right {
			b += n
		}
	})
	wg.Wait()

	fmt.Println("left half", a, "+ right half", b)
	return a + b
}

func main() {
	fmt.Println("the total is", sumOnTwoGoroutines())
}
GO

say() { printf '$ %s\n' "$*"; }

say 'go build -gcflags=-m -o lend lend.go'
(cd "$dir" && "${GO:-go}" build -gcflags=-m -o lend lend.go 2>escape.txt) || exit 1
sed -n 's/^.*: \(moved to heap: .*\)$/\1/p' "$dir/escape.txt" | sort

say './lend'
(cd "$dir" && ./lend)
