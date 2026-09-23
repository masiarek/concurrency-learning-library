# Can one thread see another's writes out of order?

**Level:** 201 · anyone who reasoned about threads from the source order

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A write to `data` followed by a write to `ready` can be seen by another thread as `ready` first — the compiler may reorder them, and the CPU may make them visible in either order — unless the write to `ready` is a release and the read of it an acquire; the memory model is the contract that says which orders a program may rely on, and it is the same contract in C, C++, Rust and Java, spelled four ways.

## The question

Thread A: `data = 42; ready = true`. Thread B: `while !ready {}; print(data)`. Must B print 42? In the source, yes. On an ARM machine with plain stores, B can print 0. The page runs the store-buffering and message-passing litmus tests under each language's atomics with `Relaxed` and then with `Release`/`Acquire`, and counts the reorderings — as *Real runs*, since an x86 machine will show almost none and an ARM machine many.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `Ordering::Relaxed` permits the reordering; `Release` on the store and `Acquire` on the load forbid it |
| Go | the memory model gives happens-before through channels, mutexes and `sync/atomic`, and says not to rely on anything weaker |
| C | `memory_order_relaxed` against `memory_order_release`/`acquire` on `atomic_bool` |
| C++ | the same orderings under the same names; `std::atomic` defaults to `seq_cst` |
| Java | `volatile` gives sequential consistency for the field; a plain field gives nothing |
| Python | one interpreter lock: bytecodes are sequentially consistent, and the question does not arise on CPython |

## What the programs have to show

- the message-passing litmus test with relaxed atomics, a million iterations, counting the runs where `ready` was seen and `data` was stale — a *Real runs* fence on x86 and, when available, on arm64
- the same with release/acquire: zero, and the key
- the Java `volatile` and non-`volatile` field pair

## See also

- Before this: [What may be handed to another thread?](../what_may_cross_a_thread_boundary/README.md)
- [Is `total += n` safe on two threads?](../the_lost_update/README.md)
- [Can a read see half of a write?](../a_torn_read/README.md)
- The Rust library's [RwLock and atomics ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/rwlock_and_atomics/index.html)
- Concepts: [Weak memory models and reordering](../../11_Concepts/hazards/weak_memory_model/README.md) · [Happens-before](../../11_Concepts/lock_free/happens_before/README.md) · [Sequential consistency](../../11_Concepts/safety_in_languages/sequential_consistency/README.md) · [Atomic variable](../../11_Concepts/lock_free/atomic_variable/README.md) · [Cache coherence](../../11_Concepts/parallelism/cache_coherence/README.md)
