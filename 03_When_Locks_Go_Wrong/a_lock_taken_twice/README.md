# What happens when a thread takes a lock it already holds?

**Level:** 201 · anyone whose helper function locks the same mutex as its caller

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A thread that locks a mutex it already holds deadlocks against itself in Rust, Go and C, is undefined behaviour in C++ unless the mutex is recursive, and simply proceeds in Java, where every monitor is reentrant — and a reentrant lock is not the fix it looks like, because the inner call runs with the invariant half-restored.

## The question

`update()` locks the table and calls `log_change()`, which also locks the table. One thread, one lock, two acquisitions. What happens depends entirely on the language: a hang, a crash, a return value, or silent success. The page runs it, then asks the harder question — if the lock *is* reentrant, what state does `log_change` see?

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `Mutex::lock` twice on one thread: the docs say it may deadlock or panic; on this platform it hangs |
| Go | `sync.Mutex` is not reentrant and hangs; if it is the only goroutine, the runtime reports the deadlock |
| C | `PTHREAD_MUTEX_NORMAL` hangs, `ERRORCHECK` returns `EDEADLK`, `RECURSIVE` counts |
| C++ | `std::mutex` twice is undefined; `std::recursive_mutex` counts |
| Java | `synchronized` and `ReentrantLock` are reentrant; the hold count is observable |
| Python | `threading.Lock` hangs; `threading.RLock` counts |

## What the programs have to show

- the double lock per language under a two-second timeout: the exit and the message
- the reentrant variants, and the count they report
- the invariant case: a reentrant inner call reading a struct the outer call has half-updated

## See also

- Before this: [Why do two locks taken in different orders hang?](../two_locks_in_different_orders/README.md)
- After this: [Who unlocks when the function returns early?](../the_forgotten_unlock/README.md)
- [Why do two locks taken in different orders hang?](../two_locks_in_different_orders/README.md)
- Concepts: [Reentrant lock](../../11_Concepts/synchronization/reentrant_lock/README.md) · [Reentrancy](../../11_Concepts/safety_in_languages/reentrancy/README.md) · [Deadlock](../../11_Concepts/hazards/deadlock/README.md) · [Mutex](../../11_Concepts/synchronization/mutex/README.md)
