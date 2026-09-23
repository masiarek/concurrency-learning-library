# How does one thread watch a thousand sockets?

**Level:** 201 · anyone who wants to know what the event loop is waiting on

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** Under every event loop is one system call — `poll`, `epoll_wait`, `kqueue` — that takes a set of file descriptors and sleeps until one is ready, which is how one thread serves a thousand idle connections at no cost per connection; a thread per connection pays a stack each, and the two designs meet in the middle when the connections are busy rather than idle.

## The question

A thousand client sockets, one message each, spread over a second. Serve them with a thread each, and with one thread and `poll`. The page counts the threads, the memory and the time for both, as *Real runs*, and shows the system call under the loop in the languages that let you see it — then shows the case that flips the result: every connection busy at once.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `mio` wraps `epoll`/`kqueue` for `tokio` (link, not run); the std column is a thread per connection |
| Go | `net.Listen` and a goroutine per connection, with the runtime's `netpoll` underneath doing the `epoll` |
| C | `poll(2)` over an array of descriptors, the loop written out |
| C++ | the same; or `boost::asio` (link, not run) |
| Java | `java.nio.channels.Selector`; or a virtual thread per connection over the same NIO |
| Python | `selectors.DefaultSelector`, which `asyncio` uses underneath |

## What the programs have to show

- a thousand connections served both ways, as *Real runs*: threads, RSS, time
- the CI example at ten connections: every message answered, both ways
- `strace -c` or `dtruss` counting the `epoll_wait`/`kevent` calls under the loop, as *Real runs*

## See also

- Before this: [Who runs an async task, and on how many threads?](../who_runs_the_tasks/README.md)
- After this: [Why may only one thread touch the user interface?](../the_ui_thread/README.md)
- [What does an event loop do all day?](../what_an_event_loop_does/README.md)
- [How many threads can you start?](../../01_Threads/how_many_threads_can_you_start/README.md)
- The Rust library's [The Tokio runtime ↗](https://masiarek.github.io/rust-learning-library/35_Async/building_minidb/the_tokio_runtime/index.html)
- Concepts: [I/O multiplexing](../../11_Concepts/scheduling/io_multiplexing/README.md) · [Event loop](../../11_Concepts/scheduling/event_loop/README.md) · [Blocking and non-blocking calls](../../11_Concepts/foundations/blocking_and_nonblocking/README.md) · [Thread pool and executor](../../11_Concepts/units_of_execution/thread_pool/README.md) · [I/O-bound and CPU-bound work](../../11_Concepts/foundations/io_bound_and_cpu_bound/README.md)
