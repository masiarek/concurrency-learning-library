# 07 — Parallelism

The earlier chapters are about doing several things at once correctly. This one is about doing one thing on several cores so that it finishes sooner — and about the ways the parallel version stops being the same computation as the serial one. It starts where the textbooks start, with a sum split across workers.

| Lesson | The one thing |
|---|---|
| [Splitting a sum across workers](splitting_a_sum_across_workers/README.md) | private partial sums need no lock; a tree combines them in fewer rounds; and a float total depends on how the additions were grouped |
| [How much faster is real work on eight threads?](cpu_bound_speedup/README.md) | *stub* — near N× on N cores when the work dwarfs the start-up; slower than serial when it does not; 1× under the GIL |
| [Why do Python threads take turns?](the_gil_and_free_threaded_python/README.md) | *stub* — one thread runs bytecode at a time; I/O and C code release it; the `t` build removes it |
| [Why does the ninth core help less than the second?](amdahls_law/README.md) | *stub* — a 10% serial part caps the speedup at 10× however many cores; the curve bends long before that |
| [Why are eight threads writing eight different variables slow?](false_sharing/README.md) | *stub* — eight threads on eight slots of one cache line are slower than one thread; pad to 64 bytes |
| [Same work on different data, or different work at once?](data_parallel_or_task_parallel/README.md) | *stub* — the same operation over pieces of one collection, or different operations at once — different tools |
| [Can a `for` loop be made parallel by changing one word?](a_parallel_iterator/README.md) | *stub* — `par_iter`, `parallelStream`, `execution::par`: one word, and the loop body may now run anywhere in any order |
| [How does a recursive job split itself across cores?](fork_join/README.md) | *stub* — split in half, recurse, join — and the threshold below which to stop is the whole tuning problem |
| [Why is a reduction the hard half of a parallel map?](map_and_reduce/README.md) | *stub* — the map is easy; the reduce is where the threads meet, and a tree reduce needs associativity |
| [How many workers should a pool have?](how_many_workers/README.md) | *stub* — cores for CPU-bound work, more for I/O-bound, and a hundred for safety is oversubscription |

Rows marked *stub* are questions with their expected answers written down and no program behind them yet; the page says so at the top.
