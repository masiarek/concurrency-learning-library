# Why is checking and then acting two steps too many?

**Level:** 201 · anyone who wrote `if not exists: create`

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** Between the check and the act, another thread can change what was checked — a file that did not exist now does, a key that was absent is now present, a balance that covered the withdrawal no longer does — and the fix is always the same: make the check and the act one operation, which the language, the library or the operating system has to offer.

## The question

`if !map.contains(k) { map.insert(k, v) }` on two threads. Both check, both find nothing, both insert, and the second overwrites the first. This is *time of check to time of use*, the general shape of which [the lost update](../the_lost_update/README.md) is one instance. The page shows it in memory, then the operations each language offers that do the check and the act atomically — and the filesystem case, where the operating system offers `O_EXCL`.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `HashMap::entry(k).or_insert(v)` under one lock; `OpenOptions::create_new` for the file |
| Go | `sync.Map.LoadOrStore`; `os.OpenFile` with `O_CREATE|O_EXCL` |
| C | `open` with `O_CREAT | O_EXCL`; in memory, the check and the insert under one mutex |
| C++ | `std::map::try_emplace`; `std::ios::noreplace` (C++23) |
| Java | `ConcurrentHashMap.putIfAbsent` and `computeIfAbsent`; `Files.createFile` is atomic |
| Python | `dict.setdefault` is atomic under the GIL; `open(path, 'x')` for the file |

## What the programs have to show

- two threads doing check-then-insert on a plain map behind a barrier between the check and the act: two inserts, one lost
- the same with the one-step operation: one insert, and the loser learns it lost
- the filesystem: two processes creating the same file with and without exclusive create

## See also

- Before this: [Can a read see half of a write?](../a_torn_read/README.md)
- After this: [Can a compare-and-swap succeed when it should have failed?](../the_aba_problem/README.md)
- [Is `total += n` safe on two threads?](../the_lost_update/README.md)
- [The lost update in a database](../the_lost_update_in_a_database/README.md)
- [Can a compare-and-swap succeed when it should have failed?](../the_aba_problem/README.md)
- Concepts: [Time of check to time of use](../../11_Concepts/hazards/toctou/README.md) · [Race condition](../../11_Concepts/hazards/race_condition/README.md) · [Compare-and-swap](../../11_Concepts/lock_free/compare_and_swap/README.md) · [Mutual exclusion](../../11_Concepts/synchronization/mutual_exclusion/README.md)
