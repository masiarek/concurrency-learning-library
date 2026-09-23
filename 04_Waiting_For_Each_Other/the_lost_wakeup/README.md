# What happens when the signal comes before the wait?

**Level:** 201 · anyone whose consumer slept through the one item it was waiting for

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A signal on a condition variable wakes whoever is waiting *now* and is otherwise dropped, so a producer that signals a moment before the consumer waits leaves the consumer asleep forever with a full queue in front of it — which is why the condition is checked under the lock before waiting, and why the lock is held across the signal.

## The question

Consumer: check the queue, empty, wait. Producer: push, signal. Interleave them as *check, push, signal, wait* and the signal finds nobody; the consumer then waits for a signal that has already happened. The page forces that order with a barrier between the consumer's check and its wait, shows the hang under a timeout, and then shows why holding the mutex across the check-and-wait makes the order impossible.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `Condvar` with the check outside the lock: hangs; `wait_while` under the guard: cannot |
| Go | `sync.Cond` with `L.Lock()` released between check and `Wait`: hangs |
| C | `pthread_cond_signal` with no waiter is a no-op by specification |
| C++ | `std::condition_variable::notify_one` with no waiter does nothing |
| Java | `notify()` with no waiter does nothing; the check must be inside `synchronized` |
| Python | `Condition.notify()` with no waiter does nothing |

## What the programs have to show

- the forced lost wakeup per language, killed by a timeout driver
- the correct version, where the lock spans the check and the wait, and the item arrives
- a Go channel doing the same job without the hazard, since a buffered send is not dropped

## See also

- Before this: [How does a thread wait for something to become true?](../waiting_for_a_condition/README.md)
- After this: [What does a semaphore count?](../a_semaphore_counts_permits/README.md)
- [How does a thread wait for something to become true?](../waiting_for_a_condition/README.md)
- [Does a send return before anyone receives?](../../05_Message_Passing/an_unbuffered_send_waits/README.md)
- Concepts: [Condition variable](../../11_Concepts/synchronization/condition_variable/README.md) · [Race condition](../../11_Concepts/hazards/race_condition/README.md) · [Liveness failure](../../11_Concepts/hazards/liveness_failure/README.md) · [Mutex](../../11_Concepts/synchronization/mutex/README.md)
