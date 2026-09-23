# Can a `for` loop be made parallel by changing one word?

**Level:** 201 · anyone who wants the speedup without the threads

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** Rust's `rayon`, Java's parallel streams and C++'s execution policies each let a sequential loop become a parallel one by changing one call, and the trade is that the loop body may now run on any thread in any order — which is fine for a sum and wrong for anything that appends to a list, prints in order, or depends on the previous iteration.

## The question

`.iter().map(f).sum()` → `.par_iter().map(f).sum()`. `.stream()` → `.parallelStream()`. `std::transform(...)` → `std::transform(std::execution::par, ...)`. The page makes each change on a sum and gets the same answer faster, then makes it on a loop that pushes to a shared vector and gets a compile error, a data race, or a wrong count, depending on the language.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `rayon::par_iter` (link, not run); std has no parallel iterator, so the std column is `thread::scope` over chunks |
| Go | no parallel iterator; a worker pool, or a channel of chunks |
| C | none; `#pragma omp parallel for` with OpenMP is the C world's one-word version |
| C++ | `std::execution::par` on the standard algorithms |
| Java | `parallelStream()`; `forEachOrdered` to keep order at a cost |
| Python | none for threads; `multiprocessing.Pool.map` for processes |

## What the programs have to show

- the one-word change on a sum: same total, and a *Real runs* fence of the time
- the same change on a loop that appends to a shared list: the error or the wrong count
- the ordered variant, and what it costs

## See also

- Before this: [Same work on different data, or different work at once?](../data_parallel_or_task_parallel/README.md)
- After this: [How does a recursive job split itself across cores?](../fork_join/README.md)
- [Same work on different data, or different work at once?](../data_parallel_or_task_parallel/README.md)
- [Splitting a sum across workers](../splitting_a_sum_across_workers/README.md)
- Concepts: [Parallel iterators and streams](../../11_Concepts/parallelism/parallel_iterators/README.md) · [Data parallelism](../../11_Concepts/parallelism/data_parallelism/README.md) · [Parallel algorithms](../../11_Concepts/parallelism/parallel_algorithms/README.md) · [OpenMP](../../11_Concepts/parallelism/openmp/README.md) · [Nondeterminism](../../11_Concepts/foundations/nondeterminism/README.md)
