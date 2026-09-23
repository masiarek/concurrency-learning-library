# How many threads can you start?

**Level:** 201 · anyone who was told goroutines are cheap and wants a number

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** An operating-system thread costs a stack — megabytes reserved, kilobytes touched — and a machine runs out somewhere in the tens of thousands; goroutines and virtual threads start with a few kilobytes on the heap and run into the millions, which is a difference in kind, and every count on this page is a *Real runs* fence because the limits are the machine's.

## The question

Every language here can start a thread. How many can it start before something gives — `pthread_create` returning `EAGAIN`, the JVM throwing `OutOfMemoryError: unable to create native thread`, the process being killed? And how do Go's goroutines and Java's virtual threads, which are not operating-system threads, compare on the same machine? The number itself is not the lesson; the order of magnitude is, and so is what the failure looks like when it comes.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | OS threads with a 2 MiB default stack; the count before `thread::spawn` returns `Err` is the machine's, in the tens of thousands |
| Go | goroutines start with a 2 KiB stack on the heap and grow; a million is routine |
| C | `pthread_create` fails with `EAGAIN` at the process or system limit (`ulimit -u`, `RLIMIT_NPROC`) |
| C++ | `std::thread` throws `std::system_error` at the same limit as C |
| Java | platform threads fail with `OutOfMemoryError`; virtual threads (Java 21) are heap objects and go far higher |
| Python | `threading.Thread` is an OS thread and fails with `RuntimeError: can't start new thread` |

## What the programs have to show

- a `demo/` script per language that starts threads that each block until released, counting until the first failure, as a *Real runs* fence with the machine and its limits
- the same for goroutines and virtual threads, on the same machine, the same day
- the CI example is the small case: a thousand of each, all joined, printing only the count

## See also

- Before this: [What does a failure on a thread do when nobody is waiting for it?](../a_failure_nobody_is_waiting_for/README.md)
- After this: [Is a thread-local variable really one per thread?](../a_variable_per_thread/README.md)
- [Who waits when main returns?](../who_waits_when_main_returns/README.md)
- The Go library's [Goroutines are cheap ↗](https://masiarek.github.io/go-learning-library/01_Goroutines/goroutines_are_cheap/index.html)
- Concepts: [Thread](../../11_Concepts/units_of_execution/thread/README.md) · [Goroutine](../../11_Concepts/units_of_execution/goroutine/README.md) · [Virtual thread](../../11_Concepts/units_of_execution/virtual_thread/README.md) · [Green threads and M:N scheduling](../../11_Concepts/units_of_execution/green_thread/README.md) · [Thread pool and executor](../../11_Concepts/units_of_execution/thread_pool/README.md) · [Oversubscription](../../11_Concepts/foundations/oversubscription/README.md)
