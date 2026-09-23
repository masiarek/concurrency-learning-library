# How does initialization run exactly once with many threads racing to it?

**Level:** 201 · anyone who wrote a lazy singleton

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A check-then-initialize is [the check-then-act bug](../../02_Shared_State/check_then_act/README.md) with a constructor in it — two threads see `None`, both build, one result is dropped — and every language here has a primitive that runs the initializer once and makes every other caller wait for it, including the callers that arrive while it is still running.

## The question

Ten threads call `config()`. The first to arrive must build the config; the other nine must get *that* config, not build their own, and must not return before it is ready. `if config is None: config = build()` does none of that. The page runs ten threads through the naive check and counts the builds, then through each language's once-primitive and counts one — and then asks what happens when the initializer panics.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `OnceLock` / `LazyLock` in std; a panic in the initializer poisons the `Once` |
| Go | `sync.Once.Do`; a panic inside counts as done, and `OnceFunc`/`OnceValue` since 1.21 |
| C | `pthread_once`; if the init routine is cancelled it may run again |
| C++ | `std::call_once` with `std::once_flag`; a thrown exception lets the next caller retry; a `static` local is initialized once by the language |
| Java | a `static` initializer runs once under the class-init lock; `ConcurrentHashMap.computeIfAbsent` for a keyed once |
| Python | `functools.cache` is not thread-safe for the first call; a `Lock` around the check |

## What the programs have to show

- ten threads through the naive check, from a barrier: builds counted, more than one
- ten threads through the once-primitive: one build, ten identical results
- the initializer that fails: what the second caller sees, per language

## See also

- Before this: [How do N threads wait for each other?](../a_barrier_and_a_latch/README.md)
- After this: [What is a monitor, and which languages have one?](../a_monitor_bundles_lock_and_condition/README.md)
- [Why is checking and then acting two steps too many?](../../02_Shared_State/check_then_act/README.md)
- The Go library's [`sync.Once` runs exactly once ↗](https://masiarek.github.io/go-learning-library/04_Sync/once_runs_exactly_once/index.html)
- Concepts: [Run-once initialization](../../11_Concepts/synchronization/once_initialization/README.md) · [Time of check to time of use](../../11_Concepts/hazards/toctou/README.md) · [Synchronization](../../11_Concepts/synchronization/synchronization/README.md) · [Thread safety](../../11_Concepts/safety_in_languages/thread_safety/README.md)
