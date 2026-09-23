# How do you read a thread dump?

**Level:** 201 · anyone handed a stack trace for fifty threads

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A thread dump is every thread's stack at one instant, and reading one is a matter of three questions — which threads are *waiting*, what are they waiting for, and who holds it — which Java's `jstack` answers in its own format, Go's `SIGQUIT` dump in another, and `gdb`'s `thread apply all bt` in a third, and the page reads the same deadlock in all three.

## The question

[Detecting a deadlock](../../03_When_Locks_Go_Wrong/detecting_a_deadlock/README.md) got the dump; this page reads it. The same hung program, fifty threads: forty-eight idle in a pool, two deadlocked. The page shows each format abridged, marks the lines that matter, and gives the reading order — find the threads not in a known idle state, find their locks, find the cycle — then does the same for a hang that is not a deadlock: a thread blocked in a `read` that will never return.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `lldb`/`gdb` on the process, with the Rust frames' names |
| Go | the `SIGQUIT` dump, with `goroutine N [semacquire]:` and `[chan receive]:` as the states to look for |
| C | `gdb -p`, `thread apply all bt`, and `info threads` |
| C++ | the same as C |
| Java | `jstack`, with `BLOCKED`, `WAITING`, and the `Found one Java-level deadlock` section |
| Python | `faulthandler.dump_traceback_later` or `py-spy dump` |

## What the programs have to show

- the three dump formats for the same deadlock, abridged to the two threads and marked
- the blocked-read hang in each, with the state that gives it away
- the idle pool threads, and how each format shows *nothing to see here*

## See also

- Before this: [Can every interleaving of a small program be checked?](../model_checking_a_small_program/README.md)
- After this: [Where does a concurrent program spend its time?](../profiling_where_the_time_goes/README.md)
- [How do you find out where a deadlocked program is stuck?](../../03_When_Locks_Go_Wrong/detecting_a_deadlock/README.md)
- [Where does a concurrent program spend its time?](../profiling_where_the_time_goes/README.md)
- The Rust library's [Diagnosing a stuck runtime ↗](https://masiarek.github.io/rust-learning-library/35_Async/building_minidb/diagnosing_a_stuck_runtime/index.html)
- The Go library's [All goroutines are asleep ↗](https://masiarek.github.io/go-learning-library/02_Channels/all_goroutines_are_asleep/index.html)
- Concepts: [Debugging concurrent programs](../../11_Concepts/testing_and_tools/concurrency_debugging/README.md) · [Deadlock](../../11_Concepts/hazards/deadlock/README.md) · [Liveness failure](../../11_Concepts/hazards/liveness_failure/README.md) · [Thread pool and executor](../../11_Concepts/units_of_execution/thread_pool/README.md)
