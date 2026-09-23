# What happens to the work when an await times out?

**Level:** 201 · anyone who wrapped a call in a timeout and assumed that ended it

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A timeout around an await gives the caller back control after the deadline, and whether it stops the work underneath depends entirely on the language: Rust drops the future and the work stops, Python cancels the task, Go returns a context error the work must notice, and Java's `get(timeout)` returns and leaves the work running.

## The question

Await a five-second operation with a one-second timeout. The caller gets a timeout error at one second — in every language. Now: is the operation still running at two seconds? The page prints from inside the operation at each second and shows which languages' prints continue after the timeout fired.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `tokio::time::timeout` drops the inner future: no more prints (link, not run); the page's std column builds the same with a thread and `recv_timeout`, where the thread continues |
| Go | `context.WithTimeout`; the work continues unless it checks `ctx.Err()` |
| C | `pthread_cond_timedwait` returns; the worker thread continues |
| C++ | `std::future::wait_for` returns `timeout`; the async work continues |
| Java | `future.get(1, SECONDS)` throws `TimeoutException`; the task keeps running unless `cancel`led |
| Python | `asyncio.wait_for` cancels the inner task: no more prints |

## What the programs have to show

- the five-second operation under a one-second timeout: the prints after the timeout, per language
- the explicit cancel after the timeout, where one is needed
- the *Real runs* fence of how late the timeout itself fires

## See also

- Before this: [How is a running task told to stop, and does it?](../cancelling_an_async_task/README.md)
- After this: [Why can't a normal function call an async one?](../function_coloring/README.md)
- [How is a running task told to stop, and does it?](../cancelling_an_async_task/README.md)
- [What does a wait return when the time runs out?](../../04_Waiting_For_Each_Other/waiting_with_a_timeout/README.md)
- The Go library's [A deadline is a cancel with a clock ↗](https://masiarek.github.io/go-learning-library/05_Context/a_deadline_is_a_cancel_with_a_clock/index.html)
- The Go library's [A timeout is a channel ↗](https://masiarek.github.io/go-learning-library/03_Select/a_timeout_is_a_channel/index.html)
- The Rust library's [Cancellation ↗](https://masiarek.github.io/rust-learning-library/35_Async/building_minidb/cancellation/index.html)
- Concepts: [Timeout](../../11_Concepts/async/timeout/README.md) · [Cancellation](../../11_Concepts/async/cancellation/README.md) · [Timers and tickers](../../11_Concepts/async/timers/README.md) · [Future and promise](../../11_Concepts/async/future_and_promise/README.md)
