// Keeping every update, three ways. Eight handlers each add the numbers 1 to
// 10,000 to one total: under a sync.Mutex, with an atomic add, and by sending
// every number to the one goroutine that owns the total.
//
//	go build every_update_go.go && ./every_update_go
package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

const (
	handlers = 8
	last     = 10_000
)

func withAMutex() int64 {
	var mu sync.Mutex
	var total int64
	var wg sync.WaitGroup
	for range handlers {
		wg.Go(func() {
			for n := int64(1); n <= last; n++ {
				mu.Lock()
				total += n // load, add and store, all while holding the lock
				mu.Unlock()
			}
		})
	}
	wg.Wait()
	return total
}

func withAnAtomicAdd() int64 {
	var total atomic.Int64
	var wg sync.WaitGroup
	for range handlers {
		wg.Go(func() {
			for n := int64(1); n <= last; n++ {
				total.Add(n) // one indivisible operation
			}
		})
	}
	wg.Wait()
	return total.Load()
}

func withOneOwner() int64 {
	numbers := make(chan int64)
	result := make(chan int64)
	go func() {
		var total int64 // no other goroutine can reach this variable
		for n := range numbers {
			total += n
		}
		result <- total
	}()

	var wg sync.WaitGroup
	for range handlers {
		wg.Go(func() {
			for n := int64(1); n <= last; n++ {
				numbers <- n
			}
		})
	}
	wg.Wait()
	close(numbers) // the owner's range loop ends
	return <-result
}

func main() {
	fmt.Printf("%d handlers each add 1 to %d; the total should be %d\n",
		handlers, last, handlers*last*(last+1)/2)
	fmt.Println("with a sync.Mutex:   ", withAMutex())
	fmt.Println("with atomic Add:     ", withAnAtomicAdd())
	fmt.Println("with one owner:      ", withOneOwner())
}
