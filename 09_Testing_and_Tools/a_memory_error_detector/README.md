# What does AddressSanitizer find that the race detector cannot?

**Level:** 201 · anyone whose C program crashed somewhere else than where the bug was

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A memory error detector poisons the bytes around every allocation and every dead stack frame, so a read past the end of a buffer or into a returned frame is reported at the access with the variable named — the bugs that in a threaded C program otherwise appear as a crash three functions later on another thread — and it and the race detector cannot be used together.

## The question

[Can a thread borrow a local variable?](../../01_Threads/lending_a_local_to_a_thread/README.md) used AddressSanitizer for one dead frame. This page runs it over the four memory bugs a threaded C program makes: a thread reading a freed buffer, a thread writing past the end of a shared array, a dead frame, and a leak from a thread that never joined — and shows what Rust's compiler, Go's collector and Java's bounds checks each do with the same four.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | three of the four are compile errors in safe Rust; the leak from a detached thread is allowed and `Miri` finds it (link) |
| Go | the collector makes the first and third impossible; the second is a panic with `index out of range` |
| C | `-fsanitize=address` reports all four; the report is a *Real runs* fence; Valgrind's Memcheck finds the same without recompiling |
| C++ | the same, plus `-fsanitize=undefined` for the signed overflow the page also plants |
| Java | `ArrayIndexOutOfBoundsException` for the second; the others do not exist |
| Python | `IndexError` for the second; the others do not exist |

## What the programs have to show

- the four bugs in C under AddressSanitizer, as *Real runs*, each report abridged to its named variable
- the same four programs in Rust: the compile errors, as `.sh` driver keys
- Go and Java's runtime panics for the one bug they can have

## See also

- Before this: [What does a race detector see, and what does it miss?](../a_race_detector_finds_what_happened/README.md)
- After this: [How do you write a test that provokes the race?](../a_stress_test_that_actually_races/README.md)
- [Can a thread borrow a local variable?](../../01_Threads/lending_a_local_to_a_thread/README.md)
- [What does a race detector see, and what does it miss?](../a_race_detector_finds_what_happened/README.md)
- The Rust library's [Data races — ThreadSanitizer on a C counter ↗](https://masiarek.github.io/rust-learning-library/31_C_and_Cpp/data_races/index.html)
- Concepts: [Memory error detector](../../11_Concepts/testing_and_tools/memory_error_detector/README.md) · [Dangling pointer](../../11_Concepts/hazards/dangling_pointer/README.md) · [Undefined behaviour](../../11_Concepts/hazards/undefined_behaviour/README.md) · [Data-race freedom by construction](../../11_Concepts/safety_in_languages/data_race_freedom/README.md)
