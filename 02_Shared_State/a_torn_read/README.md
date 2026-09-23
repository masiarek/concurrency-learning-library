# Can a read see half of a write?

**Level:** 201 · anyone who assumed a 64-bit store is one operation

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A value wider than what the machine stores in one instruction can be read while half-written — the high word from the new value, the low word from the old — and Java's specification says so in as many words for `long` and `double`, while C and C++ call the same thing undefined and Rust refuses to let it be written.

## The question

One thread alternates writing `0x0000_0000_0000_0000` and `0xFFFF_FFFF_FFFF_FFFF` to a shared 64-bit variable. Another reads it in a loop. Can it ever read `0x0000_0000_FFFF_FFFF`? On a 64-bit machine with an aligned variable, no — the store is one instruction. On a 32-bit target, on a misaligned address, or for a struct of two words, yes. This is the *torn read*, and it is why the size of an atomic matters.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | a plain `u64` shared between threads does not compile; `AtomicU64` exists only where the platform has a 64-bit atomic (`cfg(target_has_atomic)`) |
| Go | the memory model requires word-sized reads to see one write, and warns that multiword values can tear |
| C | undefined behaviour for any non-atomic shared access; a `struct` of two `long`s tears observably under `-m32` |
| C++ | `std::atomic<T>::is_lock_free()` reports whether `T` is stored in one instruction |
| Java | JLS 17.7: writes to non-volatile `long` and `double` may be two 32-bit writes; `volatile` makes them atomic |
| Python | a `float` or `int` is an object reference; the reference itself does not tear |

## What the programs have to show

- a two-word struct written alternately as all-zeros and all-ones, read a million times, counting mixed reads — as *Real runs*, since a torn read is the machine's
- the same with the struct wrapped in a mutex: zero
- `is_lock_free()` and `cfg(target_has_atomic)` printed per platform

## See also

- Before this: [When is a read-write lock faster than a mutex?](../readers_and_writers/README.md)
- After this: [Why is checking and then acting two steps too many?](../check_then_act/README.md)
- [Is `total += n` safe on two threads?](../the_lost_update/README.md)
- [Data race or race condition?](../data_race_or_race_condition/README.md)
- Concepts: [Atomic variable](../../11_Concepts/lock_free/atomic_variable/README.md) · [Safety failure](../../11_Concepts/hazards/safety_failure/README.md) · [Data race](../../11_Concepts/hazards/data_race/README.md) · [Weak memory models and reordering](../../11_Concepts/hazards/weak_memory_model/README.md)
