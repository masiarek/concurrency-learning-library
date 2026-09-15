# Granularity

**Category:** [Foundations](../README.md) · **Status:** stub · **Lessons:** chapter 07, Parallelism *(planned)*

**One line:** How big the pieces of work handed to separate tasks are: too coarse leaves cores idle, too fine spends more on coordinating the pieces than on the work in them.

Also called: task granularity, coarse-grained, fine-grained.

## How it connects


- **See also:** [Oversubscription](../oversubscription/README.md), [Speedup and Amdahl's law](../speedup_and_amdahls_law/README.md)

## In each language

| | |
|---|---|
| Rust | Rayon's [`with_min_len` ↗](https://docs.rs/rayon/latest/rayon/iter/trait.IndexedParallelIterator.html#method.with_min_len) stops a parallel iterator splitting below a given length |
| Java | [`ForkJoinTask` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/ForkJoinTask.html) gives a rule of thumb: a task should perform more than 100 and less than 10000 basic computational steps |
| Python | [`Executor.map` ↗](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.map) with `ProcessPoolExecutor` takes a `chunksize`; a larger one can greatly speed up long iterables |
| C# | [Custom partitioners ↗](https://learn.microsoft.com/en-us/dotnet/standard/parallel-programming/custom-partitioners-for-plinq-and-tpl) group loop iterations into ranges when each one does little work |

## Where to read more

- **In the books:** [*Pro TBB*](../../../10_Resources/books_cpp/README.md#voss_pro_tbb), Michael Voss, Rafael Asenjo, James Reinders — ch. 16, 'Tuning TBB Algorithms: Granularity, Locality, Parallelism, and Determinism'
- **In the books:** [*Grokking Concurrency*](../../../10_Resources/books_general/README.md#bobrov_grokking_concurrency), Kirill Bobrov — ch. 7, 'Decomposition' → 'Granularity'
- **Notes:** [granularity - async ↗](https://docs.google.com/document/d/1maQmN7P6048Px5MIhHitgYvO3M688VMIJkIZkifuS14/edit?tab=t.0)
- **Reference:** [Wikipedia: Granularity (parallel computing) ↗](https://en.wikipedia.org/wiki/Granularity_(parallel_computing))

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
