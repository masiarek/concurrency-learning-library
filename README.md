# Concurrency — a learning library

**One question per page, put to six languages at once.** What happens to a thread when `main` returns? Where does a thread's answer go, and where does its failure go? Each page asks one question like that, answers it with a small program in Rust, Go, C, C++, Java and Python, and shows where the answers split. Every output on every page comes from a program that runs, and is checked against a recorded answer key in CI on Ubuntu and macOS.

## How it is organized

**Chapters are topics, not languages.** A chapter is a problem — starting and waiting, sharing memory, locks that go wrong, passing messages, async — and a lesson inside it is one idea. The languages live inside the lesson: a table with a row per language, then a section per language with its program and its verified output, always in the order Rust, Go, C, C++, Java, Python. A language that has nothing different to say is left out of that lesson rather than given a row that repeats another.

**The sibling libraries keep the depth.** When a language's own library already has the deep page — the Rust library's `Send` and `Sync`, or its data-race page for C programmers — the lesson here makes the cross-language point, shows the short program, and links there for the rest. [Resources](10_Resources/README.md) maps every topic to those pages.

**Languages without a toolchain here** — Erlang, Elixir, Haskell, C# — are linked and marked *(Not machine-checked here.)* until an example of theirs can run in CI.

## Start here

[**00 — Start here**](00_Start_Here/README.md) — who this is for, how a page is laid out, and what "verified" can and cannot mean when threads are involved.

## The chapters

| | Chapter | What it covers | |
|---|---|---|---|
| 01 | [Threads](01_Threads/README.md) | who waits when `main` returns, getting a result back | 2 lessons |
| 02 | Shared state | data races and lost updates, mutexes, atomics, thread-local storage | planned |
| 03 | When locks go wrong | deadlock and lock order, forgotten unlocks, poisoning | planned |
| 04 | Waiting for each other | condition variables, semaphores, barriers, run-once initialization | planned |
| 05 | Message passing | channels, closing a channel, `select`, bounded queues, actors | planned |
| 06 | Async | event loops, futures, `async` and `await`, blocking the loop, cancellation | planned |
| 07 | Parallelism | CPU-bound speedup, the GIL and free-threaded Python, Amdahl's law | planned |
| 08 | Processes | `fork`, `multiprocessing`, pipes, signals | planned |
| 09 | Testing and tools | ThreadSanitizer, Go's race detector, stress tests, deterministic schedulers | planned |
| 10 | [Resources](10_Resources/README.md) | the documentation, the books, and the crosswalk to the sibling libraries | |

## Running the examples

Each example is one file that needs nothing beyond its language's standard library. From the example's folder:

| Language | Needs | One example by hand |
|---|---|---|
| Rust | `rustc`, 2024 edition | `rustc --edition 2024 who_waits_rs.rs && ./who_waits_rs` |
| Go | Go 1.25 or later | `go build who_waits_go.go && ./who_waits_go` |
| C | a C17 compiler and POSIX threads | `cc -std=c17 -pthread who_waits_c.c -o who_waits_c && ./who_waits_c` |
| C++ | a C++20 compiler | `c++ -std=c++20 -pthread who_waits_cpp.cpp -o who_waits_cpp && ./who_waits_cpp` |
| Java | Java 25 or later | `java who_waits_java.java` |
| Python | Python 3 | `python3 who_waits_py.py` |

To run all of them and check every recorded output:

```bash
python3 tools/run_examples.py --check
```

## The one rule

No page hand-types what a program prints. A lesson marks the spot and the runner fills it from a real run, so an example that behaves differently on a new compiler or runtime breaks the build instead of quietly making a page wrong. Threads add a second rule: an answer key holds only what cannot vary from run to run, and what does vary is shown as a labelled count of real runs. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Sibling libraries

The same house rule, one language or one subject at a time. [Resources](10_Resources/README.md) maps each topic here to their pages.

- [**Rust** ↗](https://masiarek.github.io/rust-learning-library/) — threads, channels, `Arc`, `Send` and `Sync`, and lock poisoning in depth; and, for C and C++ programmers, data races and forgotten unlocks.
- [**C** ↗](https://masiarek.github.io/c-learning-library/) — building, decompiling, strings, and bytes on the wire.
- [**C++** ↗](https://masiarek.github.io/cpp-learning-library/) — clocks and benchmarking.
- [**Python** ↗](https://masiarek.github.io/python-learning-library/) — text and bytes, including the one formatting call that changes process-wide state.
- [**Java text** ↗](https://masiarek.github.io/java-text-learning-library/) — `char`, `String`, encodings and locales.
- [**Linux** ↗](https://masiarek.github.io/linux-learning-library/) — pipelines, which are concurrent processes, and the signal that ends them.
