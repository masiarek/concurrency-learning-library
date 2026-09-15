# False sharing

**Category:** [Hazards](../README.md) · **Status:** stub · **Lessons:** chapter 07, Parallelism *(planned)*

**One line:** Threads writing unrelated variables that happen to sit on the same CPU cache line keep invalidating each other's cache, slowing down with no logical sharing at all.

Also called: cache line contention.

## How it connects


- **See also:** [Cache coherence](../../parallelism/cache_coherence/README.md), [Contention](../contention/README.md), [NUMA](../../parallelism/numa/README.md), [Profiling concurrent programs](../../testing_and_tools/profiling_concurrency/README.md)

## In each language

| | |
|---|---|
| Rust | [`crossbeam_utils::CachePadded` ↗](https://docs.rs/crossbeam-utils/latest/crossbeam_utils/struct.CachePadded.html) pads and aligns a value to the length of a cache line |
| Go | [`cpu.CacheLinePad` ↗](https://pkg.go.dev/golang.org/x/sys/cpu#CacheLinePad) in `golang.org/x/sys` pads structs to avoid false sharing |
| C++ | [`std::hardware_destructive_interference_size` ↗](https://en.cppreference.com/w/cpp/thread/hardware_destructive_interference_size) (C++17): the minimum offset between two objects to avoid false sharing |

## Where to read more

- **In the books:** [*Concurrency with Modern C++*](../../../10_Resources/books_cpp/README.md#grimm_concurrency_with_modern_cpp), Rainer Grimm — ch. 13, 'Challenges' → 'False Sharing'
- **Reference:** [Wikipedia: False sharing ↗](https://en.wikipedia.org/wiki/False_sharing)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
