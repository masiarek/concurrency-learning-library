# Can every interleaving of a small program be checked?

**Level:** 201 · anyone who wants proof rather than evidence

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A model checker runs a small concurrent program under *every* possible interleaving — thousands for two threads and a few steps — and reports the first that breaks an assertion, which is the only way to be sure a lock-free algorithm is right; it works on programs small enough to enumerate, and the page's two-thread lost update has exactly forty-two.

## The question

Two threads, three steps each: load, add, store. How many interleavings? Twenty, and eight of them lose an update. The page enumerates them — with a hand-written scheduler in each language that runs the two threads step by step under every permutation — and counts the bad ones, then shows the tools that do this for real code: `loom` for Rust, TLA+ for the design, `jcstress` for the JVM.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `loom::model` runs a closure under every interleaving of its atomics (link, not run); the std column enumerates by hand |
| Go | no model checker for Go code; the hand enumeration, and a TLA+ spec linked |
| C | the hand enumeration; `CBMC` and `SPIN` linked |
| C++ | the hand enumeration; the same links |
| Java | `jcstress` runs the shape empirically by the million; the hand enumeration for the proof |
| Python | the hand enumeration in about forty lines, which is the page's reference implementation |

## What the programs have to show

- the twenty interleavings of two three-step threads, enumerated, with the eight that lose an update listed
- the same for the locked version: zero
- `loom`'s and TLA+'s output for the same model, as *Real runs*

## See also

- Before this: [How does a test wait an hour in a millisecond?](../virtual_time_in_tests/README.md)
- After this: [How do you read a thread dump?](../reading_a_thread_dump/README.md)
- [Is `total += n` safe on two threads?](../../02_Shared_State/the_lost_update/README.md)
- [How do you write a test that provokes the race?](../a_stress_test_that_actually_races/README.md)
- Concepts: [Model checking](../../11_Concepts/testing_and_tools/model_checking/README.md) · [Interleaving](../../11_Concepts/foundations/interleaving/README.md) · [Deterministic scheduling for tests](../../11_Concepts/testing_and_tools/deterministic_testing/README.md) · [Lock-free](../../11_Concepts/lock_free/lock_free/README.md)
