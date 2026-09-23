# How does a test wait an hour in a millisecond?

**Level:** 201 · anyone whose timeout test takes as long as the timeout

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A test of a retry-with-backoff or a timeout either really waits — minutes per test — or replaces the clock with one the test controls, advancing it by an hour in one call and waking every sleeper that was due; Go's `synctest` and `tokio`'s paused clock do this for their runtimes, and everywhere else the clock has to be an interface the code under test was written against.

## The question

A function retries three times with one-minute backoffs. Test it. Really waiting takes three minutes. Under `synctest`, `time.Sleep(time.Minute)` returns when every goroutine in the bubble is blocked and the virtual clock jumps; the test takes a millisecond and is deterministic. The page runs the retry test both ways, then shows what the other languages need: a clock passed in.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `tokio::time::pause()` and `advance()` (link, not run); the std column passes a `Fn() -> Instant` clock |
| Go | `testing/synctest` (Go 1.25): `synctest.Test` runs the code in a bubble with a fake clock |
| C | a clock function pointer; the test supplies one that counts calls |
| C++ | `std::chrono` clocks are types, so the code is templated on the clock and the test supplies a fake |
| Java | `java.time.Clock` injected; `Clock.fixed` and a hand-advanced test clock |
| Python | `unittest.mock.patch('time.sleep')` and a fake `monotonic` |

## What the programs have to show

- the retry test under real time as *Real runs* (three seconds, scaled down), and under virtual time as the CI key: three retries, zero wall time
- Go's `synctest.Wait` replacing a sleep in a test, from the Go library
- the clock interface in each other language, and the test's fake

## See also

- Before this: [How do you write a test that provokes the race?](../a_stress_test_that_actually_races/README.md)
- After this: [Can every interleaving of a small program be checked?](../model_checking_a_small_program/README.md)
- [How do you write a test that provokes the race?](../a_stress_test_that_actually_races/README.md)
- [What does a sleep promise, and what does a yield?](../../01_Threads/sleep_and_yield/README.md)
- The Go library's [`synctest` makes time virtual ↗](https://masiarek.github.io/go-learning-library/07_Testing_Concurrent_Code/synctest_makes_time_virtual/index.html)
- The Go library's [`synctest.Wait` instead of a sleep ↗](https://masiarek.github.io/go-learning-library/07_Testing_Concurrent_Code/synctest_wait/index.html)
- The Rust library's [Testing async code ↗](https://masiarek.github.io/rust-learning-library/35_Async/building_minidb/testing_async_code/index.html)
- Concepts: [Deterministic scheduling for tests](../../11_Concepts/testing_and_tools/deterministic_testing/README.md) · [Timers and tickers](../../11_Concepts/async/timers/README.md) · [Timeout](../../11_Concepts/async/timeout/README.md) · [Stress testing](../../11_Concepts/testing_and_tools/stress_testing/README.md)
