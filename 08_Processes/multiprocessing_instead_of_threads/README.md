# When are processes the better workers?

**Level:** 201 · anyone choosing between threads and processes

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A process shares nothing by default, which costs a copy for every value that crosses and buys three things threads cannot: a crash that takes only itself, a memory that another worker cannot corrupt, and — in Python — a way past the interpreter lock; the price is that every argument and every result is serialized on the way through.

## The question

The CPU-bound sum from chapter 07, once more, on eight processes instead of eight threads. In Python it is the first version that is actually eight times faster. In the other languages it is the same speed as threads and the results took a serialization round trip. The page measures both, as *Real runs*, then shows the two things processes buy everywhere: one worker crashing with the others unharmed, and a worker that cannot see the others' memory.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `std::process::Command` per worker with the work described on stdin and the result on stdout |
| Go | `os/exec` per worker; the same |
| C | `fork` per worker, the result through a pipe or a `wait` status |
| C++ | the same as C |
| Java | `ProcessBuilder` per worker |
| Python | `multiprocessing.Pool(8).map(f, chunks)`: 8× under the GIL, with pickling on both ends |

## What the programs have to show

- eight processes summing eight chunks: the total, and a *Real runs* fence beside the thread version's time
- one worker calling `abort()`: the other seven finish and the parent reports one failure
- the argument that does not pickle, in Python, and its error

## See also

- Before this: [Which thread gets the signal?](../a_signal_arrives_on_some_thread/README.md)
- After this: [Can two processes share a variable after all?](../shared_memory_between_processes/README.md)
- [Why do Python threads take turns?](../../07_Parallelism/the_gil_and_free_threaded_python/README.md)
- [Can two processes share a variable after all?](../shared_memory_between_processes/README.md)
- Concepts: [Multiprocessing](../../11_Concepts/parallelism/multiprocessing/README.md) · [Process](../../11_Concepts/units_of_execution/process/README.md) · [Global interpreter lock](../../11_Concepts/parallelism/gil/README.md) · [Inter-process communication](../../11_Concepts/communication/ipc/README.md) · [Partial failure](../../11_Concepts/distributed/partial_failure/README.md)
