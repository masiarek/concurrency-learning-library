# Where does a concurrent program spend its time?

**Level:** 201 · anyone whose parallel program is slower than expected

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A profile of a concurrent program has to answer a question a sequential profile does not — not *which function* but *which thread was doing what, and which were waiting for whom* — and the tools split accordingly: a CPU profiler shows the hot function, a tracer shows the threads over time, and the second is where the lock contention and the idle cores are visible.

## The question

The eight-worker sum from chapter 07 with a lock around the total. The CPU profile says the time is in `lock`. The trace says seven threads waited while one held it, all run long. The page takes that program through each language's CPU profiler and tracer, as *Real runs*, and points at the line in each output that says *contention* — then removes the lock and shows the trace change.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `perf` or `samply` for CPU (link, not run); `tokio-console` for async (link) |
| Go | `pprof` for CPU and the `runtime/trace` viewer for goroutines over time, both in the standard toolchain |
| C | `perf record` and `perf report`; `perf trace` for the waits |
| C++ | the same as C |
| Java | JFR (`-XX:StartFlightRecording`) with `jfr print --events ThreadPark,JavaMonitorEnter` |
| Python | `cProfile` is per thread; `py-spy record` sees all threads and the GIL |

## What the programs have to show

- *Real runs*: the CPU profile's top entry and the tracer's contention view for the locked sum, per language
- the same after removing the lock: the trace's parallel bars
- the CI example: the program itself, with the same total either way

## See also

- Before this: [How do you read a thread dump?](../reading_a_thread_dump/README.md)
- After this: [Why did the bug disappear when you added a print?](../a_heisenbug/README.md)
- [How much faster is real work on eight threads?](../../07_Parallelism/cpu_bound_speedup/README.md)
- [How do you read a thread dump?](../reading_a_thread_dump/README.md)
- The Rust library's [Instrumenting async code ↗](https://masiarek.github.io/rust-learning-library/21_Observability/instrumenting_async/index.html)
- The Rust library's [Diagnosing a stuck runtime ↗](https://masiarek.github.io/rust-learning-library/35_Async/building_minidb/diagnosing_a_stuck_runtime/index.html)
- Concepts: [Profiling concurrent programs](../../11_Concepts/testing_and_tools/profiling_concurrency/README.md) · [Contention](../../11_Concepts/hazards/contention/README.md) · [Debugging concurrent programs](../../11_Concepts/testing_and_tools/concurrency_debugging/README.md) · [Granularity](../../11_Concepts/foundations/granularity/README.md)
