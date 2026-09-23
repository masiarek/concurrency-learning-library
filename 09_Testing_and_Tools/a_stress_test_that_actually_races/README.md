# How do you write a test that provokes the race?

**Level:** 201 · anyone whose flaky test passes when run alone

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A concurrency test that runs the racing code once almost never sees the race, so a stress test runs it ten thousand times from a barrier, on more threads than cores, with a yield or a sleep-zero between the steps that must interleave — and even then it is evidence, not proof, which is why this library's answer keys force the interleaving instead of provoking it.

## The question

The lost update again. Run it once: correct. Ten thousand times from a barrier: lost updates appear. Add a `yield` between the load and the store: many more. The page measures how many runs each technique takes to expose the race, as *Real runs*, then shows the technique that makes it certain — the barrier between the load and the store — which is what the chapter 02 lessons do.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | a `#[test]` looping ten thousand times with `thread::scope`; `loom` for the exhaustive version (link) |
| Go | `go test -race -count=1000`; `runtime.Gosched()` between the steps |
| C | a loop in `main` with `sched_yield` |
| C++ | the same with `std::this_thread::yield` |
| Java | `@RepeatedTest(10000)`; `jcstress` runs this shape by the million (link) |
| Python | a loop with `time.sleep(0)`; the free-threaded build needed |

## What the programs have to show

- *Real runs*: iterations to first lost update with no yield, with a yield, on N > cores
- the barrier version: lost on run one, every time — the CI example
- the test that passes alone and fails under `-count=1000`, and the reason

## See also

- Before this: [What does AddressSanitizer find that the race detector cannot?](../a_memory_error_detector/README.md)
- After this: [How does a test wait an hour in a millisecond?](../virtual_time_in_tests/README.md)
- [Is `total += n` safe on two threads?](../../02_Shared_State/the_lost_update/README.md)
- [How does a test wait an hour in a millisecond?](../virtual_time_in_tests/README.md)
- The Go library's [The race detector ↗](https://masiarek.github.io/go-learning-library/07_Testing_Concurrent_Code/the_race_detector/index.html)
- The Rust library's [Testing async code ↗](https://masiarek.github.io/rust-learning-library/35_Async/building_minidb/testing_async_code/index.html)
- Concepts: [Stress testing](../../11_Concepts/testing_and_tools/stress_testing/README.md) · [Heisenbug](../../11_Concepts/hazards/heisenbug/README.md) · [Nondeterminism](../../11_Concepts/foundations/nondeterminism/README.md) · [Deterministic scheduling for tests](../../11_Concepts/testing_and_tools/deterministic_testing/README.md) · [Interleaving](../../11_Concepts/foundations/interleaving/README.md)
