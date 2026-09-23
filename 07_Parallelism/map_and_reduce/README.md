# Why is a reduction the hard half of a parallel map?

**Level:** 201 · anyone who parallelized a map and then serialized the sum

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A parallel map is easy because the outputs are independent; the reduce that combines them is where the threads meet, and it is either serialized behind a lock — which throws away the parallelism — or done as a tree of partial results, which works only when the operation is associative, and floating-point addition is not quite.

## The question

Map a million records to a number each, then add them up. The map is embarrassingly parallel. The add: a lock around a shared total is the lost-update fix from chapter 02 and it makes the eight threads queue for the total. A partial sum per thread and a final combine keeps them apart. The page measures both, then shows the associativity trap: the tree sum of floats differs from the serial sum, as [When does order change a sum?](../../02_Shared_State/when_order_changes_a_sum/README.md) predicts.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | map over chunks in `thread::scope`, each returning its partial sum, combined by the caller |
| Go | a results channel and a final loop, or per-goroutine partials |
| C | per-thread partials handed back through `pthread_join`'s `void *` |
| C++ | `std::transform_reduce(std::execution::par, ...)`, which does exactly this |
| Java | `stream().parallel().map(f).reduce(0, Integer::sum)`, and the reduce's associativity requirement in its Javadoc |
| Python | `Pool.map` then `sum`, where the reduce is serial by construction |

## What the programs have to show

- the locked total and the partial sums: the same integer total, and a *Real runs* fence of the two times
- the float case: the serial total and the tree total, differing in the last digits
- Java's `reduce` with a non-associative operation: the wrong answer, deterministic under a forced split

## See also

- Before this: [How does a recursive job split itself across cores?](../fork_join/README.md)
- After this: [How many workers should a pool have?](../how_many_workers/README.md)
- [Splitting a sum across workers](../splitting_a_sum_across_workers/README.md)
- [When does order change a sum?](../../02_Shared_State/when_order_changes_a_sum/README.md)
- Concepts: [Map-reduce](../../11_Concepts/parallelism/map_reduce/README.md) · [Data parallelism](../../11_Concepts/parallelism/data_parallelism/README.md) · [Parallel algorithms](../../11_Concepts/parallelism/parallel_algorithms/README.md) · [Contention](../../11_Concepts/hazards/contention/README.md)
