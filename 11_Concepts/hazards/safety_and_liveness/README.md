# Safety and liveness

**Category:** [Hazards](../README.md) · **Status:** stub · **Lessons:** chapter 03, When locks go wrong *(planned)*

**One line:** The two kinds of correctness for a concurrent program: safety means nothing bad ever happens, liveness means something good eventually does.

Also called: safety property, liveness property.

## How it connects


- **See also:** [Liveness failure](../liveness_failure/README.md), [Safety failure](../safety_failure/README.md)

## In each language

| | |
|---|---|
| Rust | [The Rustonomicon: Data races and race conditions ↗](https://doc.rust-lang.org/nomicon/races.html): safe Rust guarantees there are no data races, a safety property, but counts getting deadlocked as safe, so liveness is left to the program |
| Java | [JLS §17.1 ↗](https://docs.oracle.com/javase/specs/jls/se25/html/jls-17.html#jls-17.1): the language neither prevents nor requires detection of deadlock, so liveness is the program's job |

## Where to read more

- **In the books:** [*Java Concurrency in Practice*](../../../10_Resources/books_java/README.md#goetz_java_concurrency_in_practice), Brian Goetz, Tim Peierls, Joshua Bloch, Joseph Bowbeer, David Holmes, Doug Lea — ch. 2, 'Thread Safety' → 'Liveness and Performance'
- **In the books:** [*Concurrent Programming on Windows*](../../../10_Resources/books_csharp_dotnet/README.md#duffy_concurrent_programming_on_windows), Joe Duffy — ch. 11, 'Concurrency Hazards' → 'Liveness Hazards'
- **In the books:** [*Concurrent Programming: Algorithms, Principles, and Foundations*](../../../10_Resources/books_general/README.md#raynal_concurrent_programming_algorithms), Michel Raynal — ch. 5, 'Mutex-Free Concurrent Objects' → 'Mutex-Freedom and Progress Conditions'
- **In the books:** [*Operating System Concepts*](../../../10_Resources/books_c/README.md#silberschatz_operating_system_concepts), Abraham Silberschatz, Peter Baer Galvin, Greg Gagne — ch. 6, 'Synchronization Tools' → 'Liveness'
- **Reference:** [Wikipedia: Liveness ↗](https://en.wikipedia.org/wiki/Liveness)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
