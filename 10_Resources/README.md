# 10 — Resources

## The primary sources

Every page here can be checked against these. Where a page says what a language promises, it links one of them rather than paraphrasing from memory.

**Rust**

- [**`std::thread`** ↗](https://doc.rust-lang.org/std/thread/index.html) — the module documentation, including what happens to the other threads when the main thread ends. [**`thread::scope`** ↗](https://doc.rust-lang.org/std/thread/fn.scope.html) — the construct that waits.
- [**Rust Atomics and Locks** ↗](https://marabos.nl/atomics/) — Mara Bos's book, free to read online. Its first chapter's first program is where [Who waits when main returns?](../01_Threads/who_waits_when_main_returns/README.md) starts.

**Go**

- [**The Go Programming Language Specification** ↗](https://go.dev/ref/spec) — the sections *Go statements* and *Program execution*. [**The Go Memory Model** ↗](https://go.dev/ref/mem) — what one goroutine may assume about what another has written.
- [**`sync`** ↗](https://pkg.go.dev/sync) — `WaitGroup`, `Mutex`, `Once`.

**C**

- **POSIX threads**: [`pthread_create` ↗](https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_create.html), [`pthread_join` ↗](https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_join.html), [`pthread_exit` ↗](https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_exit.html), in POSIX.1-2024.
- [**The `main` function** ↗](https://en.cppreference.com/w/c/language/main_function) on cppreference — what returning from `main` means.

**C++**

- [**Concurrency support library** ↗](https://en.cppreference.com/w/cpp/thread) on cppreference — `std::thread`, `std::jthread`, `std::async`, `std::future`, mutexes and atomics.

**Java**

- [**`java.lang.Thread`** ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Thread.html) and [**`java.util.concurrent`** ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/package-summary.html), for Java 25.
- [**JEP 444: Virtual Threads** ↗](https://openjdk.org/jeps/444) and [**JEP 512: Compact Source Files and Instance Main Methods** ↗](https://openjdk.org/jeps/512) — the second is why the Java examples here have no class declaration.

**Python**

- [**`threading`** ↗](https://docs.python.org/3/library/threading.html) and [**`concurrent.futures`** ↗](https://docs.python.org/3/library/concurrent.futures.html).
- [**PEP 703: Making the Global Interpreter Lock Optional** ↗](https://peps.python.org/pep-0703/) — the free-threaded build.

## Books

The concurrency books on the shelf beside this library, plus a few worth knowing that are not, grouped by the language they focus on. Each entry gives the author, publisher and year from the book's own title pages, its example code where the book names a repository, and its chapters — every chapter for a book about concurrency, only the concurrency chapters for a broader one. The concept pages cite the chapters that cover each concept, and each book lists the concepts that cite it.

<!-- concepts:books -->

| Focus | Books | On the shelf | Whole-book concurrency titles |
|---|---|---|---|
| [General and cross-language](books_general/README.md) | 15 | 13 | 11 |
| [Rust](books_rust/README.md) | 13 | 13 | 4 |
| [Go](books_go/README.md) | 10 | 10 | 3 |
| [C](books_c/README.md) | 8 | 8 | 2 |
| [C++](books_cpp/README.md) | 10 | 10 | 9 |
| [Java](books_java/README.md) | 9 | 8 | 3 |
| [C# and .NET](books_csharp_dotnet/README.md) | 7 | 7 | 5 |
| [Python](books_python/README.md) | 22 | 15 | 13 |
| [Haskell](books_haskell/README.md) | 3 | 3 | 1 |
| [Erlang and Elixir](books_elixir_erlang/README.md) | 8 | 8 | 2 |
| [Scala and functional programming](books_scala_jvm_functional/README.md) | 7 | 7 | 1 |
| [JavaScript](books_javascript/README.md) | 7 | 7 | 3 |
| [Swift](books_swift/README.md) | 1 | 1 | 1 |
| [Other languages](books_other/README.md) | 7 | 7 | 3 |

<!-- /concepts:books -->

Python concurrency books have a well-kept outside list too: Jason Brownlee's [Python Concurrency Books ↗](https://superfastpython.com/python-concurrency-books/) on SuperFastPython, with each book's concurrency chapters.

## The same topic in the sibling libraries

Each row is a topic, its concept pages, the lessons here that ask about it, and the pages in the language libraries that go deeper for one language. The [concept pages](../11_Concepts/README.md) carry the same links concept by concept.

| Topic | Concepts | Here | Rust | Go | Elsewhere |
|---|---|---|---|---|---|
| Starting a thread, and waiting for it | [Thread](../11_Concepts/units_of_execution/thread/README.md) · [Join](../11_Concepts/async/join/README.md) · [Goroutine](../11_Concepts/units_of_execution/goroutine/README.md) | [Who waits when main returns?](../01_Threads/who_waits_when_main_returns/README.md) · [Getting a result back](../01_Threads/getting_a_result_back/README.md) | [Spawning a thread ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/spawning_a_thread/index.html) | [`main` does not wait ↗](https://masiarek.github.io/go-learning-library/01_Goroutines/main_does_not_wait/index.html) · [A goroutine has no handle ↗](https://masiarek.github.io/go-learning-library/01_Goroutines/a_goroutine_has_no_handle/index.html) · [Goroutines are cheap ↗](https://masiarek.github.io/go-learning-library/01_Goroutines/goroutines_are_cheap/index.html) | |
| A failure inside a thread | [Liveness failure](../11_Concepts/hazards/liveness_failure/README.md) · [Lock poisoning](../11_Concepts/synchronization/lock_poisoning/README.md) | *chapter 01, planned* | [Spawning a thread ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/spawning_a_thread/index.html) | [A panic ends the whole program ↗](https://masiarek.github.io/go-learning-library/01_Goroutines/a_panic_ends_the_whole_program/index.html) | |
| Moving a value to another thread | [Channel](../11_Concepts/communication/channel/README.md) · [Unbuffered channel](../11_Concepts/communication/unbuffered_channel/README.md) · [Buffered and bounded channels](../11_Concepts/communication/bounded_channel/README.md) | *chapter 05, planned* | [Channels ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/channels/index.html) · [Sharing across threads: `Arc` ↗](https://masiarek.github.io/rust-learning-library/18_Ownership/sharing_across_threads/index.html) | [An unbuffered send waits for a receiver ↗](https://masiarek.github.io/go-learning-library/02_Channels/an_unbuffered_send_waits_for_a_receiver/index.html) · [A buffered channel is a bounded queue ↗](https://masiarek.github.io/go-learning-library/02_Channels/a_buffered_channel_is_a_bounded_queue/index.html) · [Closing a channel ends a range ↗](https://masiarek.github.io/go-learning-library/02_Channels/closing_a_channel_ends_a_range/index.html) | |
| Waiting on several things at once | [Select](../11_Concepts/communication/select/README.md) · [Timeout](../11_Concepts/async/timeout/README.md) | *chapter 05, planned* | | [`select` waits on many channels ↗](https://masiarek.github.io/go-learning-library/03_Select/select_waits_on_many/index.html) · [`select` chooses at random ↗](https://masiarek.github.io/go-learning-library/03_Select/select_chooses_at_random/index.html) · [A timeout is a channel ↗](https://masiarek.github.io/go-learning-library/03_Select/a_timeout_is_a_channel/index.html) | |
| What may cross a thread boundary | [Send and Sync](../11_Concepts/safety_in_languages/send_and_sync/README.md) · [Thread safety](../11_Concepts/safety_in_languages/thread_safety/README.md) | *chapter 02, planned* | [`Send` and `Sync` ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/send_and_sync/index.html) | | |
| Data races and lost updates | [Race condition](../11_Concepts/hazards/race_condition/README.md) · [Data race](../11_Concepts/hazards/data_race/README.md) · [Race detector](../11_Concepts/testing_and_tools/race_detector/README.md) | [Is `total += n` safe on two threads?](../02_Shared_State/the_lost_update/README.md) | [Data races ↗](https://masiarek.github.io/rust-learning-library/31_C_and_Cpp/data_races/index.html), for C and C++ programmers | [A mutex guards a counter ↗](https://masiarek.github.io/go-learning-library/04_Sync/a_mutex_guards_a_counter/index.html) · [The race detector ↗](https://masiarek.github.io/go-learning-library/07_Testing_Concurrent_Code/the_race_detector/index.html) | Python: [The format mini-language ↗](https://masiarek.github.io/python-learning-library/01_Text_and_Bytes/the_format_mini_language/index.html) — its `n` type can change the process's locale while other threads are running |
| Locks, atomics, and run-once | [Mutex](../11_Concepts/synchronization/mutex/README.md) · [Atomic variable](../11_Concepts/lock_free/atomic_variable/README.md) · [Run-once initialization](../11_Concepts/synchronization/once_initialization/README.md) | [Keeping every update](../02_Shared_State/keeping_every_update/README.md) · *run-once: chapter 04, planned* | [`RwLock` and atomics ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/rwlock_and_atomics/index.html) · [Lock poisoning ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/mutex_poisoning/index.html) · [Forgotten unlock ↗](https://masiarek.github.io/rust-learning-library/31_C_and_Cpp/forgotten_unlock/index.html) | [Atomic counters ↗](https://masiarek.github.io/go-learning-library/04_Sync/atomic_counters/index.html) · [`sync.Once` runs exactly once ↗](https://masiarek.github.io/go-learning-library/04_Sync/once_runs_exactly_once/index.html) · [A WaitGroup counts goroutines ↗](https://masiarek.github.io/go-learning-library/04_Sync/a_waitgroup_counts_goroutines/index.html) | |
| The lost update in a database | [Compare-and-swap](../11_Concepts/lock_free/compare_and_swap/README.md) · [MVCC](../11_Concepts/distributed/mvcc/README.md) | [The lost update in a database](../02_Shared_State/the_lost_update_in_a_database/README.md) | | | |
| When order changes a sum: floats, refusals, duplicates | [Idempotency](../11_Concepts/distributed/idempotency/README.md) | [When does order change a sum?](../02_Shared_State/when_order_changes_a_sum/README.md) | [What a float actually stores ↗](https://masiarek.github.io/rust-learning-library/19_Numbers/what_a_float_stores/index.html) · [Letting the compiler reorder a float sum ↗](https://masiarek.github.io/rust-learning-library/19_Numbers/letting_the_compiler_reorder/index.html) | | Math: [Catastrophic cancellation ↗](https://masiarek.github.io/math-learning-library/01_Precision/catastrophic_cancellation/index.html) |
| Deadlock | [Deadlock](../11_Concepts/hazards/deadlock/README.md) · [Leaked tasks](../11_Concepts/hazards/task_leak/README.md) | *chapter 03, planned* | | [All goroutines are asleep ↗](https://masiarek.github.io/go-learning-library/02_Channels/all_goroutines_are_asleep/index.html) · [A leaked goroutine never ends ↗](https://masiarek.github.io/go-learning-library/05_Context/a_leaked_goroutine_never_ends/index.html) | |
| Cancellation and deadlines | [Cancellation](../11_Concepts/async/cancellation/README.md) · [Structured concurrency](../11_Concepts/async/structured_concurrency/README.md) | *chapter 06, planned* | | [One `cancel` reaches every goroutine ↗](https://masiarek.github.io/go-learning-library/05_Context/cancel_reaches_every_goroutine/index.html) · [A deadline is a cancel with a clock ↗](https://masiarek.github.io/go-learning-library/05_Context/a_deadline_is_a_cancel_with_a_clock/index.html) · [Cancel with a cause ↗](https://masiarek.github.io/go-learning-library/05_Context/cancel_with_a_cause/index.html) | |
| Patterns | [Pipeline](../11_Concepts/communication/pipeline/README.md) · [Fan-out, fan-in](../11_Concepts/communication/fan_out_fan_in/README.md) · [Worker pool](../11_Concepts/communication/worker_pool/README.md) · [Semaphore](../11_Concepts/synchronization/semaphore/README.md) | *chapter 05, planned* | | [A pipeline of stages ↗](https://masiarek.github.io/go-learning-library/06_Patterns/a_pipeline_of_stages/index.html) · [Fan-out, fan-in ↗](https://masiarek.github.io/go-learning-library/06_Patterns/fan_out_fan_in/index.html) · [A worker pool ↗](https://masiarek.github.io/go-learning-library/06_Patterns/a_worker_pool/index.html) · [A buffered channel as a semaphore ↗](https://masiarek.github.io/go-learning-library/06_Patterns/a_buffered_channel_as_a_semaphore/index.html) · [The first error cancels the rest ↗](https://masiarek.github.io/go-learning-library/06_Patterns/first_error_cancels_the_rest/index.html) | |
| Async | [Async and await](../11_Concepts/async/async_await/README.md) · [Future and promise](../11_Concepts/async/future_and_promise/README.md) · [Event loop](../11_Concepts/scheduling/event_loop/README.md) | *chapter 06, planned* | [Instrumenting async code ↗](https://masiarek.github.io/rust-learning-library/21_Observability/instrumenting_async/index.html) | | |
| Testing concurrent code | [Deterministic scheduling for tests](../11_Concepts/testing_and_tools/deterministic_testing/README.md) · [Heisenbug](../11_Concepts/hazards/heisenbug/README.md) | *chapter 09, planned* | | [`synctest` makes time virtual ↗](https://masiarek.github.io/go-learning-library/07_Testing_Concurrent_Code/synctest_makes_time_virtual/index.html) · [`synctest.Wait` instead of a sleep ↗](https://masiarek.github.io/go-learning-library/07_Testing_Concurrent_Code/synctest_wait/index.html) | |
| Concurrent processes | [Process](../11_Concepts/units_of_execution/process/README.md) · [Inter-process communication](../11_Concepts/communication/ipc/README.md) | *chapter 08, planned* | | | Linux: [head closes the pipe early ↗](https://masiarek.github.io/linux-learning-library/01_Pipelines/head_closes_the_pipe_early/index.html) · [A pipeline reports its last command ↗](https://masiarek.github.io/linux-learning-library/01_Pipelines/a_pipeline_reports_its_last_command/index.html) · [Two terminals, one history file ↗](https://masiarek.github.io/linux-learning-library/06_History/two_terminals_one_history_file/index.html) |
