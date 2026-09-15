# Oversubscription

**Category:** [Foundations](../README.md) · **Status:** stub

**One line:** More busy threads than there are cores, so the machine spends its time switching between them instead of running them.

## How it connects

```mermaid
flowchart LR
  n_contention["Contention"]
  n_oversubscription["Oversubscription"]
  n_oversubscription -->|can cause| n_contention
  classDef center stroke-width:3px
  class n_oversubscription center
  classDef outside stroke-dasharray: 4 3
  class n_contention outside
```

- **Can lead to:** [Contention](../../hazards/contention/README.md)
- **See also:** [Context switch](../../units_of_execution/context_switch/README.md), [Granularity](../granularity/README.md), [Thread pool and executor](../../units_of_execution/thread_pool/README.md)

## In each language

| | |
|---|---|
| Rust | [`available_parallelism` ↗](https://doc.rust-lang.org/std/thread/fn.available_parallelism.html) estimates how many threads a program should use |
| Go | [`runtime.GOMAXPROCS` ↗](https://pkg.go.dev/runtime#GOMAXPROCS) caps how many CPUs execute Go code simultaneously, however many goroutines there are |
| C++ | [`std::thread::hardware_concurrency` ↗](https://en.cppreference.com/w/cpp/thread/thread/hardware_concurrency) is only a hint, and may be 0 |
| Python | [`os.process_cpu_count` ↗](https://docs.python.org/3/library/os.html#os.process_cpu_count) (3.13) counts the logical CPUs the calling thread may use, and [`ThreadPoolExecutor` ↗](https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor) sizes its default pool from it |
| JavaScript | [`navigator.hardwareConcurrency` ↗](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/hardwareConcurrency) is the number of logical processors available to run threads |
| Kotlin | [`Dispatchers.Default` ↗](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-dispatchers/-default.html) uses at most as many threads as there are CPU cores, and at least two |
| The operating system | [`sched_getaffinity` ↗](https://man7.org/linux/man-pages/man2/sched_setaffinity.2.html) gives the CPUs a thread may run on, which can be fewer than the machine has |

## Where to read more

- **In the books:** [*Pro TBB*](../../../10_Resources/books_cpp/README.md#voss_pro_tbb), Michael Voss, Rafael Asenjo, James Reinders — ch. 11, 'Controlling the Number of Threads Used for Execution'
- **In the books:** [*C++ Concurrency in Action*](../../../10_Resources/books_cpp/README.md#williams_cpp_concurrency_in_action), Anthony Williams — ch. 2, 'Managing threads' → 'Choosing the number of threads at runtime'
- **In the books:** [*Functional and Concurrent Programming*](../../../10_Resources/books_scala_jvm_functional/README.md#charpentier_functional_and_concurrent_programming), Michel Charpentier — ch. 24, 'Case Study: Parallel Execution' → 'Bounded Number of Threads'
- **Notes:** [oversubscription ↗](https://docs.google.com/document/d/1LjySDlE4JbkjDYmGxU3WjZC73oABCtMp2B4oiyNw8yk/edit?tab=t.0)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
