# What does a sleep promise, and what does a yield?

**Level:** 201 · anyone who has used a sleep to make a test pass

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A sleep promises to wait *at least* as long as asked and says nothing about the other threads; a yield promises even less — that the scheduler was offered a chance — and neither is a synchronizer, which is why every lesson in this library that sleeps does so only as a margin around something it has already ordered another way.

## The question

`sleep(10ms)` and then read a value another thread was supposed to write: it works on the laptop and fails on CI. Why? Because the sleep orders nothing. This page measures what a sleep actually does — how late it can wake, and whether it releases anything — and what a yield does on a machine with idle cores, where it usually returns at once. It is the reason for the *Deterministic about nondeterminism* rule this library is written under.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `thread::sleep` sleeps at least the duration; `thread::yield_now` is a hint |
| Go | `time.Sleep`; `runtime.Gosched` yields the processor to another goroutine |
| C | `nanosleep` may return early only on a signal, reporting the remainder; `sched_yield` |
| C++ | `std::this_thread::sleep_for` and `yield` |
| Java | `Thread.sleep` (may throw `InterruptedException`); `Thread.onSpinWait` and `Thread.yield` |
| Python | `time.sleep` releases the GIL; there is no yield except a zero-length sleep |

## What the programs have to show

- a *Real runs* fence of how late a 1 ms sleep wakes, a hundred times, on the Mac and in a container
- the racy test: sleep 1 ms then read — passing on the recording machine and marked as the anti-pattern
- the same test with a join or a channel, which is the CI example

## See also

- Before this: [What is a goroutine, if not a thread?](../a_goroutine_is_not_a_thread/README.md)
- [How does a test wait an hour in a millisecond?](../../09_Testing_and_Tools/virtual_time_in_tests/README.md)
- The Go library's [`synctest.Wait` instead of a sleep ↗](https://masiarek.github.io/go-learning-library/07_Testing_Concurrent_Code/synctest_wait/index.html)
- Concepts: [Scheduler](../../11_Concepts/scheduling/scheduler/README.md) · [Preemptive scheduling](../../11_Concepts/scheduling/preemptive_scheduling/README.md) · [Busy waiting](../../11_Concepts/scheduling/busy_waiting/README.md) · [Nondeterminism](../../11_Concepts/foundations/nondeterminism/README.md) · [Polling](../../11_Concepts/scheduling/polling/README.md)
