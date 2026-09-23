# How do N threads wait for each other?

**Level:** 201 · anyone whose phases must not overlap

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A latch counts down once and then stays open, a barrier reopens for the next round, and both answer the question no mutex does — *have all of us reached this point?* — which is what the lessons in this library use to force an interleaving, and what a parallel algorithm uses between its phases.

## The question

Four workers each fill a quarter of an array, then each reads the whole array. The reads must not begin until every write is done. A join would work, but then the workers would have to be restarted for the read phase. A barrier lets the same four threads wait at the line between phases. The page shows the barrier between two phases, the latch that starts everyone together, and what a barrier's *leader* is for.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `std::sync::Barrier::wait` returns a `BarrierWaitResult` naming one leader; no latch in std |
| Go | `sync.WaitGroup` is a latch; a barrier is a channel closed by the last arrival |
| C | `pthread_barrier_t` in POSIX, absent on macOS; a mutex and condition variable otherwise |
| C++ | `std::latch` and `std::barrier` (C++20), the barrier with a completion function |
| Java | `CountDownLatch` and `CyclicBarrier` with a barrier action; `Phaser` for both |
| Python | `threading.Barrier` with an action, and `Event` as a latch |

## What the programs have to show

- two phases, four workers, a barrier between: the array is complete when every reader sees it
- the leader or barrier action printing once per round
- a broken barrier: one thread does not arrive, and what the others see under a timeout

## See also

- Before this: [What does a semaphore count?](../a_semaphore_counts_permits/README.md)
- After this: [How does initialization run exactly once with many threads racing to it?](../run_exactly_once/README.md)
- [Is `total += n` safe on two threads?](../../02_Shared_State/the_lost_update/README.md)
- [Splitting a sum across workers](../../07_Parallelism/splitting_a_sum_across_workers/README.md)
- The Go library's [A WaitGroup counts goroutines ↗](https://masiarek.github.io/go-learning-library/04_Sync/a_waitgroup_counts_goroutines/index.html)
- Concepts: [Barrier](../../11_Concepts/synchronization/barrier/README.md) · [Latch](../../11_Concepts/synchronization/latch/README.md) · [Synchronization](../../11_Concepts/synchronization/synchronization/README.md) · [Fork-join](../../11_Concepts/parallelism/fork_join/README.md)
