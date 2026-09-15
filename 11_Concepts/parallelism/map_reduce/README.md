# Map-reduce

**Category:** [Parallelism](../README.md) · **Status:** stub · **Lessons:** chapter 07, Parallelism *(planned)*

**One line:** Apply a function to every item independently, then combine the results with an associative operation, so that both halves can be split across workers.

Also called: MapReduce.

## How it connects

```mermaid
flowchart LR
  n_data_parallelism["Data parallelism"]
  n_map_reduce["Map-reduce"]
  n_map_reduce -->|is a| n_data_parallelism
  classDef center stroke-width:3px
  class n_map_reduce center
  classDef outside stroke-dasharray: 4 3
  class n_data_parallelism outside
```

- **Is a kind of:** [Data parallelism](../data_parallelism/README.md)
- **See also:** [Fork-join](../fork_join/README.md)

## In each language

| | |
|---|---|
| Rust | Rayon's [`reduce` ↗](https://docs.rs/rayon/latest/rayon/iter/trait.ParallelIterator.html#method.reduce) takes an identity value as well as the combining operation |
| C++ | [`std::transform_reduce` ↗](https://en.cppreference.com/w/cpp/algorithm/transform_reduce); with a non-associative or non-commutative operation the result is non-deterministic |
| Java | [`Stream.reduce` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html) requires an associative accumulator, so that a parallel stream can split the work |
| Elsewhere | [Hadoop MapReduce ↗](https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html) runs the same split across a cluster |

## Where to read more

- **In the books:** [*Concurrency in .NET*](../../../10_Resources/books_csharp_dotnet/README.md#terrell_concurrency_in_dotnet), Riccardo Terrell — ch. 5, 'PLINQ and MapReduce: data parallelism, part 2'
- **In the books:** [*The Art of Concurrency*](../../../10_Resources/books_general/README.md#breshears_art_of_concurrency), Clay Breshears — ch. 7, 'MapReduce'
- **In the books:** [*Python Concurrency with asyncio*](../../../10_Resources/books_python/README.md#fowler_python_concurrency_with_asyncio), Matthew Fowler — ch. 6, 'Handling CPU-bound work' → 'Solving a problem with MapReduce using asyncio'
- **In the books:** [*Python Parallel Programming Cookbook*](../../../10_Resources/books_python/README.md#zaccone_python_parallel_programming_cookbook), Giancarlo Zaccone — ch. 5, 'Distributed Python' → 'Using MapReduce with Disco'
- **In the books:** [*Seven Concurrency Models in Seven Weeks*](../../../10_Resources/books_general/README.md#butcher_seven_concurrency_models), Paul Butcher — ch. 8, 'The Lambda Architecture' → 'Day 1: MapReduce'
- **In the books:** [*The Go Programming Language Phrasebook*](../../../10_Resources/books_go/README.md#chisnall_go_phrasebook), David Chisnall — ch. 10, 'Concurrency Design Patterns' → 'Map Reduce, Go Style'
- **Reference:** [Wikipedia: MapReduce ↗](https://en.wikipedia.org/wiki/MapReduce)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
