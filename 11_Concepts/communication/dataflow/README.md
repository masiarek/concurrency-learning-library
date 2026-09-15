# Dataflow programming

**Category:** [Communication](../README.md) · **Status:** stub · **Lessons:** chapter 05, Message passing *(planned)*

**One line:** A program as a graph of blocks through which data flows, each block running when its inputs are ready — so the graph, not the programmer, decides what runs in parallel.

Also called: flow graph, TPL Dataflow.

## How it connects


- **See also:** [Pipeline](../pipeline/README.md), [Reactive programming](../../async/reactive_programming/README.md)

## In each language

| | |
|---|---|
| C# | [TPL Dataflow ↗](https://learn.microsoft.com/en-us/dotnet/standard/parallel-programming/dataflow-task-parallel-library): linked blocks that buffer, transform and join messages |
| Haskell | the [`monad-par` ↗](https://hackage.haskell.org/package/monad-par) package's `Par` monad builds a dataflow graph of parallel computations |

## Where to read more

- **In the books:** [*Pro TBB*](../../../10_Resources/books_cpp/README.md#voss_pro_tbb), Michael Voss, Rafael Asenjo, James Reinders — ch. 3, 'Flow Graphs'
- **In the books:** [*Parallel and Concurrent Programming in Haskell*](../../../10_Resources/books_haskell/README.md#marlow_parallel_and_concurrent_programming_in_haskell), Simon Marlow — ch. 4, 'Dataflow Parallelism: The Par Monad'
- **In the books:** [*Parallel Programming and Concurrency with C# 10 and .NET 6*](../../../10_Resources/books_csharp_dotnet/README.md#ashcraft_parallel_programming_concurrency_csharp10), Alvin Ashcraft — ch. 7, 'Task Parallel Library (TPL) and Dataflow'
- **In the books:** [*Concurrency in .NET*](../../../10_Resources/books_csharp_dotnet/README.md#terrell_concurrency_in_dotnet), Riccardo Terrell — ch. 12, 'Parallel workflow and agent programming with TPL Dataflow'
- **In the books:** [*Pro Asynchronous Programming with .NET*](../../../10_Resources/books_csharp_dotnet/README.md#blewett_clymer_pro_asynchronous_programming_dotnet), Richard Blewett, Andrew Clymer — ch. 10, 'TPL Dataflow'
- **In the books:** [*Concurrency in C# Cookbook*](../../../10_Resources/books_csharp_dotnet/README.md#cleary_concurrency_in_csharp_cookbook), Stephen Cleary — ch. 1, 'Concurrency: An Overview' → 'Introduction to Dataflows'
- **Reference:** [Wikipedia: Dataflow programming ↗](https://en.wikipedia.org/wiki/Dataflow_programming)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
