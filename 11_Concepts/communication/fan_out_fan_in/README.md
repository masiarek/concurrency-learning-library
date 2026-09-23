# Fan-out, fan-in

**Category:** [Communication](../README.md) · **Status:** stub · **Lessons:** [chapter 05, Message passing](../../../05_Message_Passing/README.md)

**One line:** Spreading the items of one channel across several workers, then merging their results back into one channel.

## How it connects

```mermaid
flowchart LR
  n_channel["Channel"]
  n_fan_out_fan_in["Fan-out, fan-in"]
  n_fan_out_fan_in -->|uses| n_channel
  classDef center stroke-width:3px
  class n_fan_out_fan_in center
  classDef outside stroke-dasharray: 4 3
  class n_channel outside
```

- **Is built on:** [Channel](../channel/README.md)
- **See also:** [Pipeline](../pipeline/README.md), [Worker pool](../worker_pool/README.md)

## In each language

| | |
|---|---|
| Rust | fan-in comes free, since cloned `Sender`s all feed one [`mpsc` ↗](https://doc.rust-lang.org/std/sync/mpsc/index.html) receiver; fan-out needs that receiver shared, which the Rust Book does with [`Arc<Mutex<T>>` ↗](https://doc.rust-lang.org/book/ch21-02-multithreaded.html) |
| Go | several goroutines reading one channel (fan-out) and a merge copying many channels onto one (fan-in), both named in the Go blog's [pipelines post ↗](https://go.dev/blog/pipelines) |
| Java | [`ExecutorCompletionService` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/ExecutorCompletionService.html) puts each task on a queue as it completes, for `take` to collect |
| Python | [`asyncio.gather` ↗](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather) collects results in the order of its arguments, not the order they finish in |
| JavaScript | [`Promise.all` ↗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all) collects fulfillment values in the order of the promises passed, regardless of completion order |
| Kotlin | the guide's [fan-out ↗](https://kotlinlang.org/docs/channels.html#fan-out) (several coroutines receive from one channel) and [fan-in ↗](https://kotlinlang.org/docs/channels.html#fan-in) (several coroutines send to one) |
| Erlang and Elixir | [`Task.async_stream` ↗](https://hexdocs.pm/elixir/Task.html#async_stream/3) runs a function over a collection with up to `max_concurrency` tasks and returns results in input order unless `ordered: false` |

## Where to read more

- **In this library:** [How does one thread wait on several channels at once?](../../../05_Message_Passing/waiting_on_several_channels/README.md)
- **In this library:** [How does one stream split across workers and merge back?](../../../05_Message_Passing/fan_out_fan_in/README.md)
- **In this library:** [How do N workers share one queue of jobs?](../../../05_Message_Passing/a_worker_pool/README.md)
- **In a sibling library:** [Go: Fan-out, fan-in ↗](https://masiarek.github.io/go-learning-library/06_Patterns/fan_out_fan_in/index.html)
- **In the books:** [*Concurrency in Go*](../../../10_Resources/books_go/README.md#cox_buday_concurrency_in_go), Katherine Cox-Buday — ch. 4, 'Concurrency Patterns in Go' → 'Fan-Out, Fan-In'
- **In the books:** [*Effective Concurrency in Go*](../../../10_Resources/books_go/README.md#serdar_effective_concurrency_in_go), Burak Serdar — ch. 5, 'Worker Pools and Pipelines' → 'Pipelines, fan-out, and fan-in'
- **In the books:** [*Designing Distributed Systems*](../../../10_Resources/books_general/README.md#burns_designing_distributed_systems), Brendan Burns — ch. 7, 'Scatter/Gather'
- **In the books:** [*Effective Python*](../../../10_Resources/books_python/README.md#slatkin_effective_python), Brett Slatkin — ch. 7, 'Concurrency and Parallelism' → 'Item 57: Avoid Creating New Thread Instances for On-demand Fan-out'

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
