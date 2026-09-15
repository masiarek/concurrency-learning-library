# Producer-consumer

**Category:** [Communication](../README.md) · **Status:** stub · **Lessons:** chapter 05, Message passing *(planned)*

**One line:** One or more tasks make work items and one or more take them from a shared queue, each side running at its own speed.

Also called: producer-consumer problem, bounded-buffer problem.

## How it connects

```mermaid
flowchart LR
  n_bounded_channel["Buffered and bounded channels"]
  n_producer_consumer["Producer-consumer"]
  n_task_queue["Task queue"]
  n_producer_consumer -->|uses| n_bounded_channel
  n_task_queue -->|uses| n_producer_consumer
  classDef center stroke-width:3px
  class n_producer_consumer center
  classDef outside stroke-dasharray: 4 3
  class n_bounded_channel,n_task_queue outside
```

- **Is built on:** [Buffered and bounded channels](../bounded_channel/README.md)
- **Is used by:** [Task queue](../task_queue/README.md)
- **See also:** [Classic synchronization problems](../../synchronization/classic_synchronization_problems/README.md), [Worker pool](../worker_pool/README.md)

## In each language

| | |
|---|---|
| Rust | threads sharing an [`mpsc` ↗](https://doc.rust-lang.org/std/sync/mpsc/index.html) channel, with a cloned `Sender` for each producer |
| Go | goroutines sharing a buffered [channel ↗](https://go.dev/ref/spec#Channel_types) |
| Java | [`BlockingQueue` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/BlockingQueue.html), which its docs say is designed primarily for producer-consumer queues |
| Python | [`queue.Queue` ↗](https://docs.python.org/3/library/queue.html#queue.Queue); `task_done` and `join` let a producer wait until every item has been processed |
| C# | [`System.Threading.Channels` ↗](https://learn.microsoft.com/en-us/dotnet/core/extensions/channels), data structures for passing data between producers and consumers asynchronously |
| Kotlin | a coroutine built with `produce` is a [channel producer ↗](https://kotlinlang.org/docs/channels.html) that consumers iterate over |

## Where to read more

- **In a sibling library:** [Go: A buffered channel is a bounded queue ↗](https://masiarek.github.io/go-learning-library/02_Channels/a_buffered_channel_is_a_bounded_queue/index.html)
- **In a sibling library:** [Go: A worker pool ↗](https://masiarek.github.io/go-learning-library/06_Patterns/a_worker_pool/index.html)
- **In the books:** [*Kotlin Coroutines by Tutorials*](../../../10_Resources/books_other/README.md#babic_srivastava_kotlin_coroutines_by_tutorials), Filip Babić, Nishant Srivastava — ch. 13, 'Producer & Actors'
- **In the books:** [*Effective Concurrency in Go*](../../../10_Resources/books_go/README.md#serdar_effective_concurrency_in_go), Burak Serdar — ch. 4, 'Some Well-Known Concurrency Problems' → 'The producer-consumer problem'
- **In the books:** [*Java Concurrency in Practice*](../../../10_Resources/books_java/README.md#goetz_java_concurrency_in_practice), Brian Goetz, Tim Peierls, Joshua Bloch, Joseph Bowbeer, David Holmes, Doug Lea — ch. 5, 'Building Blocks' → 'Blocking Queues and the Producer-consumer Pattern'
- **In the books:** [*Pro Asynchronous Programming with .NET*](../../../10_Resources/books_csharp_dotnet/README.md#blewett_clymer_pro_asynchronous_programming_dotnet), Richard Blewett, Andrew Clymer — ch. 10, 'TPL Dataflow' → 'Producer and Consumer Revisited'
- **In the books:** [*The Art of Multiprocessor Programming*](../../../10_Resources/books_general/README.md#herlihy_shavit_art_of_multiprocessor_programming), Maurice Herlihy, Nir Shavit — ch. 1, 'Introduction' → 'The Producer-Consumer Problem'
- **In the books:** [*The Little Book of Semaphores*](../../../10_Resources/books_general/README.md#downey_little_book_of_semaphores), Allen B. Downey — ch. 4, 'Classical synchronization problems' → 'Producer-consumer problem'
- **Reference:** [Wikipedia: Producer–consumer problem ↗](https://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
