# How does one stream split across workers and merge back?

**Level:** 201 · anyone whose one slow stage needs more than one thread

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** Fan-out gives several workers one input channel to compete for and fan-in merges their output channels into one, which is how the slow stage of a pipeline gets more cores — and the merged stream comes out in the order the workers finished, not the order the items went in, which every consumer of a fan-in has to be ready for.

## The question

The transform stage takes ten times longer than the others. Give it four workers reading the same input channel; then merge their four outputs. The page runs a thousand numbered items through, checks that every item arrived exactly once, and shows the order they arrived in — scrambled — then shows the reordering step that restores it, and what that costs.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | four threads on one `Receiver` behind an `Arc<Mutex<_>>`, or `crossbeam`'s multi-consumer channel (link); fan-in on one `Sender` cloned four times |
| Go | four goroutines reading one channel, a `WaitGroup` closing the merged channel when all four are done |
| C | four processes reading one pipe: reads of one item are atomic up to `PIPE_BUF` |
| C++ | four `std::jthread`s pulling from one queue and pushing to one queue |
| Java | four threads on one `BlockingQueue` in, one out; or a `ForkJoinPool` |
| Python | four threads on one `Queue` in, one out |

## What the programs have to show

- a thousand items, four workers: every item once, and the first twenty in arrival order — which the key records as *not* 1..20
- the reorder buffer restoring the order, and its peak size
- closing the merged channel only after every worker is done, and the hang when one is forgotten

## See also

- Before this: [How do three stages run at once on one stream of values?](../a_pipeline_of_stages/README.md)
- After this: [How do N workers share one queue of jobs?](../a_worker_pool/README.md)
- [How do three stages run at once on one stream of values?](../a_pipeline_of_stages/README.md)
- [How do N workers share one queue of jobs?](../a_worker_pool/README.md)
- The Go library's [Fan-out, fan-in ↗](https://masiarek.github.io/go-learning-library/06_Patterns/fan_out_fan_in/index.html)
- The Go library's [A worker pool ↗](https://masiarek.github.io/go-learning-library/06_Patterns/a_worker_pool/index.html)
- Concepts: [Fan-out, fan-in](../../11_Concepts/communication/fan_out_fan_in/README.md) · [Worker pool](../../11_Concepts/communication/worker_pool/README.md) · [Channel](../../11_Concepts/communication/channel/README.md) · [Pipeline](../../11_Concepts/communication/pipeline/README.md) · [Nondeterminism](../../11_Concepts/foundations/nondeterminism/README.md)
