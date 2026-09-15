// The lost update, forced. `total++` is three steps -- load, add, store -- and
// nothing stops ten goroutines from all loading the same old total. Each one
// reports its load on a channel and then waits for a second channel to close,
// so every load happens before any store, on every run.
//
// Each Load and each Store is atomic, so `go run -race` has no data race to
// report here. The pair is not atomic.
//
//	go build lost_update_go.go && ./lost_update_go
package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

const handlers = 10

func main() {
	var total atomic.Int64
	loads := make(chan int64)
	allLoaded := make(chan struct{})

	var wg sync.WaitGroup
	for range handlers {
		wg.Go(func() {
			seen := total.Load() // 1. load
			loads <- seen
			<-allLoaded           // every handler has loaded
			total.Store(seen + 1) // 2. add, 3. store
		})
	}

	loaded := make([]int64, 0, handlers)
	for range handlers {
		loaded = append(loaded, <-loads)
	}
	close(allLoaded)
	wg.Wait()

	fmt.Printf("%d handlers each added 1 to a total that started at 0\n", handlers)
	fmt.Println("the totals they loaded:", loaded)
	fmt.Printf("the total is %d, not %d\n", total.Load(), handlers)
}
