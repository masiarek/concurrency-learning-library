# Reentrant lock

**Category:** [Synchronization](../README.md) · **Status:** stub

**One line:** A lock that the thread already holding it may take again without deadlocking itself; it is released only when every acquisition has been undone.

Also called: recursive mutex, recursive lock, RLock.

## How it connects

```mermaid
flowchart LR
  n_mutex["Mutex"]
  n_reentrancy["Reentrancy"]
  n_reentrant_lock["Reentrant lock"]
  n_reentrancy ---|vs| n_reentrant_lock
  n_reentrant_lock -->|is a| n_mutex
  classDef center stroke-width:3px
  class n_reentrant_lock center
  classDef outside stroke-dasharray: 4 3
  class n_mutex,n_reentrancy outside
```

- **Is a kind of:** [Mutex](../mutex/README.md)
- **Often confused with:** [Reentrancy](../../safety_in_languages/reentrancy/README.md)

## In each language

| | |
|---|---|
| Rust | [`Mutex::lock` ↗](https://doc.rust-lang.org/std/sync/struct.Mutex.html#method.lock) is not reentrant — a second call may panic or deadlock; [`ReentrantLock` ↗](https://doc.rust-lang.org/std/sync/struct.ReentrantLock.html) is a nightly-only experimental API |
| Go | None: a [`sync.Mutex` ↗](https://pkg.go.dev/sync#Mutex) is not tied to a goroutine, so a second `Lock` from the same goroutine blocks like any other; `RWMutex` rules out recursive read-locking too |
| C | [`mtx_init` ↗](https://en.cppreference.com/w/c/thread/mtx_init) with `mtx_recursive` |
| C++ | [`std::recursive_mutex` ↗](https://en.cppreference.com/w/cpp/thread/recursive_mutex) |
| Java | Both locks are reentrant: [JLS §17.1 ↗](https://docs.oracle.com/javase/specs/jls/se25/html/jls-17.html#jls-17.1) lets a thread lock a monitor multiple times, and [`ReentrantLock` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/ReentrantLock.html) allows up to 2147483647 recursive locks |
| Python | [`threading.RLock` ↗](https://docs.python.org/3/library/threading.html#rlock-objects) may be acquired multiple times by the same thread |
| C# | [`System.Threading.Lock` ↗](https://learn.microsoft.com/en-us/dotnet/api/system.threading.lock) may be entered recursively and must be exited as many times |
| Kotlin | [`Mutex` ↗](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.sync/-mutex/) is non-reentrant: locking it again from the coroutine that holds it suspends |
| The operating system | POSIX [`PTHREAD_MUTEX_RECURSIVE` ↗](https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_mutex_lock.html) keeps a lock count; a Windows [critical section ↗](https://learn.microsoft.com/en-us/windows/win32/sync/critical-section-objects) lets its owner enter again without blocking |

## Where to read more

- **In this library:** [What happens when a thread takes a lock it already holds?](../../../03_When_Locks_Go_Wrong/a_lock_taken_twice/README.md)
- **In the books:** [*Multi-Threaded Programming in C++*](../../../10_Resources/books_cpp/README.md#walmsley_multithreaded_programming_in_cpp), Mark Walmsley — ch. 8, 'Multiple Mutexes' → 'The RECURSIVE MUTEX Class'
- **In the books:** [*Java Concurrency in Practice*](../../../10_Resources/books_java/README.md#goetz_java_concurrency_in_practice), Brian Goetz, Tim Peierls, Joshua Bloch, Joseph Bowbeer, David Holmes, Doug Lea — ch. 13, 'Explicit Locks' → 'Lock and ReentrantLock'
- **In the books:** [*The Art of Multiprocessor Programming*](../../../10_Resources/books_general/README.md#herlihy_shavit_art_of_multiprocessor_programming), Maurice Herlihy, Nir Shavit — ch. 8, 'Monitors and Blocking Synchronization' → 'Our Own Reentrant Lock'
- **Reference:** [Wikipedia: Reentrant mutex ↗](https://en.wikipedia.org/wiki/Reentrant_mutex)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
