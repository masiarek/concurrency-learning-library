# What does a semaphore count?

**Level:** 201 · anyone who needs at most N of something at once

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A semaphore is a counter that blocks when it reaches zero — N permits for N concurrent users of a pool, a connection limit, a disk — and unlike a mutex it has no owner, so any thread may release what another acquired, which is both its use and its hazard.

## The question

Ten workers, three database connections. A mutex allows one; a semaphore initialized to three allows three. The page runs ten workers through a semaphore of three, records that no more than three were ever inside at once, and then does what a mutex would forbid: releases from a thread that did not acquire, which is how a semaphore signals *an event happened* rather than *I am done with the resource*.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | no semaphore in std; a `Mutex<usize>` plus `Condvar`, or `tokio::sync::Semaphore` (link, not run) |
| Go | a buffered channel of capacity N: send to acquire, receive to release; `golang.org/x/sync/semaphore` is weighted |
| C | `sem_init`/`sem_wait`/`sem_post` from POSIX; unnamed on macOS is deprecated, so `sem_open` |
| C++ | `std::counting_semaphore<N>` (C++20) and `binary_semaphore` |
| Java | `java.util.concurrent.Semaphore(n)` with an optional fairness flag |
| Python | `threading.Semaphore(n)` and `BoundedSemaphore`, which refuses to be released past its initial count |

## What the programs have to show

- ten workers, three permits: the peak concurrency observed, three, and every worker finished
- release from a different thread than acquired: allowed, and what it is for
- `BoundedSemaphore` raising on the extra release, the one language that checks

## See also

- Before this: [What happens when the signal comes before the wait?](../the_lost_wakeup/README.md)
- After this: [How do N threads wait for each other?](../a_barrier_and_a_latch/README.md)
- [How do N threads wait for each other?](../a_barrier_and_a_latch/README.md)
- [What stops a fast producer from filling memory?](../../05_Message_Passing/a_bounded_queue_pushes_back/README.md)
- The Go library's [A buffered channel as a semaphore ↗](https://masiarek.github.io/go-learning-library/06_Patterns/a_buffered_channel_as_a_semaphore/index.html)
- Concepts: [Semaphore](../../11_Concepts/synchronization/semaphore/README.md) · [Synchronization](../../11_Concepts/synchronization/synchronization/README.md) · [Buffered and bounded channels](../../11_Concepts/communication/bounded_channel/README.md) · [Mutex](../../11_Concepts/synchronization/mutex/README.md)
