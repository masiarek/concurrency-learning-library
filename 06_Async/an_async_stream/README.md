# How does a loop await a sequence of values that arrive over time?

**Level:** 201 · anyone who wants `for` over a channel in async code

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** An async stream is an iterator whose `next` is awaited — the values arrive over time and the loop yields between them — and it is where the languages' async designs are furthest apart: Python has `async for`, Rust has a `Stream` trait outside the standard library, Go has a channel and needs nothing else, and Java has `Flow.Publisher` with request-N backpressure.

## The question

A source produces a value every 100 ms, ten times. A consumer loops over them, awaiting each. The page writes the source and the loop in each language and confirms the ten values arrived in order, then asks the stream's two hard questions: what happens when the consumer is slower than the source, and how the loop ends.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | no `Stream` in std; `futures::Stream` and `while let Some(x) = s.next().await` (link, not run); the std column uses a channel on a thread |
| Go | `for x := range ch` over a channel fed by a goroutine |
| C | a `read` loop on a pipe |
| C++ | a C++20 generator-style coroutine, hand-rolled promise type; `std::generator` is C++23 |
| Java | `Flow.Publisher` and a `Subscriber` calling `request(1)` |
| Python | `async for x in agen()` over an `async def` with `yield` |

## What the programs have to show

- ten values at 100 ms intervals, received in order
- the slow consumer: the source waits (backpressure) or runs ahead, per design
- the end: the generator returning, the channel closing, `onComplete`

## See also

- Before this: [What happens to a task that is started and never awaited?](../a_task_nobody_awaits/README.md)
- After this: [Who runs an async task, and on how many threads?](../who_runs_the_tasks/README.md)
- [How does a receiver learn that no more values will come?](../../05_Message_Passing/closing_a_channel/README.md)
- [How does one event reach every subscriber?](../../05_Message_Passing/publish_and_subscribe/README.md)
- The Rust library's [Streams, sinks, and pipelining ↗](https://masiarek.github.io/rust-learning-library/35_Async/building_minidb/streams_sinks_and_pipelining/index.html)
- The Go library's [Closing a channel ends a range ↗](https://masiarek.github.io/go-learning-library/02_Channels/closing_a_channel_ends_a_range/index.html)
- Concepts: [Async stream](../../11_Concepts/async/async_stream/README.md) · [Backpressure](../../11_Concepts/communication/backpressure/README.md) · [Channel](../../11_Concepts/communication/channel/README.md) · [Reactive programming](../../11_Concepts/async/reactive_programming/README.md) · [Coroutine](../../11_Concepts/units_of_execution/coroutine/README.md)
