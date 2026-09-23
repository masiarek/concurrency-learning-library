# What does a wait return when the time runs out?

**Level:** 201 · anyone who has been told never to wait without a timeout

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A wait with a timeout has three outcomes, not two — the condition became true, the time ran out, and the time ran out *just as* the condition became true — and each language reports the third one differently, which is where a timed wait silently drops a result.

## The question

Wait up to one second for an item. Nothing comes: a timeout, clearly. An item comes at 0.5 s: got it. An item is pushed at 0.9999 s while the wait is deciding it timed out: what does the caller get — the item, or a timeout with an item in the queue? The page shows the three cases with a two-second margin between the first two and forces the third, then reads what each language's return value says.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `Condvar::wait_timeout` returns the guard *and* a `WaitTimeoutResult`, so the caller re-checks the condition either way |
| Go | `select` on the channel and `time.After`; if both are ready the choice is random |
| C | `pthread_cond_timedwait` returns `ETIMEDOUT`, and the condition must still be checked under the mutex |
| C++ | `wait_for` returns `std::cv_status`, or the predicate's value with the predicate overload |
| Java | `Condition.await(time, unit)` returns `false` on timeout; `BlockingQueue.poll(time, unit)` returns `null` |
| Python | `Condition.wait_for(pred, timeout)` returns the predicate's last value; `Queue.get(timeout=)` raises `Empty` |

## What the programs have to show

- the three cases per language, with the item pushed at 3 s against a 1 s wait and vice versa
- the forced simultaneous case: what the return value says, and whether the item is still in the queue
- the *Real runs* fence of how late a 1 s timed wait returns

## See also

- Before this: [Why do five philosophers with five forks starve?](../the_dining_philosophers/README.md)
- [What happens to the work when an await times out?](../../06_Async/a_timeout_on_an_await/README.md)
- [How does a thread wait for something to become true?](../waiting_for_a_condition/README.md)
- The Go library's [A timeout is a channel ↗](https://masiarek.github.io/go-learning-library/03_Select/a_timeout_is_a_channel/index.html)
- Concepts: [Timeout](../../11_Concepts/async/timeout/README.md) · [Condition variable](../../11_Concepts/synchronization/condition_variable/README.md) · [Select](../../11_Concepts/communication/select/README.md) · [Race condition](../../11_Concepts/hazards/race_condition/README.md)
