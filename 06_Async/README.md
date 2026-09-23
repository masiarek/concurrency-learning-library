# 06 — Async

`async` is concurrency without threads: one thread, an event loop, and tasks that give the loop back at every `await`. It changes the questions. There is no data race to find and no lock to forget, and instead a blocking call anywhere stops everything, a task nobody awaits fails silently, and cancellation is either automatic or impossible depending on the language. The chapter starts by writing the loop itself, so that nothing after it is magic.

Every lesson in this chapter is a **stub**: the question, the expected answer per language and what the programs will have to show, waiting for the programs. A stub becomes a lesson when its examples run in CI and its table is replaced by what they printed.

| Lesson | The one thing |
|---|---|
| [What does an event loop do all day?](what_an_event_loop_does/README.md) | *stub* — one thread, one `while`: run the ready task to its next `await`, then sleep in `poll` until something is |
| [What is a future before it has a value?](a_future_is_a_value_not_yet_there/README.md) | *stub* — a Java future is already running; a Rust future does nothing until polled |
| [What happens at an `await`?](async_and_await/README.md) | *stub* — `await` is where a task may stop and hand back its thread, its locals kept in the future |
| [What does one blocking call do to every other task?](blocking_the_event_loop/README.md) | *stub* — one blocking call stops every task on the loop for as long as it takes |
| [Where does a callback keep its state?](a_callback_and_its_state/README.md) | *stub* — a callback carries its state by hand — closure, `void *`, object — which is what `await` was invented to hide |
| [How is a running task told to stop, and does it?](cancelling_an_async_task/README.md) | *stub* — Rust drops the future, Python throws at the next `await`, Go and C leave it to a flag the task checks |
| [What happens to the work when an await times out?](a_timeout_on_an_await/README.md) | *stub* — the caller gets control back at the deadline; whether the work stops depends on the language |
| [Why can't a normal function call an async one?](function_coloring/README.md) | *stub* — an async function can only be awaited from an async function, so `async` spreads upward; Go and virtual threads have no colors |
| [What happens to a task that is started and never awaited?](a_task_nobody_awaits/README.md) | *stub* — a failure nobody sees, or a wait that never ends, and nothing reports it; structured concurrency makes both impossible |
| [How does a loop await a sequence of values that arrive over time?](an_async_stream/README.md) | *stub* — an iterator whose `next` is awaited; `async for`, a channel, `Flow.Publisher` |
| [Who runs an async task, and on how many threads?](who_runs_the_tasks/README.md) | *stub* — one thread or all cores — and on a multi-threaded runtime a task may resume somewhere else |
| [How does one thread watch a thousand sockets?](io_multiplexing_under_the_loop/README.md) | *stub* — `poll`, `epoll`, `kqueue`: one thread watches a thousand sockets at no cost per idle one |
| [Why may only one thread touch the user interface?](the_ui_thread/README.md) | *stub* — one thread owns the widgets; work elsewhere and post the result back |
