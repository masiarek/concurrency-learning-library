# Can two threads be busy forever and get nothing done?

**Level:** 201 · anyone who fixed a deadlock with a retry and made it worse

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** Two threads that each back off when they see the other's lock, and retry, can back off in lockstep forever — both running, neither progressing — which is a livelock, and it is what a deadlock turns into when the fix is a polite retry with no randomness.

## The question

Two threads each need two locks. Each takes its first, tries the second, and if it fails, releases the first and tries again — the textbook deadlock avoidance. Run in lockstep from a barrier, they release and retry together forever. The page forces the lockstep, shows the counters climbing with no transfer ever completing, and then adds the one thing that breaks it: a random backoff.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `try_lock` in a loop from a barrier: attempts climb into the thousands with zero successes, until the timeout |
| Go | `TryLock` (Go 1.18) in the same loop, same result |
| C | `pthread_mutex_trylock`, same |
| C++ | `try_lock`, same; `std::scoped_lock` is the deterministic fix |
| Java | `ReentrantLock.tryLock`, same |
| Python | `Lock.acquire(blocking=False)`, same |

## What the programs have to show

- the lockstep retry per language, killed by a timeout driver, printing the attempt counts and zero completed transfers
- the same with `sleep(random)` before retrying: completes, as *Real runs* with the number of retries
- the ordered-locks version, which needs no retry at all

## See also

- Before this: [What state is the data in after a thread died holding the lock?](../a_panic_while_holding_the_lock/README.md)
- After this: [Can a thread wait forever for a lock that is always free eventually?](../starvation_and_fairness/README.md)
- [Why do two locks taken in different orders hang?](../two_locks_in_different_orders/README.md)
- [Can a thread wait forever for a lock that is always free eventually?](../starvation_and_fairness/README.md)
- Concepts: [Livelock](../../11_Concepts/hazards/livelock/README.md) · [Liveness failure](../../11_Concepts/hazards/liveness_failure/README.md) · [Deadlock](../../11_Concepts/hazards/deadlock/README.md) · [Lock ordering](../../11_Concepts/synchronization/lock_ordering/README.md)
