# How do you find out where a deadlocked program is stuck?

**Level:** 201 · anyone staring at a process that is alive and doing nothing

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A deadlocked program is alive, consumes no CPU and prints nothing, and each runtime offers a different way to ask it where every thread is: Go prints it unasked if every goroutine is stuck, Java answers `jstack` with the cycle named, and C, C++, Rust and Python answer only a debugger — and then only if you know to attach one.

## The question

The transfer program from [the first lesson](../two_locks_in_different_orders/README.md) is hanging in production. Which lock is each thread waiting for, and who holds it? The page takes the same deadlock and asks each runtime: `SIGQUIT` to a Go program, `jstack` to a Java one, `gdb -p` or `lldb` to the rest, and `faulthandler` in Python. Every answer is a *Real runs* fence, since it is a stack trace.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `gdb`/`lldb` `thread apply all bt`; no built-in report |
| Go | `SIGQUIT` dumps every goroutine's stack; a total deadlock is reported without asking |
| C | `gdb` with `thread apply all bt`; an `ERRORCHECK` mutex only catches the self-deadlock |
| C++ | the same as C |
| Java | `jstack <pid>` names the deadlocked threads and the monitors, and `ThreadMXBean.findDeadlockedThreads()` does it from inside |
| Python | `faulthandler.dump_traceback` on a signal, or `py-spy dump` from outside |

## What the programs have to show

- the deadlock sent each runtime's signal or tool, with the output abridged to the two waiting threads
- Java's in-process detection, which *is* a CI example: the thread ids and the lock names
- Go's report, which is a CI example when the deadlock is total

## See also

- Before this: [What does a spinlock cost when there is nowhere to spin?](../a_spinlock_on_one_core/README.md)
- [Why do two locks taken in different orders hang?](../two_locks_in_different_orders/README.md)
- [How do you read a thread dump?](../../09_Testing_and_Tools/reading_a_thread_dump/README.md)
- The Go library's [All goroutines are asleep ↗](https://masiarek.github.io/go-learning-library/02_Channels/all_goroutines_are_asleep/index.html)
- The Rust library's [Diagnosing a stuck runtime ↗](https://masiarek.github.io/rust-learning-library/35_Async/building_minidb/diagnosing_a_stuck_runtime/index.html)
- Concepts: [Deadlock](../../11_Concepts/hazards/deadlock/README.md) · [Debugging concurrent programs](../../11_Concepts/testing_and_tools/concurrency_debugging/README.md) · [Liveness failure](../../11_Concepts/hazards/liveness_failure/README.md)
