# Why does the ninth core help less than the second?

**Level:** 201 · anyone planning to buy more cores

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** If a fraction *s* of a program cannot be parallelized, then no number of workers makes it faster than 1/*s* — Amdahl's law — so a program that is 10% serial tops out at 10× however many cores it gets, and the speedup curve bends over well before that; the page measures the curve with a deliberately serial 10% and finds the bend.

## The question

A job with a serial part — reading the input — and a parallel part. Time it on 1, 2, 4, 8 and 16 workers. The parallel part shrinks; the serial part does not; the total approaches the serial part. The page plots the measured speedups against the law's prediction for the measured serial fraction, and then asks Gustafson's question: what if the input grows with the cores?

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | the serial read and the scoped parallel part; the measured curve against 1/(s + (1−s)/N) |
| Go | the same with goroutines |
| C | the same with pthreads |
| C++ | the same with `std::execution::par` |
| Java | the same with a parallel stream |
| Python | the same with `multiprocessing`, where the serial part includes pickling the input |

## What the programs have to show

- *Real runs*: speedup on 1..16 workers for a 10% serial job, and the law's prediction beside it
- the CI example: the serial fraction computed from one timed run, without asserting the time
- the same job with input scaled by N: near-linear again

## See also

- Before this: [Why do Python threads take turns?](../the_gil_and_free_threaded_python/README.md)
- After this: [Why are eight threads writing eight different variables slow?](../false_sharing/README.md)
- [How much faster is real work on eight threads?](../cpu_bound_speedup/README.md)
- [How many workers should a pool have?](../how_many_workers/README.md)
- Concepts: [Speedup and Amdahl's law](../../11_Concepts/foundations/speedup_and_amdahls_law/README.md) · [Parallelism](../../11_Concepts/foundations/parallelism/README.md) · [Granularity](../../11_Concepts/foundations/granularity/README.md) · [Sequential execution](../../11_Concepts/foundations/sequential_execution/README.md)
