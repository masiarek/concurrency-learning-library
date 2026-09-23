# How do three stages run at once on one stream of values?

**Level:** 201 · anyone with a read-parse-write loop that uses one core

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A pipeline puts each stage on its own thread with a channel between them, so that the parser works on item 2 while the reader fetches item 3 and the writer stores item 1 — which gives a speedup of up to the number of stages and no more, bounded by the slowest stage, and it fails in one characteristic way: a stage that stops without closing its output leaves the rest waiting.

## The question

Read, transform, write, over a thousand items. In one loop it takes the sum of the three stage times. As a pipeline it takes about the maximum, once the pipe is full. The page builds the three-stage pipeline in each language, checks that every item came out once and in order, and shows the shutdown: the reader closes its channel, the transformer sees the close and closes its own, and the writer finishes.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | three threads and two `mpsc` channels; dropping each `Sender` propagates the end |
| Go | three goroutines and two channels; `close` propagates; the Go library's pipeline lesson is the model |
| C | three processes and two pipes, which is what a shell pipeline is |
| C++ | three `std::jthread`s and two hand-built queues with a *done* flag |
| Java | three threads and two `BlockingQueue`s with a poison pill passed along |
| Python | three threads and two `Queue`s with a `None` passed along |

## What the programs have to show

- a thousand items through three stages, each sleeping a millisecond: the count out, in order
- a *Real runs* fence of the pipeline's time against the loop's
- the stage that fails mid-stream: what the stages downstream see

## See also

- Before this: [How does one thread wait on several channels at once?](../waiting_on_several_channels/README.md)
- After this: [How does one stream split across workers and merge back?](../fan_out_fan_in/README.md)
- [How does a receiver learn that no more values will come?](../closing_a_channel/README.md)
- [How does one stream split across workers and merge back?](../fan_out_fan_in/README.md)
- The Go library's [A pipeline of stages ↗](https://masiarek.github.io/go-learning-library/06_Patterns/a_pipeline_of_stages/index.html)
- The Linux library's [head closes the pipe early ↗](https://masiarek.github.io/linux-learning-library/01_Pipelines/head_closes_the_pipe_early/index.html)
- The Rust library's [Streams, sinks, and pipelining ↗](https://masiarek.github.io/rust-learning-library/35_Async/building_minidb/streams_sinks_and_pipelining/index.html)
- Concepts: [Pipeline](../../11_Concepts/communication/pipeline/README.md) · [Channel](../../11_Concepts/communication/channel/README.md) · [Dataflow programming](../../11_Concepts/communication/dataflow/README.md) · [Backpressure](../../11_Concepts/communication/backpressure/README.md) · [Task parallelism](../../11_Concepts/parallelism/task_parallelism/README.md)
