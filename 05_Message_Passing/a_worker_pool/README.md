# How do N workers share one queue of jobs?

**Level:** 201 · anyone whose fan-out became a permanent fixture

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A worker pool is fan-out made permanent: N workers started once, reading one job channel until it closes, with results going back on another — and its three design decisions are the ones this chapter has been building toward: how many workers, how long the job queue may grow, and how the pool learns it is done.

## The question

Thread pools in [chapter 01](../../01_Threads/reusing_threads_in_a_pool/README.md) came from the libraries. This page builds one from a channel, in each language, and uses it: a hundred jobs, four workers, results collected and summed. Then it exercises the three decisions — the queue is bounded so the submitter waits; the job channel is closed so the workers exit; a job that panics does not take the pool with it.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | four `thread::scope` workers on one `Receiver` under a `Mutex`; results on a second channel; dropping the job `Sender` ends them |
| Go | four goroutines, a jobs channel, a results channel, a `WaitGroup`: the Go library's worker pool lesson |
| C | four `pthread_t`s on a hand-built queue with a *shutdown* flag |
| C++ | four `std::jthread`s and a `stop_token` from `request_stop` |
| Java | `ExecutorService` is this, finished; the page builds one on a `BlockingQueue` to show what it hides |
| Python | `ThreadPoolExecutor` is this; the page builds one on `queue.Queue` to show the same |

## What the programs have to show

- a hundred jobs, four workers, the sum of results — and that no worker ran more than its share, as *Real runs*
- the bounded job queue blocking the submitter at job 9
- one job that fails: the pool's other 99 results still arrive

## See also

- Before this: [How does one stream split across workers and merge back?](../fan_out_fan_in/README.md)
- After this: [What if only one thread is allowed to touch the data?](../one_owner_receives_the_numbers/README.md)
- [How does one stream split across workers and merge back?](../fan_out_fan_in/README.md)
- [Why reuse a thread at all?](../../01_Threads/reusing_threads_in_a_pool/README.md)
- [How many workers should a pool have?](../../07_Parallelism/how_many_workers/README.md)
- The Go library's [A worker pool ↗](https://masiarek.github.io/go-learning-library/06_Patterns/a_worker_pool/index.html)
- Concepts: [Worker pool](../../11_Concepts/communication/worker_pool/README.md) · [Task queue](../../11_Concepts/communication/task_queue/README.md) · [Thread pool and executor](../../11_Concepts/units_of_execution/thread_pool/README.md) · [Fan-out, fan-in](../../11_Concepts/communication/fan_out_fan_in/README.md) · [Channel](../../11_Concepts/communication/channel/README.md)
