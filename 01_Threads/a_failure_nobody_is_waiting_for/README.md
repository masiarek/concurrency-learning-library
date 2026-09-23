# What does a failure on a thread do when nobody is waiting for it?

**Level:** 201 · anyone whose worker thread died quietly

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A panic, an exception or a crash on a thread that nobody joins is either a program-wide failure or a silent one, and the six languages split down the middle: Go ends the process, Rust and Java keep it running with the thread's failure printed to stderr, C++ calls `std::terminate`, C dies only if the failure is a signal, and Python prints a traceback and carries on.

## The question

[Getting a result back](../getting_a_result_back/README.md) shows a thread's failure travelling through its join. This page removes the join. A thread panics, throws or segfaults, and no handle is ever waited on: what happens to the rest of the program, what is printed, and what is the exit status? The answer decides whether a worker that dies at three in the morning takes the server with it or leaves it running with one worker fewer and nothing in the log.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | the panic is printed to stderr with the thread's name; the process continues and exits 0 unless `main` itself panics |
| Go | any unrecovered panic on any goroutine ends the whole process, exit status 2, with the goroutine's stack |
| C | no failure mechanism except a signal: a `SIGSEGV` on any thread kills the process, exit 139 |
| C++ | an exception leaving a `std::thread` function calls `std::terminate`, exit by `SIGABRT` |
| Java | the uncaught exception is printed by the default handler; the process continues, exit 0 |
| Python | the traceback is printed by `threading.excepthook`; the process continues, exit 0 |

## What the programs have to show

- one program per language: a thread that fails deliberately, a main that sleeps two seconds and then prints and exits 0
- a `.sh` driver per language keeping the last line printed, whether main's line appeared, and the exit status
- the Rust and Java rows with a `main` that later joins the handle, to show the failure is not lost, only deferred

## See also

- After this: [How many threads can you start?](../how_many_threads_can_you_start/README.md)
- [Getting a result back](../getting_a_result_back/README.md)
- [Who waits when main returns?](../who_waits_when_main_returns/README.md)
- The Go library's [A panic ends the whole program ↗](https://masiarek.github.io/go-learning-library/01_Goroutines/a_panic_ends_the_whole_program/index.html)
- The Rust library's [Spawning a thread ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/spawning_a_thread/index.html)
- Concepts: [Safety failure](../../11_Concepts/hazards/safety_failure/README.md) · [Liveness failure](../../11_Concepts/hazards/liveness_failure/README.md) · [Join](../../11_Concepts/async/join/README.md) · [Daemon and detached threads](../../11_Concepts/units_of_execution/daemon_thread/README.md)
