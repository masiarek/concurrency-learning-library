# How many workers should a pool have?

**Level:** 201 · anyone who set the pool size to 100 to be safe

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** For CPU-bound work the right number of workers is the number of cores, and more only adds context switches; for work that waits on I/O the right number is higher, roughly cores × (1 + wait/compute); and setting it to a hundred for safety makes the CPU-bound case slower and the memory larger, which is oversubscription.

## The question

A CPU-bound job on 1, 4, 8, 16, 64 and 256 workers, on an eight-core machine. The speedup rises to eight and then falls. An I/O-bound job — each task sleeps 90% of its time — on the same counts: the speedup keeps rising to about eighty. The page measures both curves as *Real runs* and shows the knee, then reads what each language's default pool size is and why.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `available_parallelism()` for the count; the page sweeps it with `thread::scope` |
| Go | `GOMAXPROCS` defaults to the cores; goroutines above it queue |
| C | `sysconf(_SC_NPROCESSORS_ONLN)` |
| C++ | `std::thread::hardware_concurrency()` |
| Java | `ForkJoinPool.commonPool()` has cores − 1; `Executors.newCachedThreadPool` is unbounded |
| Python | `os.cpu_count()`; `ThreadPoolExecutor`'s default is `min(32, cpu_count + 4)`, tuned for I/O |

## What the programs have to show

- *Real runs*: speedup against worker count for the CPU job and the I/O job
- each language's reported core count and default pool size, printed
- the CI example: the jobs' results, the same at every count

## See also

- Before this: [Why is a reduction the hard half of a parallel map?](../map_and_reduce/README.md)
- [How much faster is real work on eight threads?](../cpu_bound_speedup/README.md)
- [How do N workers share one queue of jobs?](../../05_Message_Passing/a_worker_pool/README.md)
- The Go library's [A worker pool ↗](https://masiarek.github.io/go-learning-library/06_Patterns/a_worker_pool/index.html)
- Concepts: [Oversubscription](../../11_Concepts/foundations/oversubscription/README.md) · [Granularity](../../11_Concepts/foundations/granularity/README.md) · [Thread pool and executor](../../11_Concepts/units_of_execution/thread_pool/README.md) · [I/O-bound and CPU-bound work](../../11_Concepts/foundations/io_bound_and_cpu_bound/README.md) · [Context switch](../../11_Concepts/units_of_execution/context_switch/README.md)
