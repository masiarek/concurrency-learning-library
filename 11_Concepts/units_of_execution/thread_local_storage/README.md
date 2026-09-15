# Thread-local storage

**Category:** [Units of execution](../README.md) · **Status:** stub · **Lessons:** chapter 02, Shared state *(planned)*

**One line:** A variable with a separate copy per thread, so each thread sees only its own value and no lock is needed.

Also called: TLS, thread-specific data, thread-local variable.

## How it connects

```mermaid
flowchart LR
  n_data_race["Data race"]
  n_thread_local_storage["Thread-local storage"]
  n_thread_local_storage -->|prevents| n_data_race
  classDef center stroke-width:3px
  class n_thread_local_storage center
  classDef outside stroke-dasharray: 4 3
  class n_data_race outside
```

- **Helps prevent:** [Data race](../../hazards/data_race/README.md)
- **See also:** [Task (async)](../async_task/README.md), [Thread confinement](../../safety_in_languages/thread_confinement/README.md)

## In each language

| | |
|---|---|
| Rust | [`thread_local!` ↗](https://doc.rust-lang.org/std/macro.thread_local.html) declares a [`LocalKey` ↗](https://doc.rust-lang.org/std/thread/struct.LocalKey.html), read through `with` |
| Go | None: goroutines are anonymous, with [no ID ↗](https://go.dev/doc/faq#no_goroutine_id) to attach state to, and request-scoped values travel in a [`context.Context` ↗](https://pkg.go.dev/context) |
| C | C11 [`_Thread_local` ↗](https://en.cppreference.com/w/c/language/storage_duration) (`thread_local` since C23), or POSIX [`pthread_key_create` ↗](https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_key_create.html) |
| C++ | [`thread_local` ↗](https://en.cppreference.com/w/cpp/language/storage_duration) (C++11) |
| Java | [`ThreadLocal` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/ThreadLocal.html), and [`ScopedValue` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/ScopedValue.html) (JDK 25) for immutable values bound for a scope |
| Python | [`threading.local` ↗](https://docs.python.org/3/library/threading.html#threading.local); concurrent code should use [`contextvars` ↗](https://docs.python.org/3/library/contextvars.html) instead, so that state does not bleed into other code |
| C# | [`ThreadLocal<T>` ↗](https://learn.microsoft.com/en-us/dotnet/api/system.threading.threadlocal-1), and [`AsyncLocal<T>` ↗](https://learn.microsoft.com/en-us/dotnet/api/system.threading.asynclocal-1) for a value that follows an asynchronous flow |
| Swift | [`TaskLocal` ↗](https://developer.apple.com/documentation/swift/tasklocal) values belong to a task and are inherited by its child tasks |
| Erlang and Elixir | Each process has its own [process dictionary ↗](https://www.erlang.org/doc/apps/erts/erlang.html#put/2) |

## Where to read more

- **In the books:** [*Async Rust*](../../../10_Resources/books_rust/README.md#flitton_morton_async_rust), Maxwell Flitton, Caroline Morton — ch. 7, 'Customizing Tokio' → 'Getting Unsafe with Thread Data'
- **In the books:** [*Pthreads Programming*](../../../10_Resources/books_c/README.md#nichols_pthreads_programming), Bradford Nichols, Dick Buttlar, Jacqueline Proulx Farrell — ch. 4, 'Managing Pthreads' → 'Keys: Using Thread-Specific Data'
- **In the books:** [*Concurrency with Modern C++*](../../../10_Resources/books_cpp/README.md#grimm_concurrency_with_modern_cpp), Rainer Grimm — ch. 3, 'Multithreading' → 'Thread-Local Data'
- **In the books:** [*The Art of Concurrency*](../../../10_Resources/books_general/README.md#breshears_art_of_concurrency), Clay Breshears — ch. 4, 'Eight Simple Rules for Designing Multithreaded Applications' → 'Rule 7: Use Thread-Local Storage Whenever Possible or Associate Locks to Specific Data'
- **In the books:** [*Programming with POSIX Threads*](../../../10_Resources/books_c/README.md#butenhof_programming_with_posix_threads), David R. Butenhof — ch. 5, 'Advanced Threaded Programming' → 'Thread-specific data'
- **In the books:** [*Multi-Threaded Programming in C++*](../../../10_Resources/books_cpp/README.md#walmsley_multithreaded_programming_in_cpp), Mark Walmsley — ch. 7, 'Keys' → 'Thread-Specific Storage'
- **Reference:** [Wikipedia: Thread-local storage ↗](https://en.wikipedia.org/wiki/Thread-local_storage)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
