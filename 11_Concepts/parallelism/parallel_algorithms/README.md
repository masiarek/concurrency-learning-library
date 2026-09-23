# Parallel algorithms

**Category:** [Parallelism](../README.md) · **Status:** stub · **Lessons:** [chapter 07, Parallelism](../../../07_Parallelism/README.md)

**One line:** Sorting, searching, graph and numeric algorithms rebuilt so that their work splits across cores — not always by the obvious split.

Also called: parallel sort, parallel search.

## How it connects


- **See also:** [Data parallelism](../data_parallelism/README.md), [Fork-join](../fork_join/README.md), [Speedup and Amdahl's law](../../foundations/speedup_and_amdahls_law/README.md)

## In each language

| | |
|---|---|
| Rust | Rayon's [`par_sort` ↗](https://docs.rs/rayon/latest/rayon/slice/trait.ParallelSliceMut.html) and the other parallel slice methods |
| C++ | the standard algorithms with an [execution policy ↗](https://en.cppreference.com/w/cpp/algorithm/execution_policy_tag_t) (C++17), such as `std::sort(std::execution::par, ...)` |
| Java | [`Arrays.parallelSort` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Arrays.html) |

## Where to read more

- **In this library:** [Splitting a sum across workers](../../../07_Parallelism/splitting_a_sum_across_workers/README.md)
- **In this library:** [Can a for loop be made parallel by changing one word?](../../../07_Parallelism/a_parallel_iterator/README.md)
- **In this library:** [Why is a reduction the hard half of a parallel map?](../../../07_Parallelism/map_and_reduce/README.md)
- **In the books:** [*An Introduction to Parallel Programming*](../../../10_Resources/books_general/README.md#pacheco_malensek_introduction_to_parallel_programming), Peter S. Pacheco, Matthew Malensek — ch. 1, 'Why parallel computing'
- **In the books:** [*C++ Concurrency in Action*](../../../10_Resources/books_cpp/README.md#williams_cpp_concurrency_in_action), Anthony Williams — ch. 10, 'Parallel algorithms'
- **In the books:** [*Pro TBB*](../../../10_Resources/books_cpp/README.md#voss_pro_tbb), Michael Voss, Rafael Asenjo, James Reinders — ch. 2, 'Generic Parallel Algorithms'
- **In the books:** [*Concurrency with Modern C++*](../../../10_Resources/books_cpp/README.md#grimm_concurrency_with_modern_cpp), Rainer Grimm — ch. 1, 'Concurrency with Modern C++' → 'C++17: Parallel Algorithms of the Standard Template Library'
- **In the books:** [*Introduction to Algorithms*](../../../10_Resources/books_general/README.md#cormen_introduction_to_algorithms), Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein — ch. 26, 'Parallel Algorithms'
- **In the books:** [*The Art of Multiprocessor Programming*](../../../10_Resources/books_general/README.md#herlihy_shavit_art_of_multiprocessor_programming), Maurice Herlihy, Nir Shavit — ch. 12, 'Counting, Sorting, and Distributed Coordination' → 'Sorting Networks'
- **In the books:** [*Parallel Programming with Python*](../../../10_Resources/books_python/README.md#palach_parallel_programming_with_python), Jan Palach — ch. 2, 'Designing Parallel Algorithms'
- **Reference:** [Wikipedia: Parallel algorithm ↗](https://en.wikipedia.org/wiki/Parallel_algorithm)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
