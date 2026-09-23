# Why are eight threads writing eight different variables slow?

**Level:** 201 · anyone whose per-thread counters were slower than one shared one

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** Eight threads each writing their own element of one array are writing to the same 64-byte cache line, and the CPU moves that line between the cores on every write — *false sharing* — so that eight independent counters run slower than a single locked one; padding each counter to its own line, or keeping it in a local and writing it once, gives the expected speedup.

## The question

`counts[i] += 1` a hundred million times per thread, thread *i* owning `counts[i]`. No data race — each thread has its own slot. Eight threads take longer than one. Pad each slot to 64 bytes and eight threads take an eighth of the time. The page measures both as *Real runs* and shows the padding in each language, plus the version that needs none: a local accumulator written back once.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `#[repr(align(64))]` on the slot type; `crossbeam::CachePadded` names the fix (link) |
| Go | a struct with `_ [56]byte` padding, as the runtime's own source does |
| C | `_Alignas(64)` on the slot |
| C++ | `alignas(std::hardware_destructive_interference_size)` |
| Java | `@Contended` with `-XX:-RestrictContended`; or the local-accumulator fix |
| Python | not reachable under the GIL; the local-accumulator shape is the only lesson |

## What the programs have to show

- *Real runs*: eight threads on adjacent slots against padded slots, time per language
- the local accumulator written back once, which is [Splitting a sum](../splitting_a_sum_across_workers/README.md)'s private partial sum
- the CI example: the counts, identical either way

## See also

- Before this: [Why does the ninth core help less than the second?](../amdahls_law/README.md)
- After this: [Same work on different data, or different work at once?](../data_parallel_or_task_parallel/README.md)
- [Splitting a sum across workers](../splitting_a_sum_across_workers/README.md)
- [How much faster is real work on eight threads?](../cpu_bound_speedup/README.md)
- Concepts: [False sharing](../../11_Concepts/hazards/false_sharing/README.md) · [Cache coherence](../../11_Concepts/parallelism/cache_coherence/README.md) · [Contention](../../11_Concepts/hazards/contention/README.md) · [Data parallelism](../../11_Concepts/parallelism/data_parallelism/README.md)
