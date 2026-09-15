# Weak memory models and reordering

**Category:** [Hazards](../README.md) · **Status:** stub · **Lessons:** [chapter 02, Shared state](../../../02_Shared_State/README.md)

**One line:** CPUs and compilers may perform memory reads and writes in a different order from the source code, and without synchronization another thread can see that order.

Also called: weak ordering, compiler reordering, store buffering.

## How it connects


- **See also:** [Data race](../data_race/README.md), [Happens-before](../../lock_free/happens_before/README.md)

## In each language

| | |
|---|---|
| Rust | [`atomic::Ordering` ↗](https://doc.rust-lang.org/std/sync/atomic/enum.Ordering.html): `Relaxed`, `Release`, `Acquire`, `AcqRel` and `SeqCst` choose how strongly each atomic operation synchronizes memory |
| Go | [The Go Memory Model ↗](https://go.dev/ref/mem) defines happens-before from sequenced-before and synchronized-before, and tells programs to serialize shared access rather than reason about the rest |
| C++ | [`std::memory_order` ↗](https://en.cppreference.com/w/cpp/atomic/memory_order): atomic operations default to sequentially consistent ordering, which can cost performance |
| Java | [JLS §17.4 Memory Model ↗](https://docs.oracle.com/javase/specs/jls/se25/html/jls-17.html#jls-17.4); the [`java.util.concurrent` memory consistency properties ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/package-summary.html#MemoryVisibility) list what happens-before what: unlocking a monitor, `volatile` writes, `Thread.start` and `join` |

## Where to read more

- **In a sibling library:** [Rust: Data races — the -O2 build that hides one ↗](https://masiarek.github.io/rust-learning-library/31_C_and_Cpp/data_races/index.html)
- **In the books:** [*Effective Concurrency in Go*](../../../10_Resources/books_go/README.md#serdar_effective_concurrency_in_go), Burak Serdar — ch. 3, 'The Go Memory Model'
- **In the books:** [*Rust Atomics and Locks*](../../../10_Resources/books_rust/README.md#bos_rust_atomics_and_locks), Mara Bos — ch. 3, 'Memory Ordering'
- **In the books:** [*C++ Concurrency in Action*](../../../10_Resources/books_cpp/README.md#williams_cpp_concurrency_in_action), Anthony Williams — ch. 5, 'The C++ memory model and operations on atomic types'
- **In the books:** [*Java Concurrency in Practice*](../../../10_Resources/books_java/README.md#goetz_java_concurrency_in_practice), Brian Goetz, Tim Peierls, Joshua Bloch, Joseph Bowbeer, David Holmes, Doug Lea — ch. 16, 'The Java Memory Model'
- **In the books:** [*Learning Concurrent Programming in Scala*](../../../10_Resources/books_scala_jvm_functional/README.md#prokopec_learning_concurrent_programming_in_scala), Aleksandar Prokopec — ch. 2, 'Concurrency on the JVM and the Java Memory Model'
- **In the books:** [*Concurrent Programming on Windows*](../../../10_Resources/books_csharp_dotnet/README.md#duffy_concurrent_programming_on_windows), Joe Duffy — ch. 10, 'Memory Models and Lock Freedom'
- **Notes:** [Weak ordering ↗](https://docs.google.com/document/u/0/d/1q9oyCBsb82pfr_krAMFzQ9GSzWvqMJIpHZNcbmDjvVc/edit)
- **Notes:** [weak memory model - C++ ↗](https://docs.google.com/document/u/0/d/1_6CERBnbsIcBVDea-m8QNIrYuvbn8dT2fMe13wPLAow/edit)
- **Notes:** [Compiler Reordering ↗](https://docs.google.com/document/d/1PWVZ3XkgJmEl7I8XTbD_yruu_OtYm5zBSATZaCyMJ3c/edit?tab=t.0)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
