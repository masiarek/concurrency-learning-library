# How do two processes talk through a pipe?

**Level:** 201 · anyone who has written `a | b`

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A pipe is a kernel buffer with a write end and a read end, and it carries the shell's whole model of concurrency: the writer blocks when the buffer is full, the reader blocks when it is empty, a read returns zero when every write end is closed, and a write with no read end left gets `SIGPIPE` — which is what happens to `yes` when `head` has what it needs.

## The question

The page builds `a | b` by hand — two children, one pipe — in each language, and sends a hundred lines through it. Then it breaks the pipe both ways: the writer closes early, so the reader's `read` returns zero and its loop ends; the reader closes early, so the writer gets `SIGPIPE` or `EPIPE`, which the Linux library's lesson on `head` measures. Both are *results*, not errors, and both are how a pipeline ends.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `Command` with `Stdio::piped()`, and `BrokenPipe` as an `io::Error` because Rust ignores `SIGPIPE` |
| Go | `io.Pipe` in-process; `exec.Cmd.StdoutPipe` between processes; `EPIPE` as an error |
| C | `pipe(2)`, `fork`, `dup2`; `SIGPIPE` kills the writer by default |
| C++ | the same as C |
| Java | `ProcessBuilder.redirectOutput(PIPE)` and `Process.getOutputStream()`; `IOException: Broken pipe` |
| Python | `subprocess.Popen` with `stdout=PIPE`; `BrokenPipeError` |

## What the programs have to show

- a hundred lines through a hand-built pipe: the count received
- the writer closing first: the reader's loop ending on the zero-length read
- the reader closing first: `SIGPIPE`, `EPIPE`, or the exception, per language

## See also

- Before this: [How does a parent learn how its child ended?](../a_child_process_and_its_exit_status/README.md)
- After this: [Which thread gets the signal?](../a_signal_arrives_on_some_thread/README.md)
- [How do three stages run at once on one stream of values?](../../05_Message_Passing/a_pipeline_of_stages/README.md)
- [Which thread gets the signal?](../a_signal_arrives_on_some_thread/README.md)
- The Linux library's [head closes the pipe early ↗](https://masiarek.github.io/linux-learning-library/01_Pipelines/head_closes_the_pipe_early/index.html)
- Concepts: [Inter-process communication](../../11_Concepts/communication/ipc/README.md) · [Process](../../11_Concepts/units_of_execution/process/README.md) · [Buffered and bounded channels](../../11_Concepts/communication/bounded_channel/README.md) · [Backpressure](../../11_Concepts/communication/backpressure/README.md) · [Signals](../../11_Concepts/communication/signals/README.md)
