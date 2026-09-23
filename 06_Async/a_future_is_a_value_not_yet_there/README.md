# What is a future before it has a value?

**Level:** 201 · anyone holding a `Future` and wondering what it is doing

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A future is a handle to a value that will exist later, and the languages disagree about whether holding one means the work is *running*: a Java `CompletableFuture` or a Go channel is fed by work already underway, while a Rust future does nothing at all until something polls it — so dropping a Rust future cancels work that, in every other language, would have continued.

## The question

Create a future for a computation that prints as it runs. Do not await it. Wait two seconds. Did it print? In Java, yes: the executor was already running it. In Python's `asyncio`, a coroutine object prints nothing until awaited, and a `Task` prints because `create_task` scheduled it. In Rust, nothing prints, and the compiler warns that the future is unused. The page runs that experiment, then awaits each and shows the value arrive.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | an `async` block is inert: `#[must_use]` warning, and nothing runs until `.await` or `spawn` |
| Go | no future type; a goroutine plus a channel is already running when created |
| C | no futures; a thread and a pipe, running |
| C++ | `std::async` with `std::launch::async` runs at once; `std::launch::deferred` runs on `get()` |
| Java | `CompletableFuture.supplyAsync` runs at once on the common pool; `get` waits |
| Python | a coroutine object is inert; `asyncio.create_task` schedules it; `concurrent.futures.Future` is fed by a running executor |

## What the programs have to show

- the unawaited future in each language: printed, or silent, after two seconds
- the Rust `#[must_use]` warning text as a `.sh` driver key
- each future awaited: the value, and for C++ the `deferred` one running only then

## See also

- Before this: [What does an event loop do all day?](../what_an_event_loop_does/README.md)
- After this: [What happens at an `await`?](../async_and_await/README.md)
- [What happens at an `await`?](../async_and_await/README.md)
- [What happens to a task that is started and never awaited?](../a_task_nobody_awaits/README.md)
- The Rust library's [What a future is ↗](https://masiarek.github.io/rust-learning-library/35_Async/what_a_future_is/index.html)
- The Rust library's [Tasks ↗](https://masiarek.github.io/rust-learning-library/35_Async/building_minidb/tasks/index.html)
- Concepts: [Future and promise](../../11_Concepts/async/future_and_promise/README.md) · [Task (async)](../../11_Concepts/units_of_execution/async_task/README.md) · [Asynchrony](../../11_Concepts/foundations/asynchrony/README.md) · [Callback](../../11_Concepts/async/callback/README.md)
