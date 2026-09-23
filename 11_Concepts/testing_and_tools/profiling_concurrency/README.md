# Profiling concurrent programs

**Category:** [Testing and tools](../README.md) · **Status:** stub · **Lessons:** [chapter 09, Testing and tools](../../../09_Testing_and_Tools/README.md)

**One line:** Measuring where the time goes when many threads run — waiting for locks, waiting to be scheduled, and bouncing cache lines — and not only which functions are hot.

Also called: performance tuning, contention profiling, mutex profile.

## How it connects


- **See also:** [Contention](../../hazards/contention/README.md), [False sharing](../../hazards/false_sharing/README.md), [Speedup and Amdahl's law](../../foundations/speedup_and_amdahls_law/README.md)

## In each language

| | |
|---|---|
| Go | [`runtime/pprof` ↗](https://pkg.go.dev/runtime/pprof) has `block` and `mutex` profiles beside the CPU profile |
| Java | [JDK Flight Recorder ↗](https://docs.oracle.com/en/java/javase/25/docs/api/jdk.jfr/jdk/jfr/package-summary.html) records events such as lock contention from a running JVM |
| The operating system | [`perf` ↗](https://man7.org/linux/man-pages/man1/perf.1.html) samples CPU time across every thread and the kernel |

## Where to read more

- **In this library:** [Where does a concurrent program spend its time?](../../../09_Testing_and_Tools/profiling_where_the_time_goes/README.md)
- **In this library:** [Why did the bug disappear when you added a print?](../../../09_Testing_and_Tools/a_heisenbug/README.md)
- **In the books:** [*Java Concurrency in Practice*](../../../10_Resources/books_java/README.md#goetz_java_concurrency_in_practice), Brian Goetz, Tim Peierls, Joshua Bloch, Joseph Bowbeer, David Holmes, Doug Lea — ch. 11, 'Performance and Scalability'
- **In the books:** [*Concurrent Programming on Windows*](../../../10_Resources/books_csharp_dotnet/README.md#duffy_concurrent_programming_on_windows), Joe Duffy — ch. 14, 'Performance and Scalability'
- **In the books:** [*C++ Concurrency in Action*](../../../10_Resources/books_cpp/README.md#williams_cpp_concurrency_in_action), Anthony Williams — ch. 8, 'Designing concurrent code' → 'Factors affecting the performance of concurrent code'
- **In the books:** [*Parallel and Concurrent Programming in Haskell*](../../../10_Resources/books_haskell/README.md#marlow_parallel_and_concurrent_programming_in_haskell), Simon Marlow — ch. 15, 'Debugging, Tuning, and Interfacing with Foreign Code'
- **In the books:** [*asyncio Recipes*](../../../10_Resources/books_python/README.md#tahrioui_asyncio_recipes), Mohamed Mustapha Tahrioui — ch. 8, 'Improving Asyncio Applications' → 'Profiling Asyncio Applications'
- **In the books:** [*Erlang and OTP in Action*](../../../10_Resources/books_elixir_erlang/README.md#logan_erlang_and_otp_in_action), Martin Logan, Eric Merritt, Richard Carlsson — ch. 14, 'Optimization and Performance' → '– How to approach performance tuning'

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
