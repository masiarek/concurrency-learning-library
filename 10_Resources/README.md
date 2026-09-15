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

On the shelf beside this library:

- *C++ Concurrency in Action*, 2nd edition — Anthony Williams (Manning, 2019).
- *The Art of Concurrency: A Thread Monkey's Guide to Writing Parallel Applications* — Clay Breshears (O'Reilly, 2009).
- *Concurrency in Go* — Katherine Cox-Buday (O'Reilly, 2017).
- *Learn Concurrent Programming with Go* — James Cutajar (Manning, 2024).
- *Effective Concurrency in Go* — Burak Serdar (Packt, 2023).
- *Parallel and Concurrent Programming in Haskell* — Simon Marlow (O'Reilly, 2013).
- *Concurrency in .NET* — Riccardo Terrell (Manning, 2018).
- *Concurrent Programming on Windows* — Joe Duffy (Addison-Wesley, 2008).
- *Programming Elixir ≥ 1.6* — Dave Thomas (Pragmatic Bookshelf, 2018).
- *The Little Elixir & OTP Guidebook* — Benjamin Tan Wei Hao (Manning, 2016).
- *Programming Erlang* — Joe Armstrong (Pragmatic Bookshelf).
- *Functional and Concurrent Programming* — Michel Charpentier (Addison-Wesley, 2022).
- *Linux System Programming* — Robert Love (O'Reilly).

## The same topic in the sibling libraries

Each row is a topic, the lessons here that ask about it, and the pages elsewhere that go deeper for one language.

| Topic | Here | Rust | Elsewhere |
|---|---|---|---|
| Starting a thread, and waiting for it | [Who waits when main returns?](../01_Threads/who_waits_when_main_returns/README.md) · [Getting a result back](../01_Threads/getting_a_result_back/README.md) | [Spawning a thread ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/spawning_a_thread/index.html) | |
| Moving a value to another thread | *chapter 05, planned* | [Channels ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/channels/index.html) · [Sharing across threads: `Arc` ↗](https://masiarek.github.io/rust-learning-library/18_Ownership/sharing_across_threads/index.html) | |
| What may cross a thread boundary | *chapter 02, planned* | [`Send` and `Sync` ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/send_and_sync/index.html) | |
| Data races | *chapter 02, planned* | [Data races ↗](https://masiarek.github.io/rust-learning-library/31_C_and_Cpp/data_races/index.html), for C and C++ programmers | Python: [The format mini-language ↗](https://masiarek.github.io/python-learning-library/01_Text_and_Bytes/the_format_mini_language/index.html) — its `n` type can change the process's locale while other threads are running |
| Locks, and locks going wrong | *chapters 02 and 03, planned* | [`RwLock` and atomics ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/rwlock_and_atomics/index.html) · [Lock poisoning ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/mutex_poisoning/index.html) · [Forgotten unlock ↗](https://masiarek.github.io/rust-learning-library/31_C_and_Cpp/forgotten_unlock/index.html) | |
| Async | *chapter 06, planned* | [Instrumenting async code ↗](https://masiarek.github.io/rust-learning-library/21_Observability/instrumenting_async/index.html) | |
| Concurrent processes | *chapter 08, planned* | | Linux: [head closes the pipe early ↗](https://masiarek.github.io/linux-learning-library/01_Pipelines/head_closes_the_pipe_early/index.html) · [A pipeline reports its last command ↗](https://masiarek.github.io/linux-learning-library/01_Pipelines/a_pipeline_reports_its_last_command/index.html) · [Two terminals, one history file ↗](https://masiarek.github.io/linux-learning-library/06_History/two_terminals_one_history_file/index.html) |
