# Concurrency primitives

**Category:** [Foundations](../README.md) · **Status:** stub

**One line:** The building blocks a language or library provides for concurrent code, in four groups: synchronization (mutex, semaphore, condition variable), communication (channels, futures), task management (threads, tasks, pools) and atomics.

Also called: synchronization primitives, communication primitives.

## How it connects


- **See also:** [Atomic variable](../../lock_free/atomic_variable/README.md), [Channel](../../communication/channel/README.md), [Condition variable](../../synchronization/condition_variable/README.md), [Future and promise](../../async/future_and_promise/README.md), [Mutex](../../synchronization/mutex/README.md), [Semaphore](../../synchronization/semaphore/README.md), [Thread](../../units_of_execution/thread/README.md), [Thread pool and executor](../../units_of_execution/thread_pool/README.md)

## In each language

| | |
|---|---|
| Rust | [`std::sync` ↗](https://doc.rust-lang.org/std/sync/index.html) (`Mutex`, `RwLock`, `Condvar`, `Barrier`, `mpsc`, atomics) and [`std::thread` ↗](https://doc.rust-lang.org/std/thread/index.html) |
| Go | Channels in the language; [`sync` ↗](https://pkg.go.dev/sync), whose documentation says higher-level synchronization is better done with channels; and [`sync/atomic` ↗](https://pkg.go.dev/sync/atomic) |
| C | POSIX [`<pthread.h>` ↗](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/pthread.h.html), and C11's [`<threads.h>` ↗](https://en.cppreference.com/w/c/thread) and [`<stdatomic.h>` ↗](https://en.cppreference.com/w/c/atomic) |
| C++ | The [concurrency support library ↗](https://en.cppreference.com/w/cpp/thread): threads, mutexes, condition variables, semaphores, futures and atomics |
| Java | [`java.util.concurrent` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/package-summary.html), its `locks` and `atomic` subpackages, and the monitor every object has (`synchronized`, [`wait` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait%28%29), `notify`) |
| Python | [`threading` ↗](https://docs.python.org/3/library/threading.html) (`Lock`, `Condition`, `Semaphore`, `Event`, `Barrier`) and [`queue` ↗](https://docs.python.org/3/library/queue.html), with counterparts in [`asyncio` ↗](https://docs.python.org/3/library/asyncio-sync.html) |
| C# | [Overview of synchronization primitives ↗](https://learn.microsoft.com/en-us/dotnet/standard/threading/overview-of-synchronization-primitives) |
| JavaScript | Workers exchange messages with [`postMessage` ↗](https://developer.mozilla.org/en-US/docs/Web/API/Worker/postMessage); shared memory is a `SharedArrayBuffer` coordinated with [`Atomics` ↗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics) |
| Kotlin | [`Mutex` ↗](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.sync/-mutex/) and `Semaphore` for coroutines, which suspend rather than block; [`Channel` ↗](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.channels/-channel/) |
| Erlang and Elixir | Processes and messages; [ETS ↗](https://www.erlang.org/doc/apps/stdlib/ets.html) is built-in term storage for very large quantities of data |
| Haskell | [`MVar` ↗](https://hackage.haskell.org/package/base/docs/Control-Concurrent-MVar.html) and [`Chan` ↗](https://hackage.haskell.org/package/base/docs/Control-Concurrent-Chan.html) in `base`; `TVar` in the [`stm` ↗](https://hackage.haskell.org/package/stm/docs/Control-Concurrent-STM.html) package |
| The operating system | [`futex(2)` ↗](https://man7.org/linux/man-pages/man2/futex.2.html): a blocking construct for shared-memory synchronization, with most of the work done in user space |

## Where to read more

- **Notes:** [concurrency primitives ↗](https://docs.google.com/document/d/1ZbsuM7P2zKNut60H16h7r0d-ePIQjFCHXNVFEQqizLA/edit?tab=t.0)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
