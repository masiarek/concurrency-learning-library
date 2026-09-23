# What does a spinlock cost when there is nowhere to spin?

**Level:** 201 · anyone who wrote a busy-wait loop

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A spinlock burns a core while it waits, which is cheaper than a sleep when the wait is a few hundred nanoseconds and ruinous when it is not — and on a single core it is always ruinous, because the thread spinning is the thread stopping the holder from running.

## The question

A spinlock is an atomic flag and a loop: `while flag.swap(true) {}`. It avoids the system call a mutex makes. It also keeps a core busy doing nothing. The page builds one in each language that has the atomics for it, measures it against the mutex under short and long critical sections, and then pins the program to one core — where the spinner and the holder fight for the same CPU and the lock takes a thousand times longer.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `AtomicBool` with `compare_exchange` and `spin_loop`; `std::sync::Mutex` uses a futex and sleeps instead |
| Go | `atomic.Bool` in a loop; the runtime may not preempt the spinner promptly |
| C | `atomic_flag_test_and_set` in a loop against `pthread_mutex_t`; `pthread_spin_lock` on Linux |
| C++ | `std::atomic_flag` against `std::mutex` |
| Java | `AtomicBoolean.compareAndSet` in a loop with `Thread.onSpinWait()` |
| Python | an atomic loop is not possible under the GIL; a `Lock` is the only answer |

## What the programs have to show

- *Real runs*: a million short critical sections under a spinlock and under a mutex, on all cores and pinned to one (`taskset`)
- the CI example: both locks, correct counts, no timing
- a *Real runs* fence of CPU time consumed while waiting

## See also

- Before this: [How does a low-priority thread block a high-priority one?](../priority_inversion/README.md)
- After this: [How do you find out where a deadlocked program is stuck?](../detecting_a_deadlock/README.md)
- [Can a thread wait forever for a lock that is always free eventually?](../starvation_and_fairness/README.md)
- [What does a sleep promise, and what does a yield?](../../01_Threads/sleep_and_yield/README.md)
- Concepts: [Spinlock](../../11_Concepts/synchronization/spinlock/README.md) · [Busy waiting](../../11_Concepts/scheduling/busy_waiting/README.md) · [Futex](../../11_Concepts/synchronization/futex/README.md) · [Mutex](../../11_Concepts/synchronization/mutex/README.md) · [Context switch](../../11_Concepts/units_of_execution/context_switch/README.md)
