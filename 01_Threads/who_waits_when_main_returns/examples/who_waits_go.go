// Who waits when main returns? In Go, nothing waits for a goroutine: when main
// returns, the program exits. A sync.WaitGroup is a wait you write yourself.
//
//	go build who_waits_go.go && ./who_waits_go
package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var wg sync.WaitGroup
	wg.Go(func() { // Go 1.25: Add(1), start the goroutine, Done() when it returns
		time.Sleep(1 * time.Second)
		fmt.Println("goroutine in a WaitGroup:  finished")
	})
	wg.Wait()

	go func() {
		time.Sleep(3 * time.Second)
		fmt.Println("plain goroutine:           finished")
	}()

	fmt.Println("main:                      returning")
}
