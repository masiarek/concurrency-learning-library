# Why do Python threads take turns?

**Level:** 201 · anyone who used `threading` for speed

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** CPython's global interpreter lock lets one thread run Python bytecode at a time, so eight threads of pure Python compute take as long as one and slightly longer — but a thread releases the lock while it waits for I/O or runs C code, which is why threads still help a downloader, and the free-threaded build (3.13+, `python3.13t`) removes the lock and the ceiling with it.

## The question

Eight threads, each summing a million numbers in a Python loop. Wall time: the same as one thread. Eight threads each sleeping a second: one second, not eight. Eight threads each calling `numpy.sum` — or `hashlib` — on a large array: parallel, because those release the lock. The page measures all three on the ordinary build and on the free-threaded one, as *Real runs*.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | no interpreter lock; the Rust column is the comparison point at 8× |
| Go | no lock; 8× |
| C | no lock; 8× |
| C++ | no lock; 8× |
| Java | no lock; 8× |
| Python | 8 threads of bytecode: 1×; 8 threads of `time.sleep`: 8× overlap; on `python3.13t` the bytecode case becomes near 8× |

## What the programs have to show

- *Real runs*: the three workloads on 1 and 8 threads, on `python3` and `python3.13t` if installed
- `sys._is_gil_enabled()` printed by each interpreter
- the CI example: the sums, equal, and the sleep case's overlap measured with a two-second margin

## See also

- Before this: [How much faster is real work on eight threads?](../cpu_bound_speedup/README.md)
- After this: [Why does the ninth core help less than the second?](../amdahls_law/README.md)
- [How much faster is real work on eight threads?](../cpu_bound_speedup/README.md)
- [When are processes the better workers?](../../08_Processes/multiprocessing_instead_of_threads/README.md)
- Concepts: [Global interpreter lock](../../11_Concepts/parallelism/gil/README.md) · [Parallelism](../../11_Concepts/foundations/parallelism/README.md) · [I/O-bound and CPU-bound work](../../11_Concepts/foundations/io_bound_and_cpu_bound/README.md) · [Multiprocessing](../../11_Concepts/parallelism/multiprocessing/README.md)
