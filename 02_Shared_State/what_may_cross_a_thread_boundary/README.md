# What may be handed to another thread?

**Level:** 201 · anyone who has met `Send`, or `ConcurrentModificationException`, or a `pickle` error

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** Rust decides at compile time which values may move to another thread (`Send`) and which may be shared between threads (`Sync`), and refuses the rest; every other language here lets anything cross and finds out at run time — Java with a fail-fast iterator, Python with a pickling error at the process boundary, Go and C with a data race.

## The question

Hand a value to a thread. A number, obviously. A reference to a local — [the previous chapter's](../../01_Threads/lending_a_local_to_a_thread/README.md) question. A reference-counted pointer that is not thread-safe? A database connection? A mutex guard? Rust's `Send` and `Sync` are the compiler's answer to *each* of those, and this page walks the same five values across all six languages to see which ones say anything at all.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `Rc<T>` is not `Send`, `MutexGuard` is not `Send`, a raw pointer is neither: each is a compile error with the reason named |
| Go | anything may cross; the race detector finds the misuse of a map, the runtime finds it best-effort |
| C | a `void *` crosses, and what it points to is nobody's business |
| C++ | the same: `std::thread` takes any callable; `std::shared_ptr`'s count is atomic but the pointee is not protected |
| Java | any object crosses; `ArrayList` iterated while modified throws `ConcurrentModificationException` on a best-effort basis |
| Python | any object crosses between threads; only picklable ones cross to a `multiprocessing` process |

## What the programs have to show

- the five values handed to `thread::spawn`: which compile, and the error line for each that does not
- the same five in each other language: which fail, when, and how
- a *Real runs* fence for the Java fail-fast iterator, which is not guaranteed to throw

## See also

- Before this: [Can a compare-and-swap succeed when it should have failed?](../the_aba_problem/README.md)
- After this: [Can one thread see another's writes out of order?](../reordering_and_the_memory_model/README.md)
- [Can a thread borrow a local variable?](../../01_Threads/lending_a_local_to_a_thread/README.md)
- [Data race or race condition?](../data_race_or_race_condition/README.md)
- The Rust library's [Send and Sync ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/send_and_sync/index.html)
- The Rust library's [Sharing across threads: Arc ↗](https://masiarek.github.io/rust-learning-library/18_Ownership/sharing_across_threads/index.html)
- Concepts: [Send and Sync](../../11_Concepts/safety_in_languages/send_and_sync/README.md) · [Thread safety](../../11_Concepts/safety_in_languages/thread_safety/README.md) · [Data-race freedom by construction](../../11_Concepts/safety_in_languages/data_race_freedom/README.md) · [Thread confinement](../../11_Concepts/safety_in_languages/thread_confinement/README.md) · [Immutability](../../11_Concepts/safety_in_languages/immutability/README.md)
