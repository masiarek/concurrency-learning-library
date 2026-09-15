// Four goroutines, a million additions each, to a plain int64 with nothing
// guarding it. Prints how many additions were lost. This is a data race.
package main

import (
	"fmt"
	"sync"
)

const (
	goroutines = 4
	each       = 1_000_000
)

func main() {
	var total int64
	var wg sync.WaitGroup
	for range goroutines {
		wg.Go(func() {
			for range each {
				total++
			}
		})
	}
	wg.Wait()
	fmt.Println(goroutines*each - total)
}
