# What does one blocking call do to every other task?

**Level:** 201 · anyone whose async server went quiet for a second at a time

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A call that blocks the thread — a sleep, a synchronous read, a CPU loop — inside an async task stops the event loop, and with it every task on it, for as long as the call takes; nothing on the loop can run until it returns, and the fix is to move the call to a thread that is not the loop's.

## The question

Ten tasks each print once a tenth of a second. One task calls a blocking `sleep(1)`. For that second, the other nine print nothing — the page counts their prints in that window and finds zero. Then the blocking call is moved off the loop (`spawn_blocking`, `run_in_executor`, `to_thread`) and the count is nine each. Go's column is the contrast: a blocking call in a goroutine costs a thread, not the program.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `std::thread::sleep` in a `tokio` task stalls its worker; `spawn_blocking` is the fix (link, not run; std has no runtime) |
| Go | a blocking call in a goroutine blocks one OS thread and the runtime hands the others new work |
| C | a blocking `read` inside the hand-written loop stalls everything, which is why the loop uses non-blocking descriptors |
| C++ | the same as C |
| Java | on a virtual thread a blocking call unmounts the carrier — except inside `synchronized` before Java 24 |
| Python | `time.sleep(1)` in a coroutine stalls the loop; `await asyncio.to_thread(time.sleep, 1)` does not |

## What the programs have to show

- ten ticking tasks and one blocking call: the tick counts during the blocked second
- the same with the call moved off the loop
- Go's goroutines ticking through a blocking call in another goroutine

## See also

- Before this: [What happens at an `await`?](../async_and_await/README.md)
- After this: [Where does a callback keep its state?](../a_callback_and_its_state/README.md)
- [What does an event loop do all day?](../what_an_event_loop_does/README.md)
- [What is a goroutine, if not a thread?](../../01_Threads/a_goroutine_is_not_a_thread/README.md)
- The Rust library's [Common async pitfalls ↗](https://masiarek.github.io/rust-learning-library/35_Async/common_async_pitfalls/index.html)
- The Rust library's [Tasks ↗](https://masiarek.github.io/rust-learning-library/35_Async/building_minidb/tasks/index.html)
- Concepts: [Blocking the event loop](../../11_Concepts/async/blocking_the_event_loop/README.md) · [Blocking and non-blocking calls](../../11_Concepts/foundations/blocking_and_nonblocking/README.md) · [Event loop](../../11_Concepts/scheduling/event_loop/README.md) · [Cooperative scheduling](../../11_Concepts/scheduling/cooperative_scheduling/README.md) · [I/O-bound and CPU-bound work](../../11_Concepts/foundations/io_bound_and_cpu_bound/README.md)
