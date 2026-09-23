# Why reuse a thread at all?

**Level:** 201 · anyone who starts a thread per request

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** Starting an operating-system thread costs a system call and a stack, and a pool that keeps a fixed number of threads alive and hands them work from a queue turns that cost into a one-time one — every language here has a pool in its standard library or its idioms except C, where the pool is the classic thing you build from a mutex, a condition variable and a queue.

## The question

A thousand small jobs. Start a thread each, or keep eight threads and feed them a queue? The pool is faster and, more importantly, it bounds how many threads exist at once — which is what stops the thousand jobs from becoming a thousand threads. The page shows the shape of a pool in each language, what happens to a job submitted after the pool is shut down, and how the pool's size is chosen.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | no pool in std; `thread::scope` for bounded fan-out, `rayon` or a channel-fed loop of workers otherwise |
| Go | no pool type either: a `WaitGroup` and N goroutines reading one channel is the idiom |
| C | hand-built: N `pthread_t`, a mutex, a condition variable, a queue |
| C++ | no standard pool until C++26's `std::execution`; a `std::jthread` vector reading a queue |
| Java | `Executors.newFixedThreadPool(n)` and, since Java 21, `newVirtualThreadPerTaskExecutor` |
| Python | `concurrent.futures.ThreadPoolExecutor(max_workers=n)` |

## What the programs have to show

- eight workers, a thousand jobs, each job recording which worker ran it; the page prints only the total and that every job ran once
- a job submitted after shutdown: rejected, run anyway, or raised — per language
- a *Real runs* fence timing a thread per job against the pool

## See also

- Before this: [Is a thread-local variable really one per thread?](../a_variable_per_thread/README.md)
- After this: [What is a goroutine, if not a thread?](../a_goroutine_is_not_a_thread/README.md)
- [How do N workers share one queue of jobs?](../../05_Message_Passing/a_worker_pool/README.md)
- [How many workers should a pool have?](../../07_Parallelism/how_many_workers/README.md)
- The Go library's [A worker pool ↗](https://masiarek.github.io/go-learning-library/06_Patterns/a_worker_pool/index.html)
- Concepts: [Thread pool and executor](../../11_Concepts/units_of_execution/thread_pool/README.md) · [Worker pool](../../11_Concepts/communication/worker_pool/README.md) · [Task queue](../../11_Concepts/communication/task_queue/README.md) · [Oversubscription](../../11_Concepts/foundations/oversubscription/README.md)
