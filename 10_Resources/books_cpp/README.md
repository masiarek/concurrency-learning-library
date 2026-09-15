# Concurrency books — C++

[All book lists](../README.md#books) · [Concepts](../../11_Concepts/README.md)

<a id="kusswurm_modern_parallel_programming_cpp_assembly"></a>

## *Modern Parallel Programming with C++ and Assembly Language*: X86 SIMD Development Using AVX, AVX2, and AVX-512

Daniel Kusswurm · 1st edition · Apress · 2022  
dedicated to concurrency · on the shelf · [publisher ↗](https://link.springer.com/book/10.1007/978-1-4842-7918-2) · [example code ↗](https://github.com/Apress/modern-parallel-programming-cpp-assembly)

<details markdown="1">
<summary>Chapters</summary>

- **1** SIMD Fundamentals
- **2** AVX C++ Programming: Part 1
- **3** AVX C++ Programming: Part 2
- **4** AVX2 C++ Programming: Part 1
- **5** AVX2 C++ Programming: Part 2
- **6** AVX2 C++ Programming: Part 3
- **7** AVX-512 C++ Programming: Part 1
- **8** AVX-512 C++ Programming: Part 2
- **9** Supplemental C++ SIMD Programming
- **10** X86-64 Processor Architecture
- **11** Core Assembly Language Programming: Part 1
- **12** Core Assembly Language Programming: Part 2
- **13** AVX Assembly Language Programming: Part 1
- **14** AVX Assembly Language Programming: Part 2
- **15** AVX2 Assembly Language Programming: Part 1
- **16** AVX2 Assembly Language Programming: Part 2
- **17** AVX-512 Assembly Language Programming: Part 1
- **18** AVX-512 Assembly Language Programming: Part 2
- **19** SIMD Usage and Optimization Guidelines

</details>

Cited on: [SIMD](../../11_Concepts/parallelism/simd/README.md)

<a id="reinders_data_parallel_cpp"></a>

## *Data Parallel C++*: Mastering DPC++ for Programming of Heterogeneous Systems using C++ and SYCL

James Reinders, Ben Ashbaugh, James Brodman, Michael Kinsner, John Pennycook, Xinmin Tian · 1st edition · Apress · 2021  
dedicated to concurrency · on the shelf · [publisher ↗](https://link.springer.com/book/10.1007/978-1-4842-5574-2) · [example code ↗](https://github.com/Apress/data-parallel-CPP)

<details markdown="1">
<summary>Chapters</summary>

- **1** Introduction
- **2** Where Code Executes
- **3** Data Management
- **4** Expressing Parallelism
- **5** Error Handling
- **6** Unified Shared Memory
- **7** Buffers
- **8** Scheduling Kernels and Data Movement
- **9** Communication and Synchronization
- **10** Defining Kernels
- **11** Vectors
- **12** Device Information
- **13** Practical Tips
- **14** Common Parallel Patterns
- **15** Programming for GPUs
- **16** Programming for CPUs
- **17** Programming for FPGAs
- **18** Libraries
- **19** Memory Model and Atomics

</details>

Cited on: [Barrier](../../11_Concepts/synchronization/barrier/README.md), [Data parallelism](../../11_Concepts/parallelism/data_parallelism/README.md), [GPU computing](../../11_Concepts/parallelism/gpu_computing/README.md), [SIMD](../../11_Concepts/parallelism/simd/README.md)

<a id="williams_cpp_concurrency_in_action"></a>

## *C++ Concurrency in Action*

Anthony Williams · 2nd edition · Manning Publications · 2019  
dedicated to concurrency · on the shelf · [publisher ↗](https://www.manning.com/books/c-plus-plus-concurrency-in-action-second-edition) · [example code ↗](https://github.com/anthonywilliams/ccia_code_samples)

<details markdown="1">
<summary>Chapters</summary>

- **1** Hello, world of concurrency in C++!
- **2** Managing threads
- **3** Sharing data between threads
- **4** Synchronizing concurrent operations
- **5** The C++ memory model and operations on atomic types
- **6** Designing lock-based concurrent data structures
- **7** Designing lock-free concurrent data structures
- **8** Designing concurrent code
- **9** Advanced thread management
- **10** Parallel algorithms
- **11** Testing and debugging multithreaded applications
- Brief comparison of concurrency libraries
- **C** A message-passing framework and complete ATM example
- **D** C++ Thread Library reference

</details>

Cited on: [Atomic variable](../../11_Concepts/lock_free/atomic_variable/README.md), [Concurrency](../../11_Concepts/foundations/concurrency/README.md), [Concurrent data structures](../../11_Concepts/lock_free/concurrent_data_structures/README.md), [Data parallelism](../../11_Concepts/parallelism/data_parallelism/README.md), [Debugging concurrent programs](../../11_Concepts/testing_and_tools/concurrency_debugging/README.md), [Future and promise](../../11_Concepts/async/future_and_promise/README.md), [Lock-free](../../11_Concepts/lock_free/lock_free/README.md), [Oversubscription](../../11_Concepts/foundations/oversubscription/README.md), [Parallel algorithms](../../11_Concepts/parallelism/parallel_algorithms/README.md), [Profiling concurrent programs](../../11_Concepts/testing_and_tools/profiling_concurrency/README.md), [Shared memory](../../11_Concepts/communication/shared_memory/README.md), [Thread](../../11_Concepts/units_of_execution/thread/README.md), [Thread pool and executor](../../11_Concepts/units_of_execution/thread_pool/README.md), [Timeout](../../11_Concepts/async/timeout/README.md), [Weak memory models and reordering](../../11_Concepts/hazards/weak_memory_model/README.md)

<a id="grimm_concurrency_with_modern_cpp"></a>

## *Concurrency with Modern C++*

Rainer Grimm · Leanpub version of 2019-03-19 edition · Leanpub (self-published) · 2019  
dedicated to concurrency · on the shelf · [publisher ↗](https://leanpub.com/concurrencywithmodernc)

<details markdown="1">
<summary>Chapters</summary>

- **1** Concurrency with Modern C++
- **2** Memory Model
- **3** Multithreading
- **4** Parallel Algorithms of the Standard Template Library
- **5** Case Studies
- **6** The Future: C++20/23
- **7** Patterns and Best Practices
- **8** Synchronisation Patterns
- **9** Concurrent Architecture
- **10** Best Practices
- **11** Lock-Based Data Structures
- **12** Lock-Free Data Structures
- **13** Challenges
- **14** The Time Library
- **15** CppMem - An Overview

</details>

Cited on: [ABA problem](../../11_Concepts/hazards/aba_problem/README.md), [Barrier](../../11_Concepts/synchronization/barrier/README.md), [Concurrent data structures](../../11_Concepts/lock_free/concurrent_data_structures/README.md), [Condition variable](../../11_Concepts/synchronization/condition_variable/README.md), [Coroutine](../../11_Concepts/units_of_execution/coroutine/README.md), [Data race](../../11_Concepts/hazards/data_race/README.md), [Deadlock](../../11_Concepts/hazards/deadlock/README.md), [False sharing](../../11_Concepts/hazards/false_sharing/README.md), [Join](../../11_Concepts/async/join/README.md), [Latch](../../11_Concepts/synchronization/latch/README.md), [Monitor](../../11_Concepts/synchronization/monitor/README.md), [Parallel algorithms](../../11_Concepts/parallelism/parallel_algorithms/README.md), [Race condition](../../11_Concepts/hazards/race_condition/README.md), [Task (async)](../../11_Concepts/units_of_execution/async_task/README.md), [Thread safety](../../11_Concepts/safety_in_languages/thread_safety/README.md), [Thread-local storage](../../11_Concepts/units_of_execution/thread_local_storage/README.md), [Transactional memory](../../11_Concepts/lock_free/transactional_memory/README.md)

<a id="voss_pro_tbb"></a>

## *Pro TBB*: C++ Parallel Programming with Threading Building Blocks

Michael Voss, Rafael Asenjo, James Reinders · 1st edition · Apress · 2019  
dedicated to concurrency · on the shelf · [publisher ↗](https://link.springer.com/book/10.1007/978-1-4842-4398-5) · [example code ↗](https://github.com/Apress/pro-TBB)

<details markdown="1">
<summary>Chapters</summary>

- **1** Jumping Right In: “Hello, TBB!”
- **2** Generic Parallel Algorithms
- **3** Flow Graphs
- **4** TBB and the Parallel Algorithms of the C++ Standard Template Library
- **5** Synchronization: Why and How to Avoid It
- **6** Data Structures for Concurrency
- **7** Scalable Memory Allocation
- **8** Mapping Parallel Patterns to TBB
- **9** The Pillars of Composability
- **10** Using Tasks to Create Your Own Algorithms
- **11** Controlling the Number of Threads Used for Execution
- **12** Using Work Isolation for Correctness and Performance
- **13** Creating Thread-to-Core and Task-to-Thread Affinity
- **14** Using Task Priorities
- **15** Cancellation and Exception Handling
- **16** Tuning TBB Algorithms: Granularity, Locality, Parallelism, and Determinism
- **17** Flow Graphs: Beyond the Basics
- **18** Beef Up Flow Graphs with Async Nodes
- **19** Flow Graphs on Steroids: OpenCL Nodes
- **20** TBB on NUMA Architectures

</details>

Cited on: [Cancellation](../../11_Concepts/async/cancellation/README.md), [Cooperative scheduling](../../11_Concepts/scheduling/cooperative_scheduling/README.md), [Dataflow programming](../../11_Concepts/communication/dataflow/README.md), [Fork-join](../../11_Concepts/parallelism/fork_join/README.md), [GPU computing](../../11_Concepts/parallelism/gpu_computing/README.md), [Granularity](../../11_Concepts/foundations/granularity/README.md), [NUMA](../../11_Concepts/parallelism/numa/README.md), [Oversubscription](../../11_Concepts/foundations/oversubscription/README.md), [Parallel algorithms](../../11_Concepts/parallelism/parallel_algorithms/README.md), [Pipeline](../../11_Concepts/communication/pipeline/README.md), [Preemptive scheduling](../../11_Concepts/scheduling/preemptive_scheduling/README.md), [Scheduler](../../11_Concepts/scheduling/scheduler/README.md), [SIMD](../../11_Concepts/parallelism/simd/README.md), [Task parallelism](../../11_Concepts/parallelism/task_parallelism/README.md), [Thread confinement](../../11_Concepts/safety_in_languages/thread_confinement/README.md)

<a id="pai_abraham_cpp_reactive_programming"></a>

## *C++ Reactive Programming*: Design concurrent and asynchronous applications using the RxCpp library and Modern C++17

Praseed Pai, Peter Abraham · 1st edition · Packt Publishing · 2018  
dedicated to concurrency · on the shelf · [example code ↗](https://github.com/PacktPublishing/CPP-Reactive-Programming)

<details markdown="1">
<summary>Chapters</summary>

- **1** Reactive Programming Model – Overview and History
- **2** A Tour of Modern C++ and its Key Idioms
- **3** Language-Level Concurrency and Parallelism in C++
- **4** Asynchronous and Lock-Free Programming in C++
- **5** Introduction to Observables
- **6** Introduction to Event Stream Programming Using C++
- **7** Introduction to Data Flow Computation and the RxCpp Library
- **8** RxCpp – the Key Elements
- **9** Reactive GUI Programming Using Qt/C++
- **10** Creating Custom Operators in RxCpp
- **11** Design Patterns and Idioms for C++ Rx Programming
- **12** Reactive Microservices Using C++
- **13** Advanced Streams and Handling Errors

</details>

Cited on: [Async stream](../../11_Concepts/async/async_stream/README.md), [Event-driven programming](../../11_Concepts/async/event_driven_programming/README.md), [Publish-subscribe and broadcast](../../11_Concepts/communication/publish_subscribe/README.md), [Reactive programming](../../11_Concepts/async/reactive_programming/README.md), [Task (async)](../../11_Concepts/units_of_execution/async_task/README.md), [UI thread](../../11_Concepts/units_of_execution/ui_thread/README.md)

<a id="posch_mastering_cpp_multithreading"></a>

## *Mastering C++ Multithreading*: Write robust, concurrent, and parallel applications

Maya Posch · 1st edition · Packt Publishing · 2017  
dedicated to concurrency · on the shelf · [example code ↗](https://github.com/PacktPublishing/Mastering-CPP-Multithreading)

<details markdown="1">
<summary>Chapters</summary>

- **1** Revisiting Multithreading
- **2** Multithreading Implementation on the Processor and OS
- **3** C++ Multithreading APIs
- **4** Thread Synchronization and Communication
- **5** Native C++ Threads and Primitives
- **6** Debugging Multithreaded Code
- **7** Best Practices
- **8** Atomic Operations - Working with the Hardware
- **9** Multithreading with Distributed Computing
- **10** Multithreading with GPGPU

</details>

Cited on: [Data race](../../11_Concepts/hazards/data_race/README.md), [Debugging concurrent programs](../../11_Concepts/testing_and_tools/concurrency_debugging/README.md), [GPU computing](../../11_Concepts/parallelism/gpu_computing/README.md), [MPI](../../11_Concepts/parallelism/mpi/README.md), [Mutual exclusion](../../11_Concepts/synchronization/mutual_exclusion/README.md), [Process](../../11_Concepts/units_of_execution/process/README.md)

<a id="blair_chappell_intel_parallel_studio_xe"></a>

## *Parallel Programming with Intel Parallel Studio XE*

Stephen Blair-Chappell, Andrew Stokes · 1st edition · John Wiley & Sons (Wrox) · 2012  
dedicated to concurrency · on the shelf · [publisher ↗](https://www.wiley.com/en-us/Parallel+Programming+with+Intel+Parallel+Studio+XE-p-9780470891650)

<details markdown="1">
<summary>Chapters</summary>

- **1** Parallelism Today
- **2** An Overview of Parallel Studio XE
- **3** Parallel Studio XE for the Impatient
- **4** Producing Optimized Code
- **5** Writing Secure Code
- **6** Where to Parallelize
- **7** Implementing Parallelism
- **8** Checking for Errors
- **9** Tuning Parallel Applications
- **10** Parallel Advisor–Driven Design
- **11** Debugging Parallel Applications
- **12** Event-Based Analysis with VTune Amplifier XE
- **13** The World’s First Sudoku “Thirty-Niner”
- **14** Nine Tips to Parallel-Programming Heaven
- **15** Parallel Track Fitting in the CERN Collider
- **16** Parallelizing Legacy Code

</details>

Cited on: [Data race](../../11_Concepts/hazards/data_race/README.md), [OpenMP](../../11_Concepts/parallelism/openmp/README.md), [Parallelism](../../11_Concepts/foundations/parallelism/README.md), [SIMD](../../11_Concepts/parallelism/simd/README.md)

<a id="walmsley_multithreaded_programming_in_cpp"></a>

## *Multi-Threaded Programming in C++*

Mark Walmsley · 1st edition · Springer-Verlag London · 2000  
dedicated to concurrency · on the shelf · [publisher ↗](https://link.springer.com/book/10.1007/978-1-4471-0725-5)

<details markdown="1">
<summary>Chapters</summary>

- **1** Introduction
- **2** Threads
- **3** Mutexes
- **4** Events
- **5** Semaphores
- **6** Objects
- **7** Keys
- **8** Multiple Mutexes
- **9** Multiple Events
- **10** Distributed Computing

</details>

Cited on: [Channel](../../11_Concepts/communication/channel/README.md), [Lock ordering](../../11_Concepts/synchronization/lock_ordering/README.md), [Multiprocessing](../../11_Concepts/parallelism/multiprocessing/README.md), [Mutex](../../11_Concepts/synchronization/mutex/README.md), [Reentrant lock](../../11_Concepts/synchronization/reentrant_lock/README.md), [Run-once initialization](../../11_Concepts/synchronization/once_initialization/README.md), [Semaphore](../../11_Concepts/synchronization/semaphore/README.md), [Sequential execution](../../11_Concepts/foundations/sequential_execution/README.md), [Thread-local storage](../../11_Concepts/units_of_execution/thread_local_storage/README.md)

<a id="fertig_programming_with_cpp20"></a>

## *Programming with C++20*: Concepts, Coroutines, Ranges, and more

Andreas Fertig · 1st edition · Fertig Publications · 2021  
a concurrency chapter in a broader book · on the shelf · [publisher ↗](https://leanpub.com/programming-with-cpp20) · [example code ↗](https://github.com/andreasfertig/programming-with-cpp20)

<details markdown="1">
<summary>The concurrency chapters</summary>

- **2** Coroutines: Suspending functions

</details>

Cited on: [Suspension point](../../11_Concepts/scheduling/suspension_point/README.md)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
