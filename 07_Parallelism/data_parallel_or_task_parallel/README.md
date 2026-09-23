# Same work on different data, or different work at once?

**Level:** 201 · anyone deciding how to split a job

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** Data parallelism runs the same operation over the pieces of one collection — the sum, the map, the filter — and task parallelism runs different operations at once — parse the header while decoding the body — and the two need different tools: chunks and a reduction for the first, futures or a fork-join for the second.

## The question

Two jobs. Resize a thousand images: the same function, a thousand inputs — split the list. Build a report: fetch, parse, render, three different steps with a dependency between two — a task graph. The page does both in each language with that language's tool for each and shows the shape of the code, then the case that is both at once: a task graph whose one heavy node is itself data-parallel.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `chunks` and `thread::scope` for data; `thread::scope` with two handles joined in order for tasks; `rayon` for both (link) |
| Go | a worker pool for data; goroutines and a `WaitGroup` or `errgroup` for tasks |
| C | pthreads over chunks; pthreads per task |
| C++ | `std::execution::par` for data; `std::async` per task |
| Java | a parallel stream for data; `CompletableFuture` graph or `ForkJoinPool` for tasks |
| Python | `multiprocessing.Pool.map` for data; `concurrent.futures` for tasks |

## What the programs have to show

- a thousand items mapped in parallel: the count and a checksum
- a three-task graph with one dependency: the completion order, forced by the dependency
- the combined case, and a *Real runs* fence of its time

## See also

- Before this: [Why are eight threads writing eight different variables slow?](../false_sharing/README.md)
- After this: [Can a `for` loop be made parallel by changing one word?](../a_parallel_iterator/README.md)
- [Can a `for` loop be made parallel by changing one word?](../a_parallel_iterator/README.md)
- [How does a recursive job split itself across cores?](../fork_join/README.md)
- The Go library's [Fan-out, fan-in ↗](https://masiarek.github.io/go-learning-library/06_Patterns/fan_out_fan_in/index.html)
- Concepts: [Data parallelism](../../11_Concepts/parallelism/data_parallelism/README.md) · [Task parallelism](../../11_Concepts/parallelism/task_parallelism/README.md) · [Fork-join](../../11_Concepts/parallelism/fork_join/README.md) · [Map-reduce](../../11_Concepts/parallelism/map_reduce/README.md) · [Parallel iterators and streams](../../11_Concepts/parallelism/parallel_iterators/README.md)
