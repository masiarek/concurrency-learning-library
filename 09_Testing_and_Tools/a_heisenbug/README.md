# Why did the bug disappear when you added a print?

**Level:** 201 · anyone whose race went away under the debugger

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A print, a log line or a breakpoint takes microseconds, and a race whose window is nanoseconds closes when either side is slowed by that much — so the instrument that was added to observe the bug removes it, which is the Heisenbug, and the cure is an observer that does not change the timing: a ring buffer written with one atomic store, read after the fact.

## The question

A race that loses an update one run in a hundred. Add a `println!` in the window: one in a million. Add a breakpoint: never. The page measures the loss rate with and without the print, as *Real runs*, then shows the observer that does not disturb: each thread writing a timestamp and an event code into its own slot of a preallocated array, dumped after the run — and finds the race in the dump.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | the loss rate with and without a `println!` in the window; a `static` array of `AtomicU64` slots as the quiet observer |
| Go | the same with `fmt.Println`; `runtime/trace` is the built-in quiet observer |
| C | the same with `printf`; a static array of slots |
| C++ | the same |
| Java | the same with `System.out.println`, which is `synchronized` and slows it further; JFR as the quiet observer |
| Python | the same with `print`, which takes the GIL; the free-threaded build for a real window |

## What the programs have to show

- *Real runs*: lost updates per million with no observer, with a print, with the ring buffer
- the ring buffer's dump showing the interleaving that lost the update
- the CI example: the forced version from chapter 02, which no observer can hide

## See also

- Before this: [Where does a concurrent program spend its time?](../profiling_where_the_time_goes/README.md)
- [How do you write a test that provokes the race?](../a_stress_test_that_actually_races/README.md)
- [Is `total += n` safe on two threads?](../../02_Shared_State/the_lost_update/README.md)
- The Go library's [The race detector ↗](https://masiarek.github.io/go-learning-library/07_Testing_Concurrent_Code/the_race_detector/index.html)
- Concepts: [Heisenbug](../../11_Concepts/hazards/heisenbug/README.md) · [Nondeterminism](../../11_Concepts/foundations/nondeterminism/README.md) · [Race condition](../../11_Concepts/hazards/race_condition/README.md) · [Debugging concurrent programs](../../11_Concepts/testing_and_tools/concurrency_debugging/README.md) · [Profiling concurrent programs](../../11_Concepts/testing_and_tools/profiling_concurrency/README.md)
