// Getting a result back. In Go, `go f()` is a statement, not an expression:
// there is no handle, and a function's return values are discarded. A result
// comes back as a value sent on a channel -- and so does an error.
//
//	go build result_back_go.go && ./result_back_go
package main

import (
	"errors"
	"fmt"
)

type result struct {
	total int
	err   error
}

func sumTo100() int {
	total := 0
	for i := 1; i <= 100; i++ {
		total += i
	}
	return total
}

func main() {
	totals := make(chan int)
	go func() { totals <- sumTo100() }()
	fmt.Println("received from the channel:", <-totals)

	results := make(chan result)
	go func() { results <- result{err: errors.New("no total today")} }()
	r := <-results
	fmt.Printf("received a result whose err is %q\n", r.err)
}
