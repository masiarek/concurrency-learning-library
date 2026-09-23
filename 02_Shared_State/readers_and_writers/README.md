# When is a read-write lock faster than a mutex?

**Level:** 201 · anyone whose data is read a thousand times for every write

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A read-write lock lets any number of readers in at once and one writer alone, which is a win only when reads are long and writes rare; a short read under an `RwLock` can cost more than the same read under a plain mutex, writers can starve behind a stream of readers, and Python has no such lock at all.

## The question

Eight readers and one writer share a table. With a mutex, every read waits for every other read. With a read-write lock, reads overlap and only the writer waits. So the read-write lock is faster — except when it is not, which is often: the lock's own bookkeeping is heavier, and a writer waiting for the readers to drain may wait a long time. The page measures both and shows the writer-starvation case.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `std::sync::RwLock`; whether writers are preferred is the platform's (`pthread_rwlock`'s) choice, and the docs say so |
| Go | `sync.RWMutex`, which blocks new readers once a writer is waiting |
| C | `pthread_rwlock_t`; writer preference is an attribute on some systems |
| C++ | `std::shared_mutex` with `shared_lock` and `unique_lock` |
| Java | `ReentrantReadWriteLock`, with an optional fairness flag; `StampedLock` for optimistic reads |
| Python | none in the standard library; a mutex, or one written from a `Condition` |

## What the programs have to show

- eight readers each reading a thousand times while one writer writes ten times: the total reads and writes, same under both locks
- a *Real runs* fence with the time under a mutex and under the read-write lock, reads short and reads long
- a writer that waits for a continuous stream of readers: how long, per language

## See also

- Before this: [Can two atomics keep two values consistent?](../two_values_that_must_change_together/README.md)
- After this: [Can a read see half of a write?](../a_torn_read/README.md)
- [Keeping every update](../keeping_every_update/README.md)
- [Can a thread wait forever for a lock that is always free eventually?](../../03_When_Locks_Go_Wrong/starvation_and_fairness/README.md)
- The Rust library's [RwLock and atomics ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/rwlock_and_atomics/index.html)
- Concepts: [Read-write lock](../../11_Concepts/synchronization/read_write_lock/README.md) · [Mutex](../../11_Concepts/synchronization/mutex/README.md) · [Starvation](../../11_Concepts/hazards/starvation/README.md) · [Contention](../../11_Concepts/hazards/contention/README.md)
