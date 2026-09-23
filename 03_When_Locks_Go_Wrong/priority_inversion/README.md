# How does a low-priority thread block a high-priority one?

**Level:** 201 · anyone who has heard the Mars Pathfinder story

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A high-priority thread waiting for a lock held by a low-priority thread waits for however long a *medium*-priority thread keeps the low one off the CPU — priority inversion — and the fix is for the lock to lend the waiter's priority to its holder, which POSIX offers as `PTHREAD_PRIO_INHERIT` and the other languages do not offer at all.

## The question

Three threads at three priorities. Low takes a lock. High wants it and blocks. Medium, needing no lock, runs for a second — and Low, preempted by Medium, cannot release the lock High is waiting for. High, the most important thread, waits behind the least important one's work. The page needs real priorities, so most of it is a *Real runs* fence on Linux with `SCHED_FIFO`; the CI example is the shape without the scheduling.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | no thread priorities in std; the shape can be shown, the inversion only through `libc` |
| Go | no goroutine priorities at all: the runtime's scheduler is the only one |
| C | `pthread_setschedparam` with `SCHED_FIFO` and a `PTHREAD_PRIO_INHERIT` mutex — the one place the fix exists |
| C++ | `std::thread::native_handle` to reach the same pthread calls |
| Java | `Thread.setPriority` is a hint the JVM may ignore; no inheritance |
| Python | no thread priorities |

## What the programs have to show

- a `demo/` script needing root or `CAP_SYS_NICE` in a container: how long High waits with a plain mutex and with priority inheritance
- the CI example: the three threads and the lock, printing the order of completion without real-time priorities
- the link to the Pathfinder account, which is the reason the concept has a name

## See also

- Before this: [Can a thread wait forever for a lock that is always free eventually?](../starvation_and_fairness/README.md)
- After this: [What does a spinlock cost when there is nowhere to spin?](../a_spinlock_on_one_core/README.md)
- [Can a thread wait forever for a lock that is always free eventually?](../starvation_and_fairness/README.md)
- Concepts: [Priority inversion](../../11_Concepts/hazards/priority_inversion/README.md) · [Scheduling policy](../../11_Concepts/scheduling/scheduling_policy/README.md) · [Real-time system](../../11_Concepts/real_time/real_time_system/README.md) · [Mutex](../../11_Concepts/synchronization/mutex/README.md) · [Preemptive scheduling](../../11_Concepts/scheduling/preemptive_scheduling/README.md)
