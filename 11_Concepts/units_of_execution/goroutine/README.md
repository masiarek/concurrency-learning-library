# Goroutine

**Category:** [Units of execution](../README.md) · **Status:** stub · **Lessons:** [chapter 01, Threads](../../../01_Threads/README.md)

**One line:** Go's unit of concurrency: a function call started with the `go` statement and scheduled by the Go runtime onto a small pool of operating-system threads.

## How it connects

```mermaid
flowchart LR
  n_goroutine["Goroutine"]
  n_green_thread["Green threads and M:N scheduling"]
  n_goroutine -->|is a| n_green_thread
  classDef center stroke-width:3px
  class n_goroutine center
  classDef outside stroke-dasharray: 4 3
  class n_green_thread outside
```

- **Is a kind of:** [Green threads and M:N scheduling](../green_thread/README.md)
- **See also:** [Channel](../../communication/channel/README.md), [Communicating sequential processes](../../communication/csp/README.md), [Daemon and detached threads](../daemon_thread/README.md), [Preemptive scheduling](../../scheduling/preemptive_scheduling/README.md)

## In each language

| | |
|---|---|
| Rust | [`tokio::spawn` ↗](https://docs.rs/tokio/latest/tokio/task/fn.spawn.html) is the nearest, and returns a `JoinHandle` |
| Go | The [`go` statement ↗](https://go.dev/ref/spec#Go_statements) discards the function's results, and a goroutine has [no ID ↗](https://go.dev/doc/faq#no_goroutine_id) to hold on to |
| Java | [Virtual threads ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Thread.html#virtual-threads) are the nearest: scheduled by the Java runtime, but still `Thread` objects that can be joined |
| Kotlin | [`launch` ↗](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/launch.html) returns a `Job`, and `Job.join` suspends until the coroutine completes |
| Erlang and Elixir | [`spawn` ↗](https://www.erlang.org/doc/apps/erts/erlang.html#spawn/1) returns a pid, which is used to send the process messages |
| Haskell | [`forkIO` ↗](https://hackage.haskell.org/package/base/docs/Control-Concurrent.html#v:forkIO) returns a `ThreadId` to kill it by; waiting for it is written by hand, for instance with an `MVar` |

## Where to read more

- **In this library:** [Who waits when main returns?](../../../01_Threads/who_waits_when_main_returns/README.md)
- **In this library:** [Getting a result back](../../../01_Threads/getting_a_result_back/README.md)
- **In a sibling library:** [Go: `main` does not wait ↗](https://masiarek.github.io/go-learning-library/01_Goroutines/main_does_not_wait/index.html)
- **In a sibling library:** [Go: A goroutine has no handle ↗](https://masiarek.github.io/go-learning-library/01_Goroutines/a_goroutine_has_no_handle/index.html)
- **In a sibling library:** [Go: A panic ends the whole program ↗](https://masiarek.github.io/go-learning-library/01_Goroutines/a_panic_ends_the_whole_program/index.html)
- **In a sibling library:** [Go: Goroutines are cheap ↗](https://masiarek.github.io/go-learning-library/01_Goroutines/goroutines_are_cheap/index.html)
- **In the books:** [*Concurrency in Go*](../../../10_Resources/books_go/README.md#cox_buday_concurrency_in_go), Katherine Cox-Buday — ch. 3, 'Go’s Concurrency Building Blocks' → 'Goroutines'
- **In the books:** [*Learn Concurrent Programming with Go*](../../../10_Resources/books_go/README.md#cutajar_learn_concurrent_programming_with_go), James Cutajar — ch. 2, 'Dealing with threads' → 'What’s so special about goroutines?'
- **In the books:** [*Effective Concurrency in Go*](../../../10_Resources/books_go/README.md#serdar_effective_concurrency_in_go), Burak Serdar — ch. 2, 'Go Concurrency Primitives' → 'Goroutines'
- **In the books:** [*The Go Programming Language*](../../../10_Resources/books_go/README.md#donovan_kernighan_go_programming_language), Alan A. A. Donovan, Brian W. Kernighan — ch. 8, 'Goroutines and Channels'
- **In the books:** [*The Go Programming Language Phrasebook*](../../../10_Resources/books_go/README.md#chisnall_go_phrasebook), David Chisnall — ch. 9, 'Goroutines'
- **In the books:** [*Go Systems Programming*](../../../10_Resources/books_go/README.md#tsoukalos_go_systems_programming), Mihalis Tsoukalos — ch. 9, 'Goroutines — Basic Features'
- **Notes:** [Concurrency in Go - Main ↗](https://docs.google.com/document/d/1pBqchTSqkZvxYku7BahB5--c2HWLa3OBx_Mj5g4VOHs/edit)
- **Reference:** [The Go spec: Go statements ↗](https://go.dev/ref/spec#Go_statements)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
