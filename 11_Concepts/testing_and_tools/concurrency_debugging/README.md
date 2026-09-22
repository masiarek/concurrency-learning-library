# Debugging concurrent programs

**Category:** [Testing and tools](../README.md) · **Status:** stub · **Lessons:** chapter 09, Testing and tools *(planned)*

**One line:** Thread dumps, deadlock detectors and tracing that show what every thread or task is waiting for at a given moment.

Also called: thread dump, deadlock detection, goroutine dump, stack dump.

## How it connects


- **See also:** [Deadlock](../../hazards/deadlock/README.md), [Memory error detector](../memory_error_detector/README.md)

## In each language

| | |
|---|---|
| Go | `SIGQUIT` (Ctrl-backslash) makes a program [exit with a stack dump ↗](https://pkg.go.dev/os/signal#hdr-Default_behavior_of_signals_in_Go_programs); [`runtime/pprof` ↗](https://pkg.go.dev/runtime/pprof) has `goroutine`, `block` and `mutex` profiles |
| Java | [`jcmd` `Thread.print` ↗](https://docs.oracle.com/en/java/javase/25/docs/specs/man/jcmd.html) prints all threads with stack traces; [`ThreadMXBean.findDeadlockedThreads` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.management/java/lang/management/ThreadMXBean.html) finds cycles of deadlocked threads |
| Python | [`faulthandler.dump_traceback` ↗](https://docs.python.org/3/library/faulthandler.html#faulthandler.dump_traceback) dumps the tracebacks of all threads, also after a timeout or on a signal |
| C# | [`dotnet-stack` ↗](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/dotnet-stack) inspects managed stack traces |
| Elsewhere | [GDB ↗](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Threads.html) `thread apply all bt` applies `bt` to every thread, printing a backtrace for each |

## Where to read more

- **In a sibling library:** [Rust: Instrumenting async code ↗](https://masiarek.github.io/rust-learning-library/21_Observability/instrumenting_async/index.html)
- **In a sibling library:** [Go: All goroutines are asleep ↗](https://masiarek.github.io/go-learning-library/02_Channels/all_goroutines_are_asleep/index.html)
- **In the books:** [*Effective Concurrency in Go*](../../../10_Resources/books_go/README.md#serdar_effective_concurrency_in_go), Burak Serdar — ch. 10, 'Troubleshooting Concurrency Issues'
- **In the books:** [*Programming with POSIX Threads*](../../../10_Resources/books_c/README.md#butenhof_programming_with_posix_threads), David R. Butenhof — ch. 8, 'Hints to Avoid Debugging'
- **In the books:** [*C++ Concurrency in Action*](../../../10_Resources/books_cpp/README.md#williams_cpp_concurrency_in_action), Anthony Williams — ch. 11, 'Testing and debugging multithreaded applications'
- **In the books:** [*Concurrent Programming on Windows*](../../../10_Resources/books_csharp_dotnet/README.md#duffy_concurrent_programming_on_windows), Joe Duffy — ch. 11, 'Concurrency Hazards'
- **In the books:** [*Mastering C++ Multithreading*](../../../10_Resources/books_cpp/README.md#posch_mastering_cpp_multithreading), Maya Posch — ch. 6, 'Debugging Multithreaded Code'
- **In the books:** [*Learning Concurrent Programming in Scala*](../../../10_Resources/books_scala_jvm_functional/README.md#prokopec_learning_concurrent_programming_in_scala), Aleksandar Prokopec — ch. 9, 'Concurrency in Practice' → 'Debugging concurrent programs'
- **Notes:** [tools for concurrent programming ↗](https://docs.google.com/document/d/1SC1yU8oBqvxoAsZZ2AdoaCnHFR8apqvzSoNh4U2tX0U/edit?tab=t.0)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
