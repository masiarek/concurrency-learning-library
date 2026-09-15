# GPU computing

**Category:** [Parallelism](../README.md) · **Status:** stub

**One line:** Running thousands of small data-parallel computations on a graphics processor instead of the CPU.

Also called: GPGPU, CUDA.

## How it connects

```mermaid
flowchart LR
  n_data_parallelism["Data parallelism"]
  n_gpu_computing["GPU computing"]
  n_gpu_computing -->|is a| n_data_parallelism
  classDef center stroke-width:3px
  class n_gpu_computing center
  classDef outside stroke-dasharray: 4 3
  class n_data_parallelism outside
```

- **Is a kind of:** [Data parallelism](../data_parallelism/README.md)

## In each language

| | |
|---|---|
| JavaScript | Compute shaders in the [WebGPU API ↗](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API) |
| Swift | [Metal ↗](https://developer.apple.com/documentation/metal) compute pipelines |
| Elsewhere | NVIDIA's [CUDA ↗](https://docs.nvidia.com/cuda/) toolkit |

## Where to read more

- **In the books:** [*Pro TBB*](../../../10_Resources/books_cpp/README.md#voss_pro_tbb), Michael Voss, Rafael Asenjo, James Reinders — ch. 19, 'Flow Graphs on Steroids: OpenCL Nodes'
- **In the books:** [*Parallel and Concurrent Programming in Haskell*](../../../10_Resources/books_haskell/README.md#marlow_parallel_and_concurrent_programming_in_haskell), Simon Marlow — ch. 6, 'GPU Programming with Accelerate'
- **In the books:** [*Python Parallel Programming Cookbook*](../../../10_Resources/books_python/README.md#zaccone_python_parallel_programming_cookbook), Giancarlo Zaccone — ch. 6, 'GPU Programming with Python'
- **In the books:** [*Mastering C++ Multithreading*](../../../10_Resources/books_cpp/README.md#posch_mastering_cpp_multithreading), Maya Posch — ch. 10, 'Multithreading with GPGPU'
- **In the books:** [*Seven Concurrency Models in Seven Weeks*](../../../10_Resources/books_general/README.md#butcher_seven_concurrency_models), Paul Butcher — ch. 7, 'Data Parallelism' → 'Day 1: GPGPU Programming'
- **In the books:** [*Data Parallel C++*](../../../10_Resources/books_cpp/README.md#reinders_data_parallel_cpp), James Reinders, Ben Ashbaugh, James Brodman, Michael Kinsner, John Pennycook, Xinmin Tian — ch. 2, 'Where Code Executes' → 'Method#3: Using a GPU (or Other Accelerators)'
- **In the books:** [*An Introduction to Parallel Programming*](../../../10_Resources/books_general/README.md#pacheco_malensek_introduction_to_parallel_programming), Peter S. Pacheco, Matthew Malensek — ch. 6, 'GPU programming with CUDA'
- **Reference:** [Wikipedia: General-purpose computing on graphics processing units ↗](https://en.wikipedia.org/wiki/General-purpose_computing_on_graphics_processing_units)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
