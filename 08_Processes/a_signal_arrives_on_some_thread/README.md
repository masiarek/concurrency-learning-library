# Which thread gets the signal?

**Level:** 201 · anyone whose Ctrl-C handler ran on the wrong thread

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A signal sent to a process is delivered to *one* of its threads — any that has not blocked it — and the handler runs on that thread in the middle of whatever it was doing, which is why a handler may do almost nothing safely; the languages that hide this route the signal to a known place: Go to a channel, Python to the main thread's next bytecode, Rust to nothing unless you ask.

## The question

Three threads busy in loops, and the process gets `SIGUSR1`. Which thread's handler runs? On Linux, whichever the kernel picks. The page records the thread id seen by the handler over a hundred signals, as *Real runs*, and then shows the fix each language offers: block the signal in every thread but one, and have that one wait for it — which is what Go's `signal.Notify` and Rust's `signal-hook` do underneath.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | std has no handler API; `signal-hook` or `ctrlc` (link, not run); the Rust library's page on catching a signal is the reference |
| Go | `signal.Notify(ch, syscall.SIGUSR1)`: the runtime catches it on any thread and sends on the channel |
| C | `sigaction` on any thread; `pthread_sigmask` to block it in workers; `sigwait` in one thread |
| C++ | the same as C |
| Java | `sun.misc.Signal` (not standard); the JVM handles most signals itself |
| Python | the handler runs on the main thread only, between bytecodes; a worker thread cannot receive one |

## What the programs have to show

- *Real runs*: the thread that handled each of a hundred `SIGUSR1`s, in C
- the blocked-in-workers, waited-in-one version: every signal on the chosen thread
- Python's main-thread rule, and what happens to a signal while the main thread is blocked in a lock

## See also

- Before this: [How do two processes talk through a pipe?](../a_pipe_between_processes/README.md)
- After this: [When are processes the better workers?](../multiprocessing_instead_of_threads/README.md)
- [How do two processes talk through a pipe?](../a_pipe_between_processes/README.md)
- [What does a failure on a thread do when nobody is waiting for it?](../../01_Threads/a_failure_nobody_is_waiting_for/README.md)
- The Rust library's [Catching a signal ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/catching_a_signal/index.html)
- The Python library's [Ctrl-C is a signal ↗](https://masiarek.github.io/python-learning-library/02_Projects_and_Environments/ctrl_c_is_a_signal/index.html)
- The Linux library's [The signals you cannot catch ↗](https://masiarek.github.io/linux-learning-library/11_Signals/signals_you_cannot_catch/index.html)
- Concepts: [Signals](../../11_Concepts/communication/signals/README.md) · [Process](../../11_Concepts/units_of_execution/process/README.md) · [Thread](../../11_Concepts/units_of_execution/thread/README.md) · [Inter-process communication](../../11_Concepts/communication/ipc/README.md)
