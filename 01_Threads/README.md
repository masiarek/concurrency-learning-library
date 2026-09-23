# 01 — Threads

Every language here can start an operating-system thread, and they agree on that much. They disagree about the edges of a thread's life: whether the program waits for it at the end, how its answer gets back to whoever started it, how long the data it was lent has to stay alive, and what happens when it fails. Those edges are where a first threaded program goes wrong, so they come before any question about sharing memory.

| Lesson | The one thing |
|---|---|
| [Who waits when main returns?](who_waits_when_main_returns/README.md) | Rust, Go, C and C++ end the process; Java and Python wait for their ordinary threads |
| [Getting a result back](getting_a_result_back/README.md) | only Rust and C hand the value back through the join |
| [Can a thread borrow a local variable?](lending_a_local_to_a_thread/README.md) | `thread::scope` is the two `pthread_join` calls you remembered to write, promoted from a convention to a type — and Go moves the local to the heap instead |
| [What does a failure on a thread do when nobody is waiting for it?](a_failure_nobody_is_waiting_for/README.md) | *stub* — Go ends the process; Rust, Java and Python print and carry on; C++ terminates; C dies only from a signal |
| [How many threads can you start?](how_many_threads_can_you_start/README.md) | *stub* — OS threads run out in the tens of thousands; goroutines and virtual threads run into the millions |
| [Is a thread-local variable really one per thread?](a_variable_per_thread/README.md) | *stub* — one copy per thread, made on first use; Go has none, on purpose |
| [Why reuse a thread at all?](reusing_threads_in_a_pool/README.md) | *stub* — a pool bounds how many threads exist and turns the start-up cost into a one-time one |
| [What is a goroutine, if not a thread?](a_goroutine_is_not_a_thread/README.md) | *stub* — goroutines, virtual threads and async tasks are runtime-scheduled units on a few OS threads, and a blocking call is what tells them apart |
| [What does a sleep promise, and what does a yield?](sleep_and_yield/README.md) | *stub* — a sleep waits *at least* that long and orders nothing; a yield promises even less |

Rows marked *stub* are questions with their expected answers written down and no program behind them yet; the page says so at the top.
