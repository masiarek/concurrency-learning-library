# Critical section

**Category:** [Synchronization](../README.md) · **Status:** stub · **Lessons:** [chapter 02, Shared state](../../../02_Shared_State/README.md)

**One line:** A stretch of code that touches shared state and must not be run by two tasks at once.

Also called: critical region.

## How it connects


- **See also:** [Mutual exclusion](../mutual_exclusion/README.md)

## In each language

| | |
|---|---|
| Rust | As long as the [`MutexGuard` ↗](https://doc.rust-lang.org/std/sync/struct.MutexGuard.html) lives: the mutex is unlocked when the guard is dropped |
| Go | Between [`Mutex.Lock` ↗](https://pkg.go.dev/sync#Mutex.Lock) and `Unlock`; a locked `Mutex` is not tied to the goroutine that locked it |
| C++ | The scope of a [`std::lock_guard` ↗](https://en.cppreference.com/w/cpp/thread/lock_guard), which owns the mutex for the duration of a scoped block |
| Java | A [`synchronized` statement ↗](https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.19): the monitor is unlocked whether the block completes normally or abruptly |
| Python | A `with lock:` block: [`threading` primitives ↗](https://docs.python.org/3/library/threading.html#using-locks-conditions-and-semaphores-in-the-with-statement) acquire on entry and release on exit |
| C# | The body of a [`lock` statement ↗](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/lock), released even if an exception is thrown |
| The operating system | Windows names an object after it: [critical section objects ↗](https://learn.microsoft.com/en-us/windows/win32/sync/critical-section-objects) work like a mutex for the threads of one process |

## Where to read more

- **In this library:** [Keeping every update](../../../02_Shared_State/keeping_every_update/README.md)
- **In a sibling library:** [Go: A mutex guards a counter ↗](https://masiarek.github.io/go-learning-library/04_Sync/a_mutex_guards_a_counter/index.html)
- **In the books:** [*Modern Multithreading*](../../../10_Resources/books_general/README.md#carver_tai_modern_multithreading), Richard H. Carver, Kuo-Chung Tai — ch. 2, 'The Critical Section Problem'
- **In the books:** [*Learn Concurrent Programming with Go*](../../../10_Resources/books_go/README.md#cutajar_learn_concurrent_programming_with_go), James Cutajar — ch. 4, 'Synchronization with mutexes' → 'Protecting critical sections with mutexes'
- **In the books:** [*Programming with POSIX Threads*](../../../10_Resources/books_c/README.md#butenhof_programming_with_posix_threads), David R. Butenhof — ch. 3, 'Synchronization' → 'Invariants, critical sections, and predicates'
- **In the books:** [*Python Asyncio Jump-Start*](../../../10_Resources/books_python/README.md#brownlee_python_asyncio_jump_start), Jason Brownlee — ch. 5, 'Queues and Synchronization Primitives' → 'How to Protect Critical Sections with a Mutex Lock'
- **In the books:** [*The Art of Concurrency*](../../../10_Resources/books_general/README.md#breshears_art_of_concurrency), Clay Breshears — ch. 3, 'Proving Correctness and Measuring Performance' → 'Example: The Critical Section Problem'
- **In the books:** [*The Art of Multiprocessor Programming*](../../../10_Resources/books_general/README.md#herlihy_shavit_art_of_multiprocessor_programming), Maurice Herlihy, Nir Shavit — ch. 2, 'Mutual Exclusion' → 'Critical Sections'
- **Reference:** [Wikipedia: Critical section ↗](https://en.wikipedia.org/wiki/Critical_section)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
