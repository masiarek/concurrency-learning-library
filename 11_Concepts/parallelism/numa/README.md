# NUMA

**Category:** [Parallelism](../README.md) · **Status:** stub

**One line:** Non-uniform memory access: on a multi-socket machine some memory is closer to some cores, so where a thread runs changes how fast its memory is.

Also called: non-uniform memory access.

## How it connects


- **See also:** [Cache coherence](../cache_coherence/README.md), [False sharing](../../hazards/false_sharing/README.md)

## In each language

| | |
|---|---|
| Java | HotSpot's [`-XX:+UseNUMA` ↗](https://docs.oracle.com/en/java/javase/25/docs/specs/man/java.html) option |
| The operating system | [`numa(7)` ↗](https://man7.org/linux/man-pages/man7/numa.7.html), [`set_mempolicy(2)` ↗](https://man7.org/linux/man-pages/man2/set_mempolicy.2.html), and `numactl` to bind a program to nodes |

## Where to read more

- **In the books:** [*Pro TBB*](../../../10_Resources/books_cpp/README.md#voss_pro_tbb), Michael Voss, Rafael Asenjo, James Reinders — ch. 20, 'TBB on NUMA Architectures'
- **Reference:** [Wikipedia: Non-uniform memory access ↗](https://en.wikipedia.org/wiki/Non-uniform_memory_access)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
