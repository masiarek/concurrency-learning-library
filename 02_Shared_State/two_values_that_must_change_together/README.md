# Can two atomics keep two values consistent?

**Level:** 201 · anyone who made each field atomic and called the struct thread-safe

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A total and a count that are each updated atomically can still be read in a state where one has moved and the other has not, so the average is wrong; an atomic per value makes each *value* safe and the *pair* unsafe, and only a lock around both — or a single atomic holding both — keeps an invariant that spans two fields.

## The question

A running average keeps `total` and `count`. A writer adds a sample: `total += x; count += 1`, each an atomic add. A reader computes `total / count`. Between the writer's two adds, the reader sees a total with one more sample than the count — an average that was never true. This page forces that reading with a barrier, as [the lost update](../the_lost_update/README.md) does, and then shows the three fixes.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | two `AtomicU64`s show the bad average; `Mutex<(u64, u64)>` or one `AtomicU128`-shaped packing does not |
| Go | two `atomic.Int64`s, then a `sync.Mutex` around the pair |
| C | two `atomic_long`s, then a mutex; or one 64-bit atomic packing two 32-bit fields |
| C++ | `std::atomic<Pair>` is lock-free only if the pair fits a machine word — `is_lock_free()` says |
| Java | two `AtomicLong`s, then `synchronized`; or an `AtomicReference` to an immutable record replaced whole |
| Python | the GIL makes each bytecode atomic, not the pair; a `Lock` around both |

## What the programs have to show

- the forced interleaving: writer adds to `total`, waits at a barrier, reader averages, writer adds to `count` — the average is off by one sample on every run
- the same with a lock: never
- the immutable-snapshot fix, where the pair is replaced as one reference

## See also

- After this: [When is a read-write lock faster than a mutex?](../readers_and_writers/README.md)
- [Is `total += n` safe on two threads?](../the_lost_update/README.md)
- [Keeping every update](../keeping_every_update/README.md)
- The Rust library's [RwLock and atomics ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/rwlock_and_atomics/index.html)
- The Go library's [Atomic counters ↗](https://masiarek.github.io/go-learning-library/04_Sync/atomic_counters/index.html)
- Concepts: [Atomic variable](../../11_Concepts/lock_free/atomic_variable/README.md) · [Critical section](../../11_Concepts/synchronization/critical_section/README.md) · [Mutex](../../11_Concepts/synchronization/mutex/README.md) · [Safety failure](../../11_Concepts/hazards/safety_failure/README.md) · [Linearizability](../../11_Concepts/safety_in_languages/linearizability/README.md) · [Immutability](../../11_Concepts/safety_in_languages/immutability/README.md)
