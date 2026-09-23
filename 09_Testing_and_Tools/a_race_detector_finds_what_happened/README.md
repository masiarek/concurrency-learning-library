# What does a race detector see, and what does it miss?

**Level:** 201 · anyone whose tests pass under `-race`

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A race detector instruments every memory access and reports two of them from different threads with no happens-before edge between — so it finds every data race *on the path the test took*, including ones that did not corrupt anything, and misses every race on a path the test did not take, and it cannot see a race condition at all.

## The question

[Data race or race condition?](../../02_Shared_State/data_race_or_race_condition/README.md) showed the detector reporting a race whose answer was always right. This page shows the other three cases: a race on a branch the test did not run — reported nothing; a race that happened on this run — reported; the same program with the racing accesses under a lock — silent; and the atomic lost update — silent, and wrong.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | no detector in stable Rust; `-Zsanitizer=thread` on nightly (link, not run); safe Rust's compile-time rule is the comparison |
| Go | `go test -race` and `go build -race`, ThreadSanitizer underneath; the four cases as `.sh` drivers |
| C | `-fsanitize=thread` with the same four cases; the report is a *Real runs* fence |
| C++ | the same |
| Java | no standard detector; the JVM has none built in (link to `jcstress`, not run) |
| Python | none; the free-threaded build has no race detector either |

## What the programs have to show

- the four programs under Go's detector: reported, not reported, not reported, not reported — with the last one wrong
- the same four under ThreadSanitizer in C, as *Real runs*
- the untaken-branch case made taken by a second test, and reported

## See also

- After this: [What does AddressSanitizer find that the race detector cannot?](../a_memory_error_detector/README.md)
- [Data race or race condition?](../../02_Shared_State/data_race_or_race_condition/README.md)
- [What does AddressSanitizer find that the race detector cannot?](../a_memory_error_detector/README.md)
- The Go library's [The race detector ↗](https://masiarek.github.io/go-learning-library/07_Testing_Concurrent_Code/the_race_detector/index.html)
- The Rust library's [Data races — ThreadSanitizer on a C counter ↗](https://masiarek.github.io/rust-learning-library/31_C_and_Cpp/data_races/index.html)
- Concepts: [Race detector](../../11_Concepts/testing_and_tools/race_detector/README.md) · [Data race](../../11_Concepts/hazards/data_race/README.md) · [Race condition](../../11_Concepts/hazards/race_condition/README.md) · [Happens-before](../../11_Concepts/lock_free/happens_before/README.md)
