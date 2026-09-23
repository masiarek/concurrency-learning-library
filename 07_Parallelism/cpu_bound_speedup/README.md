# How much faster is real work on eight threads?

**Level:** 201 · anyone who split a loop across threads and got nothing

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** Splitting CPU-bound work across N threads gives a speedup that approaches N only when the work is big enough to dwarf the cost of starting and joining, the threads do not fight over the same cache lines, and the machine actually has N cores that are not already busy — and Python's threads give no speedup at all until the global interpreter lock is gone.

## The question

[Splitting a sum across workers](../splitting_a_sum_across_workers/README.md) split the work and got the right answer. This page asks whether it got there faster. The same sum over a hundred million numbers, on one worker and on eight, timed — as *Real runs*, since timing is the machine's — and then the same for a sum over a hundred numbers, where eight workers are slower than one.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `thread::scope` over eight chunks: near 8× on eight cores for the big sum, slower than serial for the small one |
| Go | eight goroutines: the same shape; `GOMAXPROCS` bounds it |
| C | eight `pthread_t`s: the same |
| C++ | `std::reduce(std::execution::par, ...)`: the same, chosen by the library |
| Java | eight platform threads, or a parallel stream: the same; virtual threads give no CPU parallelism beyond the carriers |
| Python | eight `threading.Thread`s: 1× under the GIL; eight `multiprocessing` workers: near 8× |

## What the programs have to show

- *Real runs*: the big sum on 1, 2, 4, 8 workers, per language, on this Mac's core count
- the small sum on 1 and 8: the speedup below one
- the CI example: the totals, identical, with no timing

## See also

- After this: [Why do Python threads take turns?](../the_gil_and_free_threaded_python/README.md)
- [Splitting a sum across workers](../splitting_a_sum_across_workers/README.md)
- [Why does the ninth core help less than the second?](../amdahls_law/README.md)
- [How many workers should a pool have?](../how_many_workers/README.md)
- Concepts: [Parallelism](../../11_Concepts/foundations/parallelism/README.md) · [Speedup and Amdahl's law](../../11_Concepts/foundations/speedup_and_amdahls_law/README.md) · [Granularity](../../11_Concepts/foundations/granularity/README.md) · [I/O-bound and CPU-bound work](../../11_Concepts/foundations/io_bound_and_cpu_bound/README.md) · [Global interpreter lock](../../11_Concepts/parallelism/gil/README.md)
