# What state is the data in after a thread died holding the lock?

**Level:** 201 · anyone who has seen `PoisonError`

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A thread that panics or throws in the middle of a critical section leaves the data half-updated and, in every language but Rust, silently unlocked for the next thread to read; Rust marks the mutex *poisoned* so that the next `lock()` returns an error, which is not a way to fix the data but a way to make sure someone notices.

## The question

Inside the lock: `balance -= amount; panic!(); other += amount`. The thread dies. The lock is released — by the guard's destructor, by `synchronized`'s exit, by `defer`. The next thread locks and reads a balance that is short by `amount`. Rust alone refuses that read by default. The page shows the half-update in each language and the poison error, then what to do with it.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `lock()` returns `Err(PoisonError)` after a panic under the guard; `into_inner()` recovers the data on purpose |
| Go | a panic under `defer mu.Unlock()` unlocks; the next `Lock` sees the half-update |
| C | a thread cancelled or killed while holding a mutex leaves it locked forever unless it was `ROBUST` |
| C++ | `lock_guard` unlocks during unwinding; the next thread sees the half-update |
| Java | `synchronized` exits on the exception and the next thread sees the half-update |
| Python | `with lock:` releases on the exception; same |

## What the programs have to show

- the panicking critical section per language, and what the next reader prints
- Rust's `PoisonError` and the three responses: propagate, recover, or `clear_poison`
- C's `PTHREAD_MUTEX_ROBUST` and `EOWNERDEAD`, the one other language that says anything

## See also

- Before this: [Who unlocks when the function returns early?](../the_forgotten_unlock/README.md)
- After this: [Can two threads be busy forever and get nothing done?](../livelock/README.md)
- [Who unlocks when the function returns early?](../the_forgotten_unlock/README.md)
- [What does a failure on a thread do when nobody is waiting for it?](../../01_Threads/a_failure_nobody_is_waiting_for/README.md)
- The Rust library's [Lock poisoning ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/mutex_poisoning/index.html)
- Concepts: [Lock poisoning](../../11_Concepts/synchronization/lock_poisoning/README.md) · [Safety failure](../../11_Concepts/hazards/safety_failure/README.md) · [Mutex](../../11_Concepts/synchronization/mutex/README.md) · [Critical section](../../11_Concepts/synchronization/critical_section/README.md)
