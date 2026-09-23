# How is a running task told to stop, and does it?

**Level:** 201 · anyone whose request timed out but kept running

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** No language here can stop a task from outside without its cooperation, and they split on where the cooperation lives: in Rust dropping the future *is* the cancellation and the task cannot refuse, in Go and C the task must check a context or a flag, in Java and Python cancellation is an exception delivered at the next blocking point that the task may catch — and a task in the middle of writing a file is left in whatever state it was in.

## The question

A task that writes ten lines, one per second. Cancel it after 3.5 seconds. How many lines were written, and did the task get to run its cleanup? The page runs it in each language and records the line count and whether the `finally` ran — and then shows a task that ignores cancellation, which is possible everywhere except Rust, where it is not.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | dropping the `JoinHandle` does not cancel; `abort()` does, and the future is dropped at its next `.await`, running destructors but no `finally` |
| Go | `context.WithCancel`; the goroutine must select on `ctx.Done()` or it runs to the end |
| C | `pthread_cancel` with cancellation points, or an atomic flag the thread checks |
| C++ | `std::stop_token` from `std::jthread::request_stop`, checked by the thread |
| Java | `Thread.interrupt` sets a flag and throws `InterruptedException` in blocking calls; `Future.cancel(true)` uses it |
| Python | `Task.cancel()` throws `CancelledError` at the next `await`; a `finally` runs; a task may catch it |

## What the programs have to show

- cancel at 3.5 s: lines written (3 or 4), and whether cleanup ran, per language
- the task that refuses: runs to ten everywhere but Rust
- Go's context cancelling a tree of goroutines with one call

## See also

- Before this: [Where does a callback keep its state?](../a_callback_and_its_state/README.md)
- After this: [What happens to the work when an await times out?](../a_timeout_on_an_await/README.md)
- [What happens to the work when an await times out?](../a_timeout_on_an_await/README.md)
- [What happens to a task that is started and never awaited?](../a_task_nobody_awaits/README.md)
- The Rust library's [Cancellation ↗](https://masiarek.github.io/rust-learning-library/35_Async/building_minidb/cancellation/index.html)
- The Go library's [One `cancel` reaches every goroutine ↗](https://masiarek.github.io/go-learning-library/05_Context/cancel_reaches_every_goroutine/index.html)
- The Go library's [Cancel with a cause ↗](https://masiarek.github.io/go-learning-library/05_Context/cancel_with_a_cause/index.html)
- Concepts: [Cancellation](../../11_Concepts/async/cancellation/README.md) · [Structured concurrency](../../11_Concepts/async/structured_concurrency/README.md) · [Timeout](../../11_Concepts/async/timeout/README.md) · [Suspension point](../../11_Concepts/scheduling/suspension_point/README.md) · [Leaked tasks](../../11_Concepts/hazards/task_leak/README.md)
