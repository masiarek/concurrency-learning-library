# Shared memory

**Category:** [Communication](../README.md) · **Status:** stub · **Lessons:** chapter 02, Shared state *(planned)*

**One line:** Tasks read and write the same memory directly and coordinate with locks or atomics — the fastest way to share data, and the easiest to get wrong.

## How it connects

```mermaid
flowchart LR
  n_data_race["Data race"]
  n_message_passing["Message passing"]
  n_shared_memory["Shared memory"]
  n_message_passing ---|or| n_shared_memory
  n_shared_memory -->|can cause| n_data_race
  classDef center stroke-width:3px
  class n_shared_memory center
  classDef outside stroke-dasharray: 4 3
  class n_data_race,n_message_passing outside
```

- **Can lead to:** [Data race](../../hazards/data_race/README.md)
- **An alternative to:** [Message passing](../message_passing/README.md)
- **See also:** [Mutual exclusion](../../synchronization/mutual_exclusion/README.md)

## In each language

| | |
|---|---|
| Rust | an [`Arc` ↗](https://doc.rust-lang.org/std/sync/struct.Arc.html) is a thread-safe reference-counting pointer that does not allow mutation by itself; put a [`Mutex` ↗](https://doc.rust-lang.org/std/sync/struct.Mutex.html) or an atomic inside to mutate |
| Go | [`sync.Mutex` ↗](https://pkg.go.dev/sync#Mutex) and `sync/atomic` exist, but the [`sync` ↗](https://pkg.go.dev/sync) docs say most of them are for low-level library routines and higher-level synchronization is better done via channels |
| C | threads guard shared data with a mutex, [`pthread_mutex_lock` ↗](https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_mutex_lock.html) |
| C++ | [`std::mutex` ↗](https://en.cppreference.com/w/cpp/thread/mutex) and [`std::atomic` ↗](https://en.cppreference.com/w/cpp/atomic/atomic) |
| Java | `synchronized`, [`ReentrantLock` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/ReentrantLock.html), and atomics such as [`AtomicInteger` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/atomic/AtomicInteger.html) |
| Python | threads share objects and guard them with [`threading.Lock` ↗](https://docs.python.org/3/library/threading.html#threading.Lock); processes can share a block of memory through [`multiprocessing.shared_memory` ↗](https://docs.python.org/3/library/multiprocessing.shared_memory.html) (3.8) |
| C# | the [`lock` ↗](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/lock) statement |
| JavaScript | workers can share a [`SharedArrayBuffer` ↗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer), coordinated with [`Atomics` ↗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics) |
| Kotlin | [shared mutable state ↗](https://kotlinlang.org/docs/shared-mutable-state-and-concurrency.html) needs synchronizing as soon as coroutines run on a multi-threaded dispatcher such as `Dispatchers.Default` |
| Erlang and Elixir | an [ETS table ↗](https://www.erlang.org/doc/apps/stdlib/ets.html) created `public` can be read and written by any process |
| Haskell | an [`MVar` ↗](https://hackage.haskell.org/package/base/docs/Control-Concurrent-MVar.html), a synchronising variable, or [STM ↗](https://hackage.haskell.org/package/stm/docs/Control-Concurrent-STM.html) transactions |
| The operating system | [POSIX shared memory ↗](https://man7.org/linux/man-pages/man7/shm_overview.7.html): `shm_open` creates an object that each process maps into its address space with `mmap` |

## Where to read more

- **In the books:** [*Learn Concurrent Programming with Go*](../../../10_Resources/books_go/README.md#cutajar_learn_concurrent_programming_with_go), James Cutajar — ch. 3, 'Thread communication using memory sharing'
- **In the books:** [*C++ Concurrency in Action*](../../../10_Resources/books_cpp/README.md#williams_cpp_concurrency_in_action), Anthony Williams — ch. 3, 'Sharing data between threads'
- **In the books:** [*Java Concurrency in Practice*](../../../10_Resources/books_java/README.md#goetz_java_concurrency_in_practice), Brian Goetz, Tim Peierls, Joshua Bloch, Joseph Bowbeer, David Holmes, Doug Lea — ch. 3, 'Sharing Objects'
- **In the books:** [*Multithreaded JavaScript*](../../../10_Resources/books_javascript/README.md#hunter_english_multithreaded_javascript), Thomas Hunter II, Bryan English — ch. 4, 'Shared Memory'
- **In the books:** [*The Art of Multiprocessor Programming*](../../../10_Resources/books_general/README.md#herlihy_shavit_art_of_multiprocessor_programming), Maurice Herlihy, Nir Shavit — ch. 4, 'Foundations of Shared Memory'
- **In the books:** [*Async Rust*](../../../10_Resources/books_rust/README.md#flitton_morton_async_rust), Maxwell Flitton, Caroline Morton — ch. 2, 'Basic Async Rust' → 'Sharing Data Between Futures'
- **Reference:** [Wikipedia: Shared memory ↗](https://en.wikipedia.org/wiki/Shared_memory)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
