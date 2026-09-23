# Why can't a normal function call an async one?

**Level:** 201 · anyone who added `async` to one function and had to add it to ten

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** An async function can only be awaited from another async function, so `async` spreads upward through every caller until it reaches something that owns a loop — the *coloring* problem — and Go and Java's virtual threads are the two designs here that have no colors, because every function may block and the runtime handles it.

## The question

A synchronous function three levels up needs a value that only an async function produces. It cannot `await`. It can block on the loop — which deadlocks if it is already on the loop — or become async itself, and so must its callers. The page shows the deadlock, the spread, and the two escape hatches each language offers, then the Go and Java columns where the question does not arise.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | a sync fn cannot `.await`; `block_on` from inside a runtime panics; the page shows both messages (link for `tokio`; std column with a channel) |
| Go | no colors: `f()` blocks in a goroutine and nothing changes upstream |
| C | no colors and no async; every call is a blocking call |
| C++ | a coroutine can only be `co_await`ed from a coroutine; same spread |
| Java | no colors on a virtual thread; `CompletableFuture.join()` is the blocking escape |
| Python | `asyncio.run` inside a running loop raises `RuntimeError`; `nest_asyncio` and `run_coroutine_threadsafe` are the escapes |

## What the programs have to show

- the sync caller that blocks on the loop from inside it: the panic or `RuntimeError` text as a key
- the spread: the three functions made async, and the one at the top that runs the loop
- Go and Java doing the same call chain with no change

## See also

- Before this: [What happens to the work when an await times out?](../a_timeout_on_an_await/README.md)
- After this: [What happens to a task that is started and never awaited?](../a_task_nobody_awaits/README.md)
- [What happens at an `await`?](../async_and_await/README.md)
- [What is a goroutine, if not a thread?](../../01_Threads/a_goroutine_is_not_a_thread/README.md)
- The Rust library's [Common async pitfalls ↗](https://masiarek.github.io/rust-learning-library/35_Async/common_async_pitfalls/index.html)
- The Rust library's [`async fn` and `.await` ↗](https://masiarek.github.io/rust-learning-library/35_Async/async_fn_and_await/index.html)
- Concepts: [Function coloring](../../11_Concepts/async/function_coloring/README.md) · [Async and await](../../11_Concepts/async/async_await/README.md) · [Virtual thread](../../11_Concepts/units_of_execution/virtual_thread/README.md) · [Blocking the event loop](../../11_Concepts/async/blocking_the_event_loop/README.md)
