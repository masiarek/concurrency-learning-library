# Worker pool

**Category:** [Communication](../README.md) · **Status:** stub · **Lessons:** [chapter 05, Message passing](../../../05_Message_Passing/README.md)

**One line:** A fixed number of workers take jobs from one shared queue, which bounds how much work runs at once.

Also called: thread pool.

## How it connects

```mermaid
flowchart LR
  n_channel["Channel"]
  n_worker_pool["Worker pool"]
  n_worker_pool -->|uses| n_channel
  classDef center stroke-width:3px
  class n_worker_pool center
  classDef outside stroke-dasharray: 4 3
  class n_channel outside
```

- **Is built on:** [Channel](../channel/README.md)
- **See also:** [Fan-out, fan-in](../fan_out_fan_in/README.md), [Producer-consumer](../producer_consumer/README.md), [Task queue](../task_queue/README.md), [Thread pool and executor](../../units_of_execution/thread_pool/README.md)

## In each language

| | |
|---|---|
| Rust | no pool in std; the Rust Book [builds a `ThreadPool` ↗](https://doc.rust-lang.org/book/ch21-02-multithreaded.html) whose workers share one receiver behind `Arc<Mutex<T>>` |
| Go | no pool type: a fixed number of goroutines ranging over one jobs channel, the bounded parallelism of the Go blog's [pipelines post ↗](https://go.dev/blog/pipelines) |
| Java | [`Executors.newFixedThreadPool` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/Executors.html): a fixed number of threads operating off a shared unbounded queue |
| Python | [`ThreadPoolExecutor` ↗](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor) |
| C# | the process-wide [`ThreadPool` ↗](https://learn.microsoft.com/en-us/dotnet/api/system.threading.threadpool), which executes tasks, work items and asynchronous I/O |
| JavaScript | Node's [Worker Pool ↗](https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop) handles expensive tasks such as file I/O away from the event loop |
| Erlang and Elixir | [`Task.async_stream` ↗](https://hexdocs.pm/elixir/Task.html#async_stream/3) with `max_concurrency` |

## Where to read more

- **In this library:** [Why reuse a thread at all?](../../../01_Threads/reusing_threads_in_a_pool/README.md)
- **In this library:** [How does one stream split across workers and merge back?](../../../05_Message_Passing/fan_out_fan_in/README.md)
- **In this library:** [How do N workers share one queue of jobs?](../../../05_Message_Passing/a_worker_pool/README.md)
- **In a sibling library:** [Go: A worker pool ↗](https://masiarek.github.io/go-learning-library/06_Patterns/a_worker_pool/index.html)
- **In the books:** [*Effective Concurrency in Go*](../../../10_Resources/books_go/README.md#serdar_effective_concurrency_in_go), Burak Serdar — ch. 5, 'Worker Pools and Pipelines'
- **In the books:** [*Async Rust*](../../../10_Resources/books_rust/README.md#flitton_morton_async_rust), Maxwell Flitton, Caroline Morton — ch. 3, 'Building Our Own Async Queues' → 'Increasing Workers and Queues'
- **In the books:** [*Programming with POSIX Threads*](../../../10_Resources/books_c/README.md#butenhof_programming_with_posix_threads), David R. Butenhof — ch. 4, 'A Few Ways to Use Threads' → 'Work crew'
- **In the books:** [*The Little Elixir & OTP Guidebook*](../../../10_Resources/books_elixir_erlang/README.md#tan_little_elixir_otp_guidebook), Benjamin Tan Wei Hao — ch. 6, 'Fault tolerance with Supervisors' → 'Implementing Pooly: a worker-pool application'
- **In the books:** [*asyncio Recipes*](../../../10_Resources/books_python/README.md#tahrioui_asyncio_recipes), Mohamed Mustapha Tahrioui — ch. 5, 'Working with Async Context Manager' → 'Writing a Loop Worker Pool Async Context Manager'
- **In the books:** [*JavaScript Concurrency*](../../../10_Resources/books_javascript/README.md#boduch_javascript_concurrency), Adam Boduch — ch. 7, 'Abstracting Concurrency' → 'Worker pools'

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
