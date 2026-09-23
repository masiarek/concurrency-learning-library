# What happens to a task that is started and never awaited?

**Level:** 201 · anyone who has seen "Task was destroyed but it is pending"

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A task started and never awaited is either running with nobody to notice its failure, or waiting forever on something that will never come, and neither is reported by default — which is why structured concurrency ties every task to a scope that must await it, and why the Go library's leaked goroutine and Rust's `JoinHandle` warnings exist.

## The question

Spawn a task that fails, and never await it. Where does the failure go? Then spawn a task that waits on a channel nobody will send on, and let the program end. Does anyone say anything? The page runs both in each language, records what was printed and the exit status, and then puts the same tasks inside a structured scope, where the failure surfaces and the leak is impossible.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | an unawaited `JoinHandle`'s panic is silent; `tokio` prints nothing either; `thread::scope` surfaces it (link for tokio) |
| Go | a goroutine blocked forever is a leak nobody reports; `goleak` finds it in tests (link, not run) |
| C | a thread blocked on a pipe when `main` returns simply dies with the process |
| C++ | an unjoined `std::thread` terminates the program; a detached one is silent |
| Java | an `ExecutorService` task's exception is stored in the `Future` and lost if never `get`; a structured `StructuredTaskScope` rethrows |
| Python | `asyncio` logs "Task exception was never retrieved" at garbage collection, and "Task was destroyed but it is pending" |

## What the programs have to show

- the failing unawaited task per language: what was printed, if anything, and when
- the blocked task at program exit: silent, or the warning
- both inside a structured scope: the failure reaches the caller

## See also

- Before this: [Why can't a normal function call an async one?](../function_coloring/README.md)
- After this: [How does a loop await a sequence of values that arrive over time?](../an_async_stream/README.md)
- [What does a failure on a thread do when nobody is waiting for it?](../../01_Threads/a_failure_nobody_is_waiting_for/README.md)
- [How is a running task told to stop, and does it?](../cancelling_an_async_task/README.md)
- The Go library's [A leaked goroutine never ends ↗](https://masiarek.github.io/go-learning-library/05_Context/a_leaked_goroutine_never_ends/index.html)
- The Rust library's [Tasks ↗](https://masiarek.github.io/rust-learning-library/35_Async/building_minidb/tasks/index.html)
- The Rust library's [Shutdown and supervision ↗](https://masiarek.github.io/rust-learning-library/35_Async/building_minidb/shutdown_and_supervision/index.html)
- Concepts: [Leaked tasks](../../11_Concepts/hazards/task_leak/README.md) · [Structured concurrency](../../11_Concepts/async/structured_concurrency/README.md) · [Join](../../11_Concepts/async/join/README.md) · [Safety failure](../../11_Concepts/hazards/safety_failure/README.md) · [Supervision](../../11_Concepts/communication/supervision/README.md)
