# How does a thread wait for something to become true?

**Level:** 201 · anyone who polled a flag in a loop

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A condition variable lets a thread sleep until another thread signals that something may have changed, and the word *may* is the whole lesson: the wait can return without a signal, so it is always written inside a loop that re-checks the condition under the lock, and every language here either forces that loop or trusts you to write it.

## The question

A consumer needs an item that a producer has not made yet. It can spin on `queue.empty()`, burning a core, or sleep and poll, adding latency, or wait on a condition variable and be woken. The page writes the third one in each language, then removes the `while` loop around the wait to show the spurious wakeup and the stolen wakeup that the loop exists for.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `Condvar::wait` returns the guard; `wait_while` takes the loop's predicate and is the idiom |
| Go | `sync.Cond.Wait` must be inside a `for !cond {}` loop; `Broadcast` and `Signal` |
| C | `pthread_cond_wait` in a `while` loop, with the mutex held; spurious wakeups are permitted by POSIX |
| C++ | `std::condition_variable::wait` with a predicate overload that loops for you |
| Java | `Object.wait` in a `while` loop, or `Condition.await`; the JLS says spurious wakeups may occur |
| Python | `threading.Condition.wait_for(predicate)` loops for you |

## What the programs have to show

- producer and consumer through a condition variable: the items received, in order
- the wait without its loop, under a forced early signal: the consumer proceeds with an empty queue
- the predicate forms that make the loop impossible to forget

## See also

- After this: [What happens when the signal comes before the wait?](../the_lost_wakeup/README.md)
- [What happens when the signal comes before the wait?](../the_lost_wakeup/README.md)
- [How does a producer wait for room and a consumer wait for an item?](../the_bounded_buffer/README.md)
- Concepts: [Condition variable](../../11_Concepts/synchronization/condition_variable/README.md) · [Monitor](../../11_Concepts/synchronization/monitor/README.md) · [Synchronization](../../11_Concepts/synchronization/synchronization/README.md) · [Producer-consumer](../../11_Concepts/communication/producer_consumer/README.md) · [Busy waiting](../../11_Concepts/scheduling/busy_waiting/README.md)
