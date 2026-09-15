// Splitting a sum across workers. Each goroutine adds its own run of values into
// a variable no other goroutine can see, and the partial sums are then combined
// two ways: one after another, and as a tree whose rounds add pairs at the same
// time. Then the same split, with floats.
//
//	go build split_sum_go.go && ./split_sum_go
package main

import (
	"fmt"
	"strings"
	"sync"
)

const workers = 8 // a power of two, so every round of the tree pairs everyone up

var values = []int{1, 4, 3, 9, 2, 8, 5, 1, 1, 6, 2, 7, 2, 5, 0, 4, 1, 8, 6, 5, 1, 2, 3, 9}

type number interface{ int | float64 }

// partialSums gives each worker an equal run of values. Each adds its run, left
// to right, into its own mySum, and stores the result in its own slot of sums:
// no two goroutines write the same variable.
func partialSums[T number](values []T, workers int) []T {
	width := len(values) / workers
	sums := make([]T, workers)
	var wg sync.WaitGroup
	for w := range workers {
		wg.Go(func() {
			run := values[w*width : (w+1)*width]
			mySum := run[0]
			for _, x := range run[1:] {
				mySum += x
			}
			sums[w] = mySum
		})
	}
	wg.Wait()
	return sums
}

// serialCombine is the master adding every partial sum into its own, one at a time.
func serialCombine[T number](sums []T) (T, int) {
	total := sums[0]
	for _, s := range sums[1:] {
		total += s
	}
	return total, len(sums) - 1
}

// treeCombine adds neighbouring pairs, every pair in its own goroutine, round
// after round until one value is left.
func treeCombine[T number](sums []T, showRounds bool) (total T, additions, rounds int) {
	level := sums
	for len(level) > 1 {
		next := make([]T, len(level)/2)
		var wg sync.WaitGroup
		for i := range next {
			wg.Go(func() { next[i] = level[2*i] + level[2*i+1] })
		}
		wg.Wait()
		additions += len(next)
		rounds++
		level = next
		if showRounds {
			fmt.Printf("tree, round %d: %s\n", rounds, joined(level))
		}
	}
	return level[0], additions, rounds
}

func joined[T number](xs []T) string {
	parts := make([]string, len(xs))
	for i, x := range xs {
		parts[i] = fmt.Sprint(x)
	}
	return strings.Join(parts, " ")
}

func main() {
	fmt.Printf("%d values, %d to each of %d workers\n", len(values), len(values)/workers, workers)
	partials := partialSums(values, workers)
	fmt.Println("partial sums:", joined(partials))
	total, additions := serialCombine(partials)
	fmt.Printf("serial combine: %d, after %d additions in %d rounds\n", total, additions, additions)
	total, additions, rounds := treeCombine(partials, true)
	fmt.Printf("tree combine: %d, after %d additions in %d rounds\n", total, additions, rounds)

	floats := make([]float64, len(values))
	for i, v := range values {
		floats[i] = float64(v) + 0.2
	}
	fmt.Println()
	fmt.Printf("the same %d values plus 0.2 each, as float64 (on paper, 99.8)\n", len(floats))
	loopTotal := 0.0
	for _, x := range floats {
		loopTotal += x
	}
	fmt.Printf("one loop over all %d: %v\n", len(floats), loopTotal)
	floatPartials := partialSums(floats, workers)
	serialTotal, _ := serialCombine(floatPartials)
	fmt.Println("partial sums, then serial:", serialTotal)
	treeTotal, _, _ := treeCombine(floatPartials, false)
	fmt.Println("partial sums, then tree:", treeTotal)
}
