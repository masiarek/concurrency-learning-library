#!/usr/bin/env bash
# The same program in Go, which builds it. Both goroutines write 1, so the
# answer is 1 on every run and no timing can change it -- and the race detector
# reports a data race all the same, because it checks the accesses and not the
# answer. Its report names goroutine numbers and addresses that vary from run to
# run, so this script keeps whether a report appeared and the exit status.
set -u

dir=$(mktemp -d)
trap 'rm -rf "$dir"' EXIT

cat >"$dir/same_value.go" <<'GO'
package main

import (
	"fmt"
	"sync"
)

func main() {
	var shared int
	var wg sync.WaitGroup
	for range 2 {
		wg.Go(func() { shared = 1 }) // both goroutines write the same 1
	}
	wg.Wait()
	fmt.Println("shared is", shared)
}
GO

say() { printf '$ %s\n' "$*"; }

build_and_run() {
    name=$1
    shift
    say "go build $* -o $name same_value.go" | tr -s ' '
    (cd "$dir" && "${GO:-go}" build "$@" -o "$name" same_value.go) || exit 1
    say "./$name"
    (cd "$dir" && "./$name" >stdout.txt 2>stderr.txt)
    status=$?
    cat "$dir/stdout.txt"
    if grep -q '^WARNING: DATA RACE$' "$dir/stderr.txt"; then
        echo "the race detector printed WARNING: DATA RACE"
    fi
    echo "exit status $status"
}

build_and_run plain
build_and_run detector -race
