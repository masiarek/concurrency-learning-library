# Why do five philosophers with five forks starve?

**Level:** 201 · anyone who wants the deadlock of chapter 03 in its original clothes

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** Five philosophers each pick up the fork on their left and then the one on their right, and if all five pick up their left fork at once nobody ever eats — Dijkstra's problem, which is the two-lock deadlock with five locks, and its four classic solutions are the four ways out of any lock-ordering deadlock.

## The question

The page forces the deadlock — every philosopher takes the left fork and waits at a barrier before reaching for the right — and then runs each solution: one philosopher picks up right-first (lock ordering), at most four may sit (a semaphore), a philosopher takes both forks or neither (a `scoped_lock`, or a waiter), and Chandy–Misra's dirty forks. Each solution's run prints how many times each philosopher ate, which is also the starvation check.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | five `Mutex`es and the forced deadlock; the solutions with `try_lock`, a `Semaphore` built from `Condvar`, and lock ordering |
| Go | five mutexes or five channels; the runtime reports the total deadlock |
| C | five `pthread_mutex_t`s; the classic textbook program |
| C++ | `std::scoped_lock(left, right)` is the both-or-neither solution in one line |
| Java | `ReentrantLock.tryLock` for the retry solution; `Semaphore(4)` for the seat limit |
| Python | `threading.Lock` per fork; the same four solutions |

## What the programs have to show

- the forced deadlock, killed by a timeout driver
- each solution running for a fixed number of meals per philosopher and printing the counts
- a *Real runs* fence on which philosopher eats most under the unfair solutions

## See also

- Before this: [How does a producer wait for room and a consumer wait for an item?](../the_bounded_buffer/README.md)
- After this: [What does a wait return when the time runs out?](../waiting_with_a_timeout/README.md)
- [Why do two locks taken in different orders hang?](../../03_When_Locks_Go_Wrong/two_locks_in_different_orders/README.md)
- [What does a semaphore count?](../a_semaphore_counts_permits/README.md)
- Concepts: [Classic synchronization problems](../../11_Concepts/synchronization/classic_synchronization_problems/README.md) · [Deadlock](../../11_Concepts/hazards/deadlock/README.md) · [Lock ordering](../../11_Concepts/synchronization/lock_ordering/README.md) · [Starvation](../../11_Concepts/hazards/starvation/README.md) · [Semaphore](../../11_Concepts/synchronization/semaphore/README.md)
