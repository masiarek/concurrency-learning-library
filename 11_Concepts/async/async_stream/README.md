# Async stream

**Category:** [Async](../README.md) · **Status:** stub · **Lessons:** chapter 06, Async *(planned)*

**One line:** An asynchronous iterator: a sequence whose items arrive over time, each one awaited in turn.

Also called: Stream, async generator, AsyncIterator, Sink.

## How it connects

```mermaid
flowchart LR
  n_async_stream["Async stream"]
  n_future_and_promise["Future and promise"]
  n_reactive_programming["Reactive programming"]
  n_async_stream -->|uses| n_future_and_promise
  n_reactive_programming -->|uses| n_async_stream
  classDef center stroke-width:3px
  class n_async_stream center
  classDef outside stroke-dasharray: 4 3
  class n_future_and_promise,n_reactive_programming outside
```

- **Is built on:** [Future and promise](../future_and_promise/README.md)
- **Is used by:** [Reactive programming](../reactive_programming/README.md)

## In each language

| | |
|---|---|
| Rust | no stable trait: std's [`AsyncIterator` ↗](https://doc.rust-lang.org/std/async_iter/trait.AsyncIterator.html) is a nightly-only experimental API |
| Java | [`Flow.Publisher` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/Flow.html), with the subscriber requesting items |
| Python | [asynchronous generators ↗](https://docs.python.org/3/reference/expressions.html#asynchronous-generator-functions), consumed with [`async for` ↗](https://docs.python.org/3/reference/compound_stmts.html#async-for) |
| C# | [`IAsyncEnumerable<T>` ↗](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.iasyncenumerable-1), consumed with [`await foreach` ↗](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/generate-consume-asynchronous-stream) |
| JavaScript | [`async function*` ↗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function*) generators, consumed with [`for await...of` ↗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of) |
| Kotlin | [`Flow` ↗](https://kotlinlang.org/docs/coroutines-flow.html): a cold flow is lazy and runs anew for each collector, a hot flow shares its values with all collectors |
| Swift | [`AsyncSequence` ↗](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/), iterated with `for await`; an [`AsyncStream` ↗](https://developer.apple.com/documentation/swift/asyncstream) builds one from a closure |

## Where to read more

- **In the books:** [*C++ Reactive Programming*](../../../10_Resources/books_cpp/README.md#pai_abraham_cpp_reactive_programming), Praseed Pai, Peter Abraham — ch. 6, 'Introduction to Event Stream Programming Using C++'
- **In the books:** [*Concurrency in C# Cookbook*](../../../10_Resources/books_csharp_dotnet/README.md#cleary_concurrency_in_csharp_cookbook), Stephen Cleary — ch. 3, 'Asynchronous Streams'
- **In the books:** [*asyncio Recipes*](../../../10_Resources/books_python/README.md#tahrioui_asyncio_recipes), Mohamed Mustapha Tahrioui — ch. 4, 'Working with Async Generators'
- **In the books:** [*Kotlin Coroutines by Tutorials*](../../../10_Resources/books_other/README.md#babic_srivastava_kotlin_coroutines_by_tutorials), Filip Babić, Nishant Srivastava — ch. 14, 'Beginning with Coroutines Flow'
- **In the books:** [*Effective Concurrency in Go*](../../../10_Resources/books_go/README.md#serdar_effective_concurrency_in_go), Burak Serdar — ch. 8, 'Handling Requests Concurrently' → 'Streaming data'
- **In the books:** [*Learning Concurrent Programming in Scala*](../../../10_Resources/books_scala_jvm_functional/README.md#prokopec_learning_concurrent_programming_in_scala), Aleksandar Prokopec — ch. 10, 'Reactors' → 'Event streams'
- **Notes:** [sink - rust - futures::sink::Sink ↗](https://docs.google.com/document/d/1CqiyECIqf2na7Xlkc3WqurQf5kQxHDm44qY8-n3g_9s/edit?tab=t.0)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
