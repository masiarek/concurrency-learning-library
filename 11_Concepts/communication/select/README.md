# Select

**Category:** [Communication](../README.md) · **Status:** stub · **Lessons:** [chapter 05, Message passing](../../../05_Message_Passing/README.md)

**One line:** Waiting on several channel operations or futures at once, and continuing with whichever becomes ready first.

Also called: select!, race.

## How it connects

```mermaid
flowchart LR
  n_channel["Channel"]
  n_select["Select"]
  n_select -->|uses| n_channel
  classDef center stroke-width:3px
  class n_select center
  classDef outside stroke-dasharray: 4 3
  class n_channel outside
```

- **Is built on:** [Channel](../channel/README.md)
- **See also:** [Cancellation](../../async/cancellation/README.md), [Timeout](../../async/timeout/README.md)

## In each language

| | |
|---|---|
| Rust | none in std; crossbeam's [`select!` ↗](https://docs.rs/crossbeam/latest/crossbeam/channel/macro.select.html) runs a random one of the ready channel operations, and tokio's [`select!` ↗](https://docs.rs/tokio/latest/tokio/macro.select.html) returns when the first branch completes and cancels the rest |
| Go | the [`select` ↗](https://go.dev/ref/spec#Select_statements) statement: when several cases can proceed, one is chosen by uniform pseudo-random selection; a `default` case makes it non-blocking |
| C | [`select` ↗](https://pubs.opengroup.org/onlinepubs/9799919799/functions/select.html) and [`poll` ↗](https://pubs.opengroup.org/onlinepubs/9799919799/functions/poll.html) wait on file descriptors, not on in-memory channels |
| Java | [`CompletableFuture.anyOf` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/CompletableFuture.html) completes when any of the given futures does; NIO's [`Selector` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/nio/channels/Selector.html) multiplexes selectable I/O channels |
| Python | [`asyncio.wait` ↗](https://docs.python.org/3/library/asyncio-task.html#asyncio.wait) with `return_when=FIRST_COMPLETED` returns the done and pending sets as soon as any awaitable finishes |
| C# | [`Task.WhenAny` ↗](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany) completes when any of the supplied tasks has completed |
| JavaScript | [`Promise.race` ↗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race) settles with the eventual state of the first promise to settle |
| Kotlin | the experimental [`select` ↗](https://kotlinlang.org/docs/select-expression.html) expression, which is biased to the first clause when several are ready, unlike Go's random choice |
| Erlang and Elixir | [`receive` ↗](https://www.erlang.org/doc/system/expressions.html) takes the first message in the queue that matches any clause, with an optional `after` timeout |
| The operating system | [epoll ↗](https://man7.org/linux/man-pages/man7/epoll.7.html), like `select` and `poll`, monitors many file descriptors to see which can do I/O |
| Elsewhere | Clojure core.async's [`alts!` ↗](https://clojure.github.io/core.async/) |

## Where to read more

- **In this library:** [What does a wait return when the time runs out?](../../../04_Waiting_For_Each_Other/waiting_with_a_timeout/README.md)
- **In this library:** [How does one thread wait on several channels at once?](../../../05_Message_Passing/waiting_on_several_channels/README.md)
- **In a sibling library:** [Go: `select` waits on many channels ↗](https://masiarek.github.io/go-learning-library/03_Select/select_waits_on_many/index.html)
- **In a sibling library:** [Go: `select` chooses at random ↗](https://masiarek.github.io/go-learning-library/03_Select/select_chooses_at_random/index.html)
- **In a sibling library:** [Go: A nil channel disables a case ↗](https://masiarek.github.io/go-learning-library/03_Select/a_nil_channel_disables_a_case/index.html)
- **In the books:** [*Learn Concurrent Programming with Go*](../../../10_Resources/books_go/README.md#cutajar_learn_concurrent_programming_with_go), James Cutajar — ch. 8, 'Selecting channels'
- **In the books:** [*Modern Multithreading*](../../../10_Resources/books_general/README.md#carver_tai_modern_multithreading), Richard H. Carver, Kuo-Chung Tai — ch. 5, 'Message Passing' → 'Selective Wait'
- **In the books:** [*Concurrency in Go*](../../../10_Resources/books_go/README.md#cox_buday_concurrency_in_go), Katherine Cox-Buday — ch. 3, 'Go’s Concurrency Building Blocks' → 'The select Statement'
- **In the books:** [*Advanced Programming in the UNIX Environment*](../../../10_Resources/books_c/README.md#stevens_rago_apue), W. Richard Stevens, Stephen A. Rago — ch. 14, 'Advanced I/O' → 'select and pselect Functions'
- **In the books:** [*Learning Go*](../../../10_Resources/books_go/README.md#bodner_learning_go), Jon Bodner — ch. 12, 'Concurrency in Go' → 'select'
- **In the books:** [*The Go Programming Language*](../../../10_Resources/books_go/README.md#donovan_kernighan_go_programming_language), Alan A. A. Donovan, Brian W. Kernighan — ch. 8, 'Goroutines and Channels' → 'Multiplexing with select'

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
