# Lock poisoning

**Category:** [Synchronization](../README.md) · **Status:** stub · **Lessons:** chapter 03, When locks go wrong *(planned)*

**One line:** Marking a lock as suspect when a thread panics while holding it, so that the next thread to take it learns the data may be half-updated.

Also called: poisoned mutex, abandoned mutex.

## How it connects


- **See also:** [Mutex](../mutex/README.md), [Scoped locking](../scoped_lock/README.md)

## In each language

| | |
|---|---|
| Rust | [`Mutex` ↗](https://doc.rust-lang.org/std/sync/struct.Mutex.html#poisoning): a panic while holding the guard poisons it and later `lock` calls return an error, until `clear_poison` (Rust 1.77); [`Once` ↗](https://doc.rust-lang.org/std/sync/struct.Once.html) is poisoned the same way |
| Go | No poisoning: [`Mutex.Lock` ↗](https://pkg.go.dev/sync#Mutex.Lock) returns no value that could report a panic |
| Java | No poisoning: a [`synchronized` statement ↗](https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.19) unlocks the monitor when its block completes abruptly for any reason |
| C# | [`AbandonedMutexException` ↗](https://learn.microsoft.com/en-us/dotnet/api/system.threading.abandonedmutexexception) is thrown when a thread acquires a `Mutex` that another thread abandoned by exiting without releasing it |
| The operating system | POSIX robust mutexes: [`pthread_mutex_lock` ↗](https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_mutex_lock.html) returns `EOWNERDEAD` when the owner terminated while holding it, and [`pthread_mutex_consistent` ↗](https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_mutex_consistent.html) marks the state consistent again |

## Where to read more

- **In a sibling library:** [Rust: Lock poisoning ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/mutex_poisoning/index.html)
- **In a sibling library:** [Go: A mutex guards a counter ↗](https://masiarek.github.io/go-learning-library/04_Sync/a_mutex_guards_a_counter/index.html)
- **Reference:** [Rust std: Mutex poisoning ↗](https://doc.rust-lang.org/std/sync/struct.Mutex.html#poisoning)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
