# Why do two locks taken in different orders hang?

**Level:** 201 · anyone whose program stopped, with every thread waiting

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** Thread A holds lock 1 and waits for lock 2 while thread B holds lock 2 and waits for lock 1, and neither can ever proceed — a deadlock — and the only complete fix is to take every lock in one agreed order everywhere, which no compiler here enforces and Go's runtime alone detects, and only when every goroutine is stuck.

## The question

A transfer between two accounts locks the source, then the destination. Two transfers in opposite directions run at once. Each holds its first lock and waits forever for its second. The page forces that interleaving with a barrier between the two lock calls, so every run deadlocks, then shows the program dying by timeout and what each runtime says about it — nothing, mostly. The fix, lock ordering, is one line and the page shows why it works.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | two `Mutex`es, the forced interleaving, and a hang; `parking_lot` has a deadlock detector (link, not run) |
| Go | the same hang; if *every* goroutine is stuck the runtime panics with `all goroutines are asleep - deadlock!`, exit 2 |
| C | `pthread_mutex_lock` blocks forever; an `ERRORCHECK` mutex reports only self-deadlock |
| C++ | `std::scoped_lock(m1, m2)` takes both in a deadlock-free order, which is the fix in the library |
| Java | `synchronized` on two objects hangs; `jstack` prints "Found one Java-level deadlock" |
| Python | two `Lock`s hang; nothing detects it |

## What the programs have to show

- the forced deadlock per language, run by a `.sh` driver with a two-second timeout, printing how it died
- the same program with the locks ordered by address or id: completes, and the totals are right
- the one runtime message, Go's, and the one library fix, C++'s `scoped_lock`

## See also

- After this: [What happens when a thread takes a lock it already holds?](../a_lock_taken_twice/README.md)
- [How do you find out where a deadlocked program is stuck?](../detecting_a_deadlock/README.md)
- [Who unlocks when the function returns early?](../the_forgotten_unlock/README.md)
- The Go library's [All goroutines are asleep ↗](https://masiarek.github.io/go-learning-library/02_Channels/all_goroutines_are_asleep/index.html)
- Concepts: [Deadlock](../../11_Concepts/hazards/deadlock/README.md) · [Lock ordering](../../11_Concepts/synchronization/lock_ordering/README.md) · [Liveness failure](../../11_Concepts/hazards/liveness_failure/README.md) · [Mutex](../../11_Concepts/synchronization/mutex/README.md) · [Scoped locking](../../11_Concepts/synchronization/scoped_lock/README.md)
