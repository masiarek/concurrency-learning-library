# Immutability

**Category:** [Safety in languages](../README.md) · **Status:** stub

**One line:** Data that cannot change after it is built can be shared by any number of threads with no synchronization at all.

Also called: immutable object, persistent data structure.

## How it connects

```mermaid
flowchart LR
  n_data_race["Data race"]
  n_immutability["Immutability"]
  n_immutability -->|prevents| n_data_race
  classDef center stroke-width:3px
  class n_immutability center
  classDef outside stroke-dasharray: 4 3
  class n_data_race outside
```

- **Helps prevent:** [Data race](../../hazards/data_race/README.md)

## In each language

| | |
|---|---|
| Rust | The default: [shared references disallow mutation ↗](https://doc.rust-lang.org/std/sync/struct.Arc.html), so data behind an `Arc` changes only through a `Mutex`, `RwLock` or atomic inside it |
| Go | [Strings are immutable ↗](https://go.dev/ref/spec#String_types): once created, a string's contents cannot change |
| C++ | A [`const` object ↗](https://en.cppreference.com/w/cpp/language/cv) cannot be modified, except for its `mutable` members |
| Java | [JLS §17.5 `final` field semantics ↗](https://docs.oracle.com/javase/specs/jls/se25/html/jls-17.html#jls-17.5) keep objects such as `String` immutable even when references to them cross threads through data races |
| Python | [Frozen dataclasses ↗](https://docs.python.org/3/library/dataclasses.html#frozen-instances) raise `FrozenInstanceError` on assignment |
| C# | [`System.Collections.Immutable` ↗](https://learn.microsoft.com/en-us/dotnet/api/system.collections.immutable) collections cannot be changed once created |
| JavaScript | [`Object.freeze` ↗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze) is shallow: objects nested in a frozen object can still change |

## Where to read more

- **In the books:** [*Concurrency in .NET*](../../../10_Resources/books_csharp_dotnet/README.md#terrell_concurrency_in_dotnet), Riccardo Terrell — ch. 3, 'Functional data structures and immutability'
- **In the books:** [*Java Concurrency in Practice*](../../../10_Resources/books_java/README.md#goetz_java_concurrency_in_practice), Brian Goetz, Tim Peierls, Joshua Bloch, Joseph Bowbeer, David Holmes, Doug Lea — ch. 3, 'Sharing Objects' → 'Immutability'
- **In the books:** [*Programming Concurrency on the JVM*](../../../10_Resources/books_java/README.md#subramaniam_programming_concurrency_on_the_jvm), Venkat Subramaniam — ch. 3, 'Design Approaches' → 'Purely Immutable Design'
- **In the books:** [*Concurrency in C# Cookbook*](../../../10_Resources/books_csharp_dotnet/README.md#cleary_concurrency_in_csharp_cookbook), Stephen Cleary — ch. 9, 'Collections' → 'Immutable Stacks and Queues'
- **In the books:** [*Functional and Concurrent Programming*](../../../10_Resources/books_scala_jvm_functional/README.md#charpentier_functional_and_concurrent_programming), Michel Charpentier — ch. 19, 'Thread-Safe Objects' → 'Immutable Objects'
- **Reference:** [Wikipedia: Immutable object ↗](https://en.wikipedia.org/wiki/Immutable_object)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
