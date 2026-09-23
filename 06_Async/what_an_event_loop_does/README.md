# What does an event loop do all day?

**Level:** 201 · anyone who has been told JavaScript is single-threaded and does many things at once

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** An event loop is one thread running one `while` loop: take the next ready callback or task, run it to its next suspension point, and when nothing is ready, ask the operating system to sleep until some file descriptor or timer is — which is why a loop handles ten thousand idle connections on one core and why one long computation on it stops all ten thousand.

## The question

The page writes the loop itself, in about thirty lines, in each language that lets you see it: a queue of ready tasks, a set of timers, and a call to `poll` or `select` with the time until the next timer as the timeout. Then it runs three tasks on it — two that sleep and one that computes — and shows the order they progress in, which is the order every `asyncio`, `tokio` and Node program follows.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | the loop under `tokio` is not visible; the page writes a minimal one over `std::task::Waker` and `poll(2)` |
| Go | no event loop: the runtime's scheduler and `netpoll` play the role, and goroutines block instead of yielding |
| C | the loop *is* the program: `poll(2)` in a `while`, dispatching on the ready descriptors |
| C++ | the same as C, with `std::function` callbacks; C++20 coroutines are a syntax for it without a loop |
| Java | no standard event loop; `CompletableFuture` and virtual threads are the two alternatives, and the page shows why |
| Python | `asyncio`'s loop is the reference: the page's hand-written loop and `asyncio.run` produce the same order |

## What the programs have to show

- the hand-written loop running three tasks: the order of their steps, identical to the library loop's
- the loop asleep in `poll` with the timer's timeout, measured as CPU time near zero
- the compute task starving the others: the sleepers' lateness, per loop

## See also

- After this: [What is a future before it has a value?](../a_future_is_a_value_not_yet_there/README.md)
- [What does one blocking call do to every other task?](../blocking_the_event_loop/README.md)
- [Who runs an async task, and on how many threads?](../who_runs_the_tasks/README.md)
- The Rust library's [The Tokio runtime ↗](https://masiarek.github.io/rust-learning-library/35_Async/building_minidb/the_tokio_runtime/index.html)
- The Rust library's [What a future is ↗](https://masiarek.github.io/rust-learning-library/35_Async/what_a_future_is/index.html)
- Concepts: [Event loop](../../11_Concepts/scheduling/event_loop/README.md) · [I/O multiplexing](../../11_Concepts/scheduling/io_multiplexing/README.md) · [Cooperative scheduling](../../11_Concepts/scheduling/cooperative_scheduling/README.md) · [Event-driven programming](../../11_Concepts/async/event_driven_programming/README.md) · [Async runtime (executor and reactor)](../../11_Concepts/scheduling/async_runtime/README.md)
