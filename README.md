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
| 01 | [Threads](01_Threads/README.md) | who waits when `main` returns, getting a result back, lending a local to a thread; then failures nobody waits for, thread counts, thread-locals, pools, goroutines against threads, sleep and yield | 3 lessons · 6 stubs |
| 02 | [Shared state](02_Shared_State/README.md) | the lost update, and keeping every update with a lock, an atomic or one owner; the same bug in a database; when order changes a sum; data race or race condition; then pairs of values, read-write locks, torn reads, check-then-act, ABA, `Send`/`Sync`, memory ordering | 5 lessons · 7 stubs |
| 03 | [When locks go wrong](03_When_Locks_Go_Wrong/README.md) | deadlock and lock order, a lock taken twice, forgotten unlocks, poisoning, livelock, starvation, priority inversion, spinlocks, finding the deadlock | 9 stubs |
| 04 | [Waiting for each other](04_Waiting_For_Each_Other/README.md) | condition variables and the lost wakeup, semaphores, barriers and latches, run-once, monitors, the bounded buffer, dining philosophers, timed waits | 9 stubs |
| 05 | [Message passing](05_Message_Passing/README.md) | who owns a sent value, unbuffered and bounded channels, closing, `select`, pipelines, fan-out and fan-in, worker pools, actors, publish-subscribe | 10 stubs |
| 06 | [Async](06_Async/README.md) | the event loop, futures, `async` and `await`, blocking the loop, callbacks, cancellation and timeouts, function coloring, leaked tasks, streams, runtimes, I/O multiplexing, the UI thread | 13 stubs |
| 07 | [Parallelism](07_Parallelism/README.md) | splitting a sum across workers; then real speedup, the GIL, Amdahl's law, false sharing, data against task parallelism, parallel iterators, fork-join, map-reduce, how many workers | 1 lesson · 9 stubs |
| 08 | [Processes](08_Processes/README.md) | `fork`, exit statuses, pipes, signals, `multiprocessing`, shared memory, zombies and orphans | 7 stubs |
| 09 | [Testing and tools](09_Testing_and_Tools/README.md) | race and memory error detectors, stress tests, virtual time, model checking, thread dumps, profiling, Heisenbugs | 8 stubs |
| 10 | [Resources](10_Resources/README.md) | the documentation, the books by language, and the crosswalk to the sibling libraries | |
| 11 | [Concepts](11_Concepts/README.md) | the map: over 150 concepts in 13 categories — an ontology, a schema of how they connect, abbreviations, and a page per concept with its name in each language | stubs |

## The concept map

The numbered chapters teach by question. [**Chapter 11**](11_Concepts/README.md) names things: [the ontology](11_Concepts/README.md) arranges concurrency's vocabulary into categories — foundations, units of execution, scheduling, hazards, synchronization, lock-free, communication, async, parallelism, safety in languages, distributed systems, real-time systems, testing and tools — with each concept under what it is a kind of; [the schema](11_Concepts/schema/README.md) draws what uses, prevents, causes or is confused with what. Every concept has a short page that names its construct in each language, with a link to that language's documentation, and links to the lessons here, the sibling libraries, the books and the notes it came from.

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
- [**JavaScript and TypeScript** ↗](https://masiarek.github.io/javascript-typescript-learning-library/) — one thread and an event loop: microtasks before timers, promises and `async`/`await`, cancellation with `AbortController`, and worker threads sharing memory through `Atomics`.
