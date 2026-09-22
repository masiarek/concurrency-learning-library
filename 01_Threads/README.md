# 01 — Threads

Every language here can start an operating-system thread, and they agree on that much. They disagree about the edges of a thread's life: whether the program waits for it at the end, how its answer gets back to whoever started it, how long the data it was lent has to stay alive, and what happens when it fails. Those edges are where a first threaded program goes wrong, so they come before any question about sharing memory.

| Lesson | The one thing |
|---|---|
| [Who waits when main returns?](who_waits_when_main_returns/README.md) | Rust, Go, C and C++ end the process; Java and Python wait for their ordinary threads |
| [Getting a result back](getting_a_result_back/README.md) | only Rust and C hand the value back through the join |
| [Can a thread borrow a local variable?](lending_a_local_to_a_thread/README.md) | `thread::scope` is the two `pthread_join` calls you remembered to write, promoted from a convention to a type — and Go moves the local to the heap instead |

## Planned

- **A failure nobody is waiting for** — what a panic, an exception or a crash on one thread does to the others, when no join or future is there to receive it.
- **How many threads can you start?** — operating-system threads, goroutines and Java's virtual threads, counted on the same machine.
- **Thread-local storage** — `thread_local!`, `_Thread_local`, `thread_local`, `ThreadLocal` and `threading.local`, and Go, which has no such thing.
