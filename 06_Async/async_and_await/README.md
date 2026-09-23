# What happens at an `await`?

**Level:** 201 · anyone who reads `await` as "wait here"

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** `await` is the point where an async function may stop and hand its thread back to the loop, keeping its locals inside the future for when it resumes — possibly on another thread, possibly never — and a function with no `await` in it never yields at all, however long it runs.

## The question

Two async functions on one loop, each printing before and after an `await` on a sleep. The prints interleave: A-before, B-before, A-after, B-after. Remove the `await` — replace the async sleep with a blocking one — and they no longer do: A runs to completion first. The page shows both orders, then measures the thing that makes the state machine real: the size of a future grows with what it holds across the `await`.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `async fn` returns an `impl Future`; the page measures `size_of_val` growing by a 1 KiB array held across an `.await` |
| Go | no `await`: a goroutine simply blocks, and the runtime moves on; the page's Go column is the contrast |
| C | no async functions; a state machine written by hand with an `enum` for the state |
| C++ | `co_await` in a C++20 coroutine; the frame is heap-allocated by default |
| Java | no `async`/`await` keywords; a virtual thread blocks where other languages await |
| Python | `await` inside `async def`; `asyncio.sleep(0)` yields, `time.sleep(1)` does not |

## What the programs have to show

- the interleaved order with an async sleep and the serial order with a blocking one, per language
- Rust's future size with and without the array across the `.await`
- the C column's hand-written state machine doing what the compiler does

## See also

- Before this: [What is a future before it has a value?](../a_future_is_a_value_not_yet_there/README.md)
- After this: [What does one blocking call do to every other task?](../blocking_the_event_loop/README.md)
- [What is a future before it has a value?](../a_future_is_a_value_not_yet_there/README.md)
- [What does one blocking call do to every other task?](../blocking_the_event_loop/README.md)
- The Rust library's [`async fn` and `.await` ↗](https://masiarek.github.io/rust-learning-library/35_Async/async_fn_and_await/index.html)
- The Rust library's [What a future is ↗](https://masiarek.github.io/rust-learning-library/35_Async/what_a_future_is/index.html)
- Concepts: [Async and await](../../11_Concepts/async/async_await/README.md) · [Suspension point](../../11_Concepts/scheduling/suspension_point/README.md) · [Async functions as state machines](../../11_Concepts/async/async_state_machine/README.md) · [Function coloring](../../11_Concepts/async/function_coloring/README.md) · [Coroutine](../../11_Concepts/units_of_execution/coroutine/README.md)
