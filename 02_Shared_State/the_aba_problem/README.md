# Can a compare-and-swap succeed when it should have failed?

**Level:** 201 · anyone building a lock-free structure

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** Compare-and-swap checks that a value is still what it was, not that nothing has happened: a value that went from A to B and back to A passes the check, and if A is a pointer to a node that was freed and reallocated in between, the swap installs garbage — the *ABA problem*, which is why lock-free code carries a version counter beside the pointer.

## The question

A lock-free stack pops by reading the head A, reading A's next B, and swapping head from A to B. Between the reads and the swap, another thread pops A, pops B, pushes A back. The swap sees head == A and succeeds — installing B, which is no longer on the stack. Nothing was wrong with any single step. The page forces this interleaving with a barrier and then shows the tagged-pointer fix.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `AtomicPtr` with the interleaving forced; the fix is a `(ptr, tag)` in an `AtomicU128` where available, or `crossbeam-epoch` (link, not run) |
| Go | `atomic.Pointer` cannot show the memory reuse because the collector keeps A alive — the classic ABA is a non-GC problem |
| C | `atomic_compare_exchange_strong` on a struct of pointer and counter, if the platform has a double-width CAS |
| C++ | `std::atomic<Node*>::compare_exchange_strong`; the fix with a packed pointer-and-tag |
| Java | `AtomicStampedReference` exists precisely for this and carries an `int` stamp |
| Python | not reachable: no CAS on plain objects, and the GIL serializes the steps |

## What the programs have to show

- the stack, the forced pop-pop-push in the middle, and a final stack that contains a node that was freed
- the same with a stamp beside the pointer: the swap fails and retries
- Go's and Java's runs showing why a garbage collector makes the *memory* half of the problem vanish and leaves the *logic* half

## See also

- Before this: [Why is checking and then acting two steps too many?](../check_then_act/README.md)
- After this: [What may be handed to another thread?](../what_may_cross_a_thread_boundary/README.md)
- [Why is checking and then acting two steps too many?](../check_then_act/README.md)
- [Keeping every update](../keeping_every_update/README.md)
- Concepts: [ABA problem](../../11_Concepts/hazards/aba_problem/README.md) · [Compare-and-swap](../../11_Concepts/lock_free/compare_and_swap/README.md) · [Lock-free](../../11_Concepts/lock_free/lock_free/README.md) · [Hazard pointers](../../11_Concepts/lock_free/hazard_pointers/README.md) · [Concurrent data structures](../../11_Concepts/lock_free/concurrent_data_structures/README.md)
