# Run-once initialization

**Category:** [Synchronization](../README.md) · **Status:** stub · **Lessons:** [chapter 04, Waiting for each other](../../../04_Waiting_For_Each_Other/README.md)

**One line:** Running an initializer exactly once however many threads ask for it at the same moment, and handing all of them the same result.

Also called: lazy initialization, double-checked locking, sync.Once, OnceLock, call_once.

## How it connects

```mermaid
flowchart LR
  n_once_initialization["Run-once initialization"]
  n_synchronization["Synchronization"]
  n_once_initialization -->|is a| n_synchronization
  classDef center stroke-width:3px
  class n_once_initialization center
  classDef outside stroke-dasharray: 4 3
  class n_synchronization outside
```

- **Is a kind of:** [Synchronization](../synchronization/README.md)

## In each language

| | |
|---|---|
| Rust | [`Once` ↗](https://doc.rust-lang.org/std/sync/struct.Once.html), [`OnceLock` ↗](https://doc.rust-lang.org/std/sync/struct.OnceLock.html), and [`LazyLock` ↗](https://doc.rust-lang.org/std/sync/struct.LazyLock.html), a value initialized on first access that can live in a static |
| Go | [`sync.Once` ↗](https://pkg.go.dev/sync#Once) performs exactly one action; [`sync.OnceValue` ↗](https://pkg.go.dev/sync#OnceValue) (Go 1.21) returns a function that calls `f` only once |
| C | [`call_once` ↗](https://en.cppreference.com/w/c/thread/call_once) (C11) calls the function exactly once, even from several threads |
| C++ | [`std::call_once` ↗](https://en.cppreference.com/w/cpp/thread/call_once), and a [static local variable ↗](https://en.cppreference.com/w/cpp/language/storage_duration) is initialized exactly once even when threads reach it concurrently |
| Java | Class initialization runs under a unique per-class initialization lock ([JLS §12.4.2 ↗](https://docs.oracle.com/javase/specs/jls/se25/html/jls-12.html#jls-12.4.2)) |
| Python | Not [`functools.cached_property` ↗](https://docs.python.org/3/library/functools.html#functools.cached_property): since 3.12 it takes no lock, so synchronize the getter yourself |
| C# | [`Lazy<T>` ↗](https://learn.microsoft.com/en-us/dotnet/api/system.lazy-1) with `LazyThreadSafetyMode.ExecutionAndPublication`: the initialization is thread-safe, but the object it creates is not protected afterwards |
| Kotlin | [`by lazy` ↗](https://kotlinlang.org/docs/delegated-properties.html#lazy-properties) is synchronized by default: the value is computed in one thread and all threads see it |
| The operating system | POSIX [`pthread_once` ↗](https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_once.html): later calls with the same `once_control` do not call the routine again |

## Where to read more

- **In this library:** [How does initialization run exactly once with many threads racing to it?](../../../04_Waiting_For_Each_Other/run_exactly_once/README.md)
- **In a sibling library:** [Go: `sync.Once` runs exactly once ↗](https://masiarek.github.io/go-learning-library/04_Sync/once_runs_exactly_once/index.html)
- **In the books:** [*Programming with POSIX Threads*](../../../10_Resources/books_c/README.md#butenhof_programming_with_posix_threads), David R. Butenhof — ch. 5, 'Advanced Threaded Programming' → 'One-time initialization'
- **In the books:** [*Multi-Threaded Programming in C++*](../../../10_Resources/books_cpp/README.md#walmsley_multithreaded_programming_in_cpp), Mark Walmsley — ch. 7, 'Keys' → 'One-Time Initialization'
- **In the books:** [*The Go Programming Language*](../../../10_Resources/books_go/README.md#donovan_kernighan_go_programming_language), Alan A. A. Donovan, Brian W. Kernighan — ch. 9, 'Concurrency with Shared Variables' → 'Lazy Initialization: sync.Once'
- **In the books:** [*Effective Java*](../../../10_Resources/books_java/README.md#bloch_effective_java), Joshua Bloch — ch. 11, 'Concurrency' → 'Item 83: Use lazy initialization judiciously'
- **In the books:** [*C# 10 in a Nutshell*](../../../10_Resources/books_csharp_dotnet/README.md#albahari_csharp_in_a_nutshell), Joseph Albahari — ch. 21, 'Advanced Threading' → 'Lazy Initialization'
- **In the books:** [*The Go Programming Language Phrasebook*](../../../10_Resources/books_go/README.md#chisnall_go_phrasebook), David Chisnall — ch. 9, 'Goroutines' → 'Performing Thread-Safe Initialization'
- **Reference:** [Wikipedia: Double-checked locking ↗](https://en.wikipedia.org/wiki/Double-checked_locking)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
