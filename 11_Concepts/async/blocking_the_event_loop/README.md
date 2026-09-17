# Blocking the event loop

**Category:** [Async](../README.md) · **Status:** stub · **Lessons:** chapter 06, Async *(planned)*

**One line:** A task that computes for a long time, or makes a blocking call, on the runtime's thread stops every other task on that thread until it is done.

Also called: blocking in async code.

## How it connects

```mermaid
flowchart LR
  n_blocking_the_event_loop["Blocking the event loop"]
  n_cooperative_scheduling["Cooperative scheduling"]
  n_starvation["Starvation"]
  n_blocking_the_event_loop -->|can cause| n_starvation
  n_cooperative_scheduling -->|can cause| n_blocking_the_event_loop
  classDef center stroke-width:3px
  class n_blocking_the_event_loop center
  classDef outside stroke-dasharray: 4 3
  class n_cooperative_scheduling,n_starvation outside
```

- **Can lead to:** [Starvation](../../hazards/starvation/README.md)
- **Can be caused by:** [Cooperative scheduling](../../scheduling/cooperative_scheduling/README.md)
- **See also:** [Event loop](../../scheduling/event_loop/README.md), [Function coloring](../function_coloring/README.md), [UI thread](../../units_of_execution/ui_thread/README.md)

## In each language

| | |
|---|---|
| Rust | tokio's [`spawn_blocking` ↗](https://docs.rs/tokio/latest/tokio/task/fn.spawn_blocking.html) runs blocking work on a thread dedicated to it, because a future that does not yield keeps the executor from driving other futures |
| Go | there is no event loop to block, and since [Go 1.14 ↗](https://go.dev/doc/go1.14#runtime) goroutines are asynchronously preemptible, so even a loop without function calls cannot hold up the scheduler |
| Java | a virtual thread that blocks releases its platform thread; [JEP 491 ↗](https://openjdk.org/jeps/491) (JDK 24) made that happen inside `synchronized` too |
| Python | blocking (CPU-bound) code should not be called directly; `loop.run_in_executor` or [`asyncio.to_thread` ↗](https://docs.python.org/3/library/asyncio-task.html#asyncio.to_thread) moves it off the loop ([asyncio guide ↗](https://docs.python.org/3/library/asyncio-dev.html#running-blocking-code)) |
| JavaScript | Node runs callbacks on the Event Loop and expensive tasks on a Worker Pool; a thread blocked on behalf of one client cannot serve any other ([guide ↗](https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop)) |

## Where to read more

- **In a sibling library:** [Rust: Diagnosing a stuck runtime ↗](https://masiarek.github.io/rust-learning-library/35_Async/building_minidb/diagnosing_a_stuck_runtime/index.html)
- **In a sibling library:** [Rust: Common async pitfalls ↗](https://masiarek.github.io/rust-learning-library/35_Async/common_async_pitfalls/index.html)
- **In the books:** [*Parallel Programming and Concurrency with C# 10 and .NET 6*](../../../10_Resources/books_csharp_dotnet/README.md#ashcraft_parallel_programming_concurrency_csharp10), Alvin Ashcraft — ch. 4, 'User Interface Responsiveness and Threading'
- **In the books:** [*Python Concurrency with asyncio*](../../../10_Resources/books_python/README.md#fowler_python_concurrency_with_asyncio), Matthew Fowler — ch. 6, 'Handling CPU-bound work'
- **In the books:** [*asyncio Recipes*](../../../10_Resources/books_python/README.md#tahrioui_asyncio_recipes), Mohamed Mustapha Tahrioui — ch. 10, 'Preventing Common Asyncio Mistakes'
- **In the books:** [*High Performance JavaScript*](../../../10_Resources/books_javascript/README.md#zakas_high_performance_javascript), Nicholas C. Zakas — ch. 6, 'Responsive Interfaces'

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
