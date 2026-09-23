# Can a thread wait forever for a lock that is always free eventually?

**Level:** 201 · anyone whose one slow thread never got its turn

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A mutex promises exclusion, not turn-taking: a lock that is released and immediately retaken by the same fast thread can leave a waiting thread starved for as long as the fast one keeps going, and the fair locks that prevent it — Java's fairness flag, Go's starvation mode after a millisecond — cost throughput for the promise.

## The question

One thread locks, does a microsecond of work, unlocks, and loops. A second thread wants the lock once. How long does it wait? Under an unfair lock, possibly the whole run: the first thread re-acquires before the second is even scheduled. The page counts the acquisitions each thread makes in one second, then turns fairness on where the language allows it.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `std::sync::Mutex` makes no fairness promise; the counts are lopsided |
| Go | `sync.Mutex` switches to starvation mode when a waiter has waited over 1 ms, so the waiter gets in |
| C | `pthread_mutex_t` promises nothing; the counts are the scheduler's |
| C++ | `std::mutex` promises nothing |
| Java | `new ReentrantLock(true)` grants the lock in arrival order |
| Python | `threading.Lock` promises nothing; the GIL's own switching interval bounds the wait |

## What the programs have to show

- the one-second race as *Real runs*: acquisitions by the hog and by the waiter, per language
- Java with and without the fairness flag, and Go's starvation-mode threshold measured
- the ticket lock, built in C, that is fair by construction

## See also

- Before this: [Can two threads be busy forever and get nothing done?](../livelock/README.md)
- After this: [How does a low-priority thread block a high-priority one?](../priority_inversion/README.md)
- [When is a read-write lock faster than a mutex?](../../02_Shared_State/readers_and_writers/README.md)
- [Can two threads be busy forever and get nothing done?](../livelock/README.md)
- Concepts: [Starvation](../../11_Concepts/hazards/starvation/README.md) · [Liveness failure](../../11_Concepts/hazards/liveness_failure/README.md) · [Mutex](../../11_Concepts/synchronization/mutex/README.md) · [Contention](../../11_Concepts/hazards/contention/README.md) · [Scheduling policy](../../11_Concepts/scheduling/scheduling_policy/README.md)
