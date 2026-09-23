# 09 — Testing and tools

Every other chapter forces its interleavings so that the answer key is deterministic. This one is about what to do when you cannot: a race detector that sees the accesses a test made, a memory error detector that names the variable, a stress test that provokes the race a thousand times, a virtual clock that makes an hour's timeout take a millisecond, a model checker that tries every interleaving of a small program, and the profiles and thread dumps that say where a live program's time went.

Every lesson in this chapter is a **stub**: the question, the expected answer per language and what the programs will have to show, waiting for the programs. A stub becomes a lesson when its examples run in CI and its table is replaced by what they printed.

| Lesson | The one thing |
|---|---|
| [What does a race detector see, and what does it miss?](a_race_detector_finds_what_happened/README.md) | *stub* — every data race on the path the test took, none on the path it did not, and no race condition at all |
| [What does AddressSanitizer find that the race detector cannot?](a_memory_error_detector/README.md) | *stub* — a read past the end or into a dead frame, reported at the access with the variable named |
| [How do you write a test that provokes the race?](a_stress_test_that_actually_races/README.md) | *stub* — ten thousand runs from a barrier with a yield in the window: evidence, not proof |
| [How does a test wait an hour in a millisecond?](virtual_time_in_tests/README.md) | *stub* — `synctest` and a paused clock make an hour's timeout take a millisecond; elsewhere the clock has to be injected |
| [Can every interleaving of a small program be checked?](model_checking_a_small_program/README.md) | *stub* — every interleaving of two three-step threads is twenty, and eight lose an update |
| [How do you read a thread dump?](reading_a_thread_dump/README.md) | *stub* — which threads are waiting, for what, and who holds it — in three formats |
| [Where does a concurrent program spend its time?](profiling_where_the_time_goes/README.md) | *stub* — not which function but which thread was doing what, and which were waiting for whom |
| [Why did the bug disappear when you added a print?](a_heisenbug/README.md) | *stub* — the print that was added to see the race is what closed the window |
