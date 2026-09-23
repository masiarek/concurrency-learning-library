# What is a goroutine, if not a thread?

**Level:** 201 · anyone moving between Go and a language with real threads

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A goroutine, a Java virtual thread and a Rust async task are all *user-space* units of execution that a runtime multiplexes onto a few operating-system threads — cheap to start, cheap to block, and invisible to the operating system — and the price is that a call which blocks the underlying thread without telling the runtime stalls every other unit sharing it.

## The question

`go f()` starts something that looks like a thread and is not one. Neither is `Thread.ofVirtual().start(...)` nor `tokio::spawn`. What do they share, where do they run, and what do they cost? The page starts all three, then asks the question that separates them from threads: what happens when one of them makes a blocking system call?

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | no green threads since 2014; async tasks on a runtime are the equivalent, and a blocking call inside one stalls its worker thread |
| Go | goroutines on `GOMAXPROCS` threads; the runtime moves a blocked goroutine off its thread, so a blocking syscall costs a thread, not the program |
| C | none: a thread is a thread, and any lighter unit is a library (`ucontext`, or a coroutine library) |
| C++ | none in std; C++20 coroutines are a building block without a scheduler |
| Java | virtual threads (Java 21) on a `ForkJoinPool` of carriers; a `synchronized` block used to pin the carrier, fixed in Java 24 |
| Python | `asyncio` tasks on one thread; `threading` threads are real ones |

## What the programs have to show

- ten thousand units started and joined, printing the count and the number of OS threads the process had at the peak
- one unit doing a blocking read on a pipe that is never written, while the others keep printing — or stop
- a *Real runs* fence with start time and memory for a thousand of each

## See also

- Before this: [Why reuse a thread at all?](../reusing_threads_in_a_pool/README.md)
- After this: [What does a sleep promise, and what does a yield?](../sleep_and_yield/README.md)
- [What does one blocking call do to every other task?](../../06_Async/blocking_the_event_loop/README.md)
- [How many threads can you start?](../how_many_threads_can_you_start/README.md)
- The Go library's [Goroutines are cheap ↗](https://masiarek.github.io/go-learning-library/01_Goroutines/goroutines_are_cheap/index.html)
- The Go library's [A goroutine has no handle ↗](https://masiarek.github.io/go-learning-library/01_Goroutines/a_goroutine_has_no_handle/index.html)
- The Rust library's [Tasks ↗](https://masiarek.github.io/rust-learning-library/35_Async/building_minidb/tasks/index.html)
- Concepts: [Goroutine](../../11_Concepts/units_of_execution/goroutine/README.md) · [Virtual thread](../../11_Concepts/units_of_execution/virtual_thread/README.md) · [Green threads and M:N scheduling](../../11_Concepts/units_of_execution/green_thread/README.md) · [Task (async)](../../11_Concepts/units_of_execution/async_task/README.md) · [Coroutine](../../11_Concepts/units_of_execution/coroutine/README.md) · [Context switch](../../11_Concepts/units_of_execution/context_switch/README.md) · [Scheduler](../../11_Concepts/scheduling/scheduler/README.md)
