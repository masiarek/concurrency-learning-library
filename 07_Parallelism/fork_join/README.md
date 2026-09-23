# How does a recursive job split itself across cores?

**Level:** 201 · anyone parallelizing quicksort or a tree walk

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A fork-join job splits itself in two, runs the halves in parallel, and joins them — recursively, down to a threshold below which it runs serially — and the threshold is the whole tuning problem: too low and the forking costs more than the work, too high and the cores sit idle; work-stealing schedulers exist to make the forks cheap enough that the threshold can be low.

## The question

Sum a tree, or sort an array, by splitting in half and recursing. Fork a task for each half at every level and a million-element array forks a million tasks. Fork only above a threshold of, say, ten thousand and it forks a hundred. The page implements the split in each language, sweeps the threshold, and shows the time curve as *Real runs* — with the pool's work-stealing visible in Java's and Rust's columns.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `rayon::join` (link, not run); the std column uses `thread::scope` and recurses with a depth limit |
| Go | goroutines per half above a threshold, a `WaitGroup` to join |
| C | pthreads per half above a threshold, which is expensive; the threshold must be high |
| C++ | `std::async` per half, or a hand-rolled pool |
| Java | `ForkJoinPool` with `RecursiveTask` — the design this page is named after |
| Python | `multiprocessing` cannot fork cheaply; the page's Python column shows why the threshold must be huge |

## What the programs have to show

- the recursive sum with a threshold: the total, identical at every threshold
- *Real runs*: time against threshold, per language
- Java's `ForkJoinPool.getStealCount()` after the run

## See also

- Before this: [Can a `for` loop be made parallel by changing one word?](../a_parallel_iterator/README.md)
- After this: [Why is a reduction the hard half of a parallel map?](../map_and_reduce/README.md)
- [Same work on different data, or different work at once?](../data_parallel_or_task_parallel/README.md)
- [How many workers should a pool have?](../how_many_workers/README.md)
- Concepts: [Fork-join](../../11_Concepts/parallelism/fork_join/README.md) · [Work stealing](../../11_Concepts/scheduling/work_stealing/README.md) · [Granularity](../../11_Concepts/foundations/granularity/README.md) · [Task parallelism](../../11_Concepts/parallelism/task_parallelism/README.md) · [Thread pool and executor](../../11_Concepts/units_of_execution/thread_pool/README.md)
