# How does one thread wait on several channels at once?

**Level:** 201 · anyone who wants the first of two results, or a result or a timeout

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** Go's `select` waits on any number of channel operations and takes whichever is ready first, choosing at random among several — and it is the construct the other languages most conspicuously lack: Rust's std has no `select`, Java and Python have to wait on one queue at a time, and the workaround everywhere is to route every source into a single channel.

## The question

Two workers, two channels, and a caller that wants whichever answers first. In Go it is four lines. In Rust's std, there is no way to wait on two `Receiver`s; `crossbeam` has `select!`, `tokio` has one for async. In Java, `BlockingQueue` has no multi-wait; in Python neither has `queue.Queue`. The page shows the Go version, the fan-in workaround in the others, and Go's random choice when both are ready.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | no `select` in std: fan both sources into one `mpsc` channel; `crossbeam::select!` otherwise (link, not run) |
| Go | `select { case v := <-a: case v := <-b: }`; with both ready, uniformly random |
| C | `poll(2)` on the two pipes' file descriptors is the operating system's `select` |
| C++ | fan-in into one queue with a condition variable; no library multi-wait |
| Java | fan-in into one `BlockingQueue`; or `CompletableFuture.anyOf` for one-shot results |
| Python | fan-in into one `Queue`; `selectors` for file descriptors; `asyncio.wait` for tasks |

## What the programs have to show

- two workers, one at 1 s and one at 3 s: which result the caller printed first, per language
- Go's random choice measured over a thousand rounds with both ready, as *Real runs*
- the fan-in, and what it cannot do that `select` can: send-side selection

## See also

- Before this: [How does a receiver learn that no more values will come?](../closing_a_channel/README.md)
- After this: [How do three stages run at once on one stream of values?](../a_pipeline_of_stages/README.md)
- [How does one stream split across workers and merge back?](../fan_out_fan_in/README.md)
- [What does a wait return when the time runs out?](../../04_Waiting_For_Each_Other/waiting_with_a_timeout/README.md)
- The Go library's [`select` waits on many channels ↗](https://masiarek.github.io/go-learning-library/03_Select/select_waits_on_many/index.html)
- The Go library's [`select` chooses at random ↗](https://masiarek.github.io/go-learning-library/03_Select/select_chooses_at_random/index.html)
- The Go library's [A nil channel disables a case ↗](https://masiarek.github.io/go-learning-library/03_Select/a_nil_channel_disables_a_case/index.html)
- Concepts: [Select](../../11_Concepts/communication/select/README.md) · [Channel](../../11_Concepts/communication/channel/README.md) · [Fan-out, fan-in](../../11_Concepts/communication/fan_out_fan_in/README.md) · [I/O multiplexing](../../11_Concepts/scheduling/io_multiplexing/README.md)
