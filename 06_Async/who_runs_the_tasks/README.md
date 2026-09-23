# Who runs an async task, and on how many threads?

**Level:** 201 · anyone who assumed async meant single-threaded

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** An async runtime decides how many threads run the tasks — one in `asyncio` and Node, as many as there are cores in `tokio`'s default and Go's — and the difference is not performance but the rules: on a multi-threaded runtime a task may resume on a different thread than it left, so everything it holds across an `await` must be safe to move.

## The question

Ten tasks each record the thread they are on before and after an `await`. On a single-threaded loop, every task sees one thread. On a multi-threaded runtime, a task may see two different ones. The page prints the count of distinct threads observed, per runtime, and then shows what that means: a value that is not thread-safe held across the `await`, which Rust rejects at compile time and the others run.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `tokio`'s multi-thread runtime moves tasks; a `Rc` across an `.await` is `error: future cannot be sent between threads safely` (link for tokio; the std column's message is the key) |
| Go | goroutines move between threads freely; `runtime.LockOSThread` pins one |
| C | the hand-written loop is one thread |
| C++ | the same; `std::async` chooses |
| Java | virtual threads move between carrier threads; a `ThreadLocal` follows the virtual thread |
| Python | `asyncio` is one thread; `loop.run_in_executor` is the only way work leaves it |

## What the programs have to show

- ten tasks reporting their thread before and after an await: one thread or several, per runtime
- the Rust compile error for a non-`Send` value held across an await, as a `.sh` driver key
- a *Real runs* fence of a CPU-bound batch on one thread and on N

## See also

- Before this: [How does a loop await a sequence of values that arrive over time?](../an_async_stream/README.md)
- After this: [How does one thread watch a thousand sockets?](../io_multiplexing_under_the_loop/README.md)
- [What does an event loop do all day?](../what_an_event_loop_does/README.md)
- [What may be handed to another thread?](../../02_Shared_State/what_may_cross_a_thread_boundary/README.md)
- The Rust library's [The Tokio runtime ↗](https://masiarek.github.io/rust-learning-library/35_Async/building_minidb/the_tokio_runtime/index.html)
- The Rust library's [Common async pitfalls ↗](https://masiarek.github.io/rust-learning-library/35_Async/common_async_pitfalls/index.html)
- Concepts: [Async runtime (executor and reactor)](../../11_Concepts/scheduling/async_runtime/README.md) · [Scheduler](../../11_Concepts/scheduling/scheduler/README.md) · [Work stealing](../../11_Concepts/scheduling/work_stealing/README.md) · [Send and Sync](../../11_Concepts/safety_in_languages/send_and_sync/README.md) · [Event loop](../../11_Concepts/scheduling/event_loop/README.md)
