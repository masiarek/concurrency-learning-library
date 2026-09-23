# Speedup and Amdahl's law

**Category:** [Foundations](../README.md) · **Status:** stub · **Lessons:** [chapter 07, Parallelism](../../../07_Parallelism/README.md)

**One line:** How much faster more processors make a program is capped by the part that must still run sequentially: if a tenth of the work is serial, no number of cores gives more than ten times the speed.

Also called: Amdahl's law, Gustafson's law, speedup.

## How it connects


- **See also:** [Granularity](../granularity/README.md), [Parallel algorithms](../../parallelism/parallel_algorithms/README.md), [Parallelism](../parallelism/README.md), [Profiling concurrent programs](../../testing_and_tools/profiling_concurrency/README.md)

## Where to read more

- **In this library:** [How much faster is real work on eight threads?](../../../07_Parallelism/cpu_bound_speedup/README.md)
- **In this library:** [Why does the ninth core help less than the second?](../../../07_Parallelism/amdahls_law/README.md)
- **In the books:** [*The Art of Concurrency*](../../../10_Resources/books_general/README.md#breshears_art_of_concurrency), Clay Breshears — ch. 1, 'Want to Go Faster? Raise Your Hands if You Want to Go Faster!'
- **In the books:** [*Learn Concurrent Programming with Go*](../../../10_Resources/books_go/README.md#cutajar_learn_concurrent_programming_with_go), James Cutajar — ch. 1, 'Stepping into concurrent programming' → 'Increasing throughput'
- **In the books:** [*Hands-On Concurrency with Rust*](../../../10_Resources/books_rust/README.md#troutwine_hands_on_concurrency_with_rust), Brian L. Troutwine — ch. 2, 'Sequential Rust Performance and Testing' → 'Diminishing returns'
- **In the books:** [*Java Concurrency in Practice*](../../../10_Resources/books_java/README.md#goetz_java_concurrency_in_practice), Brian Goetz, Tim Peierls, Joshua Bloch, Joseph Bowbeer, David Holmes, Doug Lea — ch. 11, 'Performance and Scalability' → 'Amdahl’s Law'
- **In the books:** [*Concurrent Programming on Windows*](../../../10_Resources/books_csharp_dotnet/README.md#duffy_concurrent_programming_on_windows), Joe Duffy — ch. 14, 'Performance and Scalability' → 'Speedup: Parallel vs. Sequential Code'
- **In the books:** [*Programming Concurrency on the JVM*](../../../10_Resources/books_java/README.md#subramaniam_programming_concurrency_on_the_jvm), Venkat Subramaniam — ch. 2, 'Division of Labor' → 'Speedup for the IO-Intensive App'
- **Reference:** [Wikipedia: Amdahl's law ↗](https://en.wikipedia.org/wiki/Amdahl%27s_law)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
