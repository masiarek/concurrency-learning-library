# Reactive programming

**Category:** [Async](../README.md) · **Status:** stub

**One line:** Describing a program as streams of values over time and the values derived from them, with changes propagating through automatically.

Also called: Rx, ReactiveX, Reactive Extensions, observables.

## How it connects

```mermaid
flowchart LR
  n_async_stream["Async stream"]
  n_event_driven_programming["Event-driven programming"]
  n_reactive_programming["Reactive programming"]
  n_event_driven_programming ---|vs| n_reactive_programming
  n_reactive_programming -->|uses| n_async_stream
  classDef center stroke-width:3px
  class n_reactive_programming center
  classDef outside stroke-dasharray: 4 3
  class n_async_stream,n_event_driven_programming outside
```

- **Is built on:** [Async stream](../async_stream/README.md)
- **Often confused with:** [Event-driven programming](../event_driven_programming/README.md)
- **See also:** [Dataflow programming](../../communication/dataflow/README.md), [Publish-subscribe and broadcast](../../communication/publish_subscribe/README.md)

## In each language

| | |
|---|---|
| Java | [`Flow` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/Flow.html), the JDK's version of the reactive-streams interfaces |
| C# | [`IObservable<T>` ↗](https://learn.microsoft.com/en-us/dotnet/api/system.iobservable-1), a provider for push-based notification |
| Kotlin | [`Flow` ↗](https://kotlinlang.org/docs/coroutines-flow.html), including `StateFlow`, a `SharedFlow` that always holds the latest state value |
| Swift | [Combine ↗](https://developer.apple.com/documentation/combine): publishers expose values that change over time, and subscribers receive them |
| Elsewhere | [ReactiveX ↗](https://reactivex.io/intro.html), whose Observable is the asynchronous, push counterpart of an Iterable |

## Where to read more

- **In the books:** [*Async Rust*](../../../10_Resources/books_rust/README.md#flitton_morton_async_rust), Maxwell Flitton, Caroline Morton — ch. 6, 'Reactive Programming'
- **In the books:** [*C++ Reactive Programming*](../../../10_Resources/books_cpp/README.md#pai_abraham_cpp_reactive_programming), Praseed Pai, Peter Abraham — ch. 1, 'Reactive Programming Model – Overview and History'
- **In the books:** [*Learning Concurrent Programming in Scala*](../../../10_Resources/books_scala_jvm_functional/README.md#prokopec_learning_concurrent_programming_in_scala), Aleksandar Prokopec — ch. 6, 'Concurrent Programming with Reactive Extensions'
- **In the books:** [*Concurrency in .NET*](../../../10_Resources/books_csharp_dotnet/README.md#terrell_concurrency_in_dotnet), Riccardo Terrell — ch. 6, 'Real-time event streams: functional reactive programming'
- **In the books:** [*Combine: Asynchronous Programming with Swift*](../../../10_Resources/books_swift/README.md#kodeco_combine_asynchronous_programming_swift), Shai Mishali, Florent Pillet, Marin Todorov, Scott Gardner — ch. 1, 'Hello, Combine!'
- **In the books:** [*Kotlin Coroutines by Tutorials*](../../../10_Resources/books_other/README.md#babic_srivastava_kotlin_coroutines_by_tutorials), Filip Babić, Nishant Srivastava — ch. 1, 'What Is Asynchronous Programming' → 'Using reactive extensions for background work'
- **In the books:** [*Concurrency in C# Cookbook*](../../../10_Resources/books_csharp_dotnet/README.md#cleary_concurrency_in_csharp_cookbook), Stephen Cleary — ch. 1, 'Concurrency: An Overview' → 'Introduction to Reactive Programming (Rx)'
- **In the books:** [*Programming C# 12*](../../../10_Resources/books_csharp_dotnet/README.md#griffiths_programming_csharp), Ian Griffiths — ch. 11, 'Rx: Reactive Extensions'
- **Notes:** [Reactive Programming vs Asynchronous Programming ↗](https://docs.google.com/document/u/0/d/13Xtxk5uCx66-69cMmCQzR4AGM084u-7MvJ00xCiuCjs/edit)
- **Reference:** [Wikipedia: Reactive programming ↗](https://en.wikipedia.org/wiki/Reactive_programming)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
