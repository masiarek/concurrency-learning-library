# Semaphore

**Category:** [Synchronization](../README.md) · **Status:** stub · **Lessons:** chapter 04, Waiting for each other *(planned)*

**One line:** A counter of permits: taking one waits while none are left, and returning one lets a waiter in — a lock that up to n tasks may hold at once.

Also called: counting semaphore, binary semaphore.

## How it connects

```mermaid
flowchart LR
  n_semaphore["Semaphore"]
  n_synchronization["Synchronization"]
  n_semaphore -->|is a| n_synchronization
  classDef center stroke-width:3px
  class n_semaphore center
  classDef outside stroke-dasharray: 4 3
  class n_synchronization outside
```

- **Is a kind of:** [Synchronization](../synchronization/README.md)
- **See also:** [Buffered and bounded channels](../../communication/bounded_channel/README.md), [Classic synchronization problems](../classic_synchronization_problems/README.md), [Concurrency primitives](../../foundations/concurrency_primitives/README.md), [Latch](../latch/README.md)

## In each language

| | |
|---|---|
| Rust | None in [`std::sync` ↗](https://doc.rust-lang.org/std/sync/index.html); [`tokio::sync::Semaphore` ↗](https://docs.rs/tokio/latest/tokio/sync/struct.Semaphore.html) is fair, giving permits out in the order they were requested |
| Go | None in `sync`: a buffered channel serves as a counting semaphore, and [`golang.org/x/sync/semaphore` ↗](https://pkg.go.dev/golang.org/x/sync/semaphore) provides a weighted one |
| C | None in C11 [`<threads.h>` ↗](https://en.cppreference.com/w/c/thread); POSIX `sem_t` fills the gap |
| C++ | [`std::counting_semaphore` and `std::binary_semaphore` ↗](https://en.cppreference.com/w/cpp/thread/counting_semaphore) (C++20) |
| Java | [`Semaphore` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/Semaphore.html) with an optional fairness setting, which the untimed `tryAcquire` ignores |
| Python | [`threading.Semaphore` ↗](https://docs.python.org/3/library/threading.html#semaphore-objects), and `BoundedSemaphore`, which checks that it is not released too many times |
| C# | [`SemaphoreSlim` ↗](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim); blocked threads enter in no guaranteed order |
| Kotlin | [`Semaphore` ↗](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.sync/-semaphore/) in kotlinx.coroutines, fair and FIFO |
| The operating system | POSIX [`sem_wait` ↗](https://pubs.opengroup.org/onlinepubs/9799919799/functions/sem_wait.html) and [`sem_post` ↗](https://pubs.opengroup.org/onlinepubs/9799919799/functions/sem_post.html) |

## Where to read more

- **In a sibling library:** [Go: A buffered channel as a semaphore ↗](https://masiarek.github.io/go-learning-library/06_Patterns/a_buffered_channel_as_a_semaphore/index.html)
- **In a sibling library:** [Rust: Backpressure ↗](https://masiarek.github.io/rust-learning-library/35_Async/building_minidb/backpressure/index.html)
- **In the books:** [*Learn Concurrent Programming with Go*](../../../10_Resources/books_go/README.md#cutajar_learn_concurrent_programming_with_go), James Cutajar — ch. 5, 'Condition variables and semaphores'
- **In the books:** [*Multi-Threaded Programming in C++*](../../../10_Resources/books_cpp/README.md#walmsley_multithreaded_programming_in_cpp), Mark Walmsley — ch. 5, 'Semaphores'
- **In the books:** [*The Little Book of Semaphores*](../../../10_Resources/books_general/README.md#downey_little_book_of_semaphores), Allen B. Downey — ch. 2, 'Semaphores'
- **In the books:** [*Rust Atomics and Locks*](../../../10_Resources/books_rust/README.md#bos_rust_atomics_and_locks), Mara Bos — ch. 10, 'Ideas and Inspiration' → 'Semaphore'
- **In the books:** [*Pro Asynchronous Programming with .NET*](../../../10_Resources/books_csharp_dotnet/README.md#blewett_clymer_pro_asynchronous_programming_dotnet), Richard Blewett, Andrew Clymer — ch. 4, 'Basic Thread Safety' → 'A Semaphore Out of the Box'
- **In the books:** [*Python Concurrency with asyncio*](../../../10_Resources/books_python/README.md#fowler_python_concurrency_with_asyncio), Matthew Fowler — ch. 11, 'Synchronization' → 'Limiting concurrency with semaphores'
- **Notes:** [Semaphores in general - semaphore ↗](https://docs.google.com/document/d/1vTOfVk_ZB8ZA6WoWB9w1vR-B07Gt4y5w3JdLC7SL9RY/edit)
- **Reference:** [Wikipedia: Semaphore (programming) ↗](https://en.wikipedia.org/wiki/Semaphore_(programming))
- **Reference:** [Allen B. Downey: The Little Book of Semaphores ↗](https://greenteapress.com/wp/semaphores/)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
