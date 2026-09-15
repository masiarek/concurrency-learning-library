# SIMD

**Category:** [Parallelism](../README.md) · **Status:** stub

**One line:** One CPU instruction applied to several numbers at once: parallelism inside a single core.

Also called: vectorization, single instruction, multiple data.

## How it connects

```mermaid
flowchart LR
  n_data_parallelism["Data parallelism"]
  n_simd["SIMD"]
  n_simd -->|is a| n_data_parallelism
  classDef center stroke-width:3px
  class n_simd center
  classDef outside stroke-dasharray: 4 3
  class n_data_parallelism outside
```

- **Is a kind of:** [Data parallelism](../data_parallelism/README.md)

## In each language

| | |
|---|---|
| Rust | Platform intrinsics in [`std::arch` ↗](https://doc.rust-lang.org/std/arch/index.html); the portable [`std::simd` ↗](https://doc.rust-lang.org/std/simd/index.html) is nightly-only |
| C++ | [`std::simd` ↗](https://en.cppreference.com/w/cpp/numeric/simd) in C++26, after [`std::experimental::simd` ↗](https://en.cppreference.com/w/cpp/experimental/simd) |
| Java | The [Vector API ↗](https://docs.oracle.com/en/java/javase/25/docs/api/jdk.incubator.vector/jdk/incubator/vector/package-summary.html), still an incubator module in JDK 25 |
| C# | [`Vector<T>` ↗](https://learn.microsoft.com/en-us/dotnet/api/system.numerics.vector-1), which supports hardware acceleration, and the instruction-set register types of [`System.Runtime.Intrinsics` ↗](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.intrinsics) |
| Swift | [`SIMD` ↗](https://developer.apple.com/documentation/swift/simd) vector types such as `SIMD4<Float>` in the standard library |

## Where to read more

- **In the books:** [*Modern Parallel Programming with C++ and Assembly Language*](../../../10_Resources/books_cpp/README.md#kusswurm_modern_parallel_programming_cpp_assembly), Daniel Kusswurm — ch. 1, 'SIMD Fundamentals'
- **In the books:** [*Pro TBB*](../../../10_Resources/books_cpp/README.md#voss_pro_tbb), Michael Voss, Rafael Asenjo, James Reinders — ch. 4, 'TBB and the Parallel Algorithms of the C++ Standard Template Library' → 'Other Ways to Introduce SIMD Parallelism'
- **In the books:** [*Data Parallel C++*](../../../10_Resources/books_cpp/README.md#reinders_data_parallel_cpp), James Reinders, Ben Ashbaugh, James Brodman, Michael Kinsner, John Pennycook, Xinmin Tian — ch. 16, 'Programming for CPUs' → 'The Basics of SIMD Hardware'
- **In the books:** [*Parallel Programming with Intel Parallel Studio XE*](../../../10_Resources/books_cpp/README.md#blair_chappell_intel_parallel_studio_xe), Stephen Blair-Chappell, Andrew Stokes — ch. 4, 'Producing Optimized Code' → 'More on Auto-Vectorization'
- **Reference:** [Wikipedia: Single instruction, multiple data ↗](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
