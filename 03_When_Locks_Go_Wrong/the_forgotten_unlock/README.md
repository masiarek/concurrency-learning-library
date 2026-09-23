# Who unlocks when the function returns early?

**Level:** 201 · anyone who has held a lock through an early `return` or an exception

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A lock released by an explicit call is not released on the path you forgot — the early return, the thrown exception, the `?` — and the next thread to ask for it waits forever; Rust, C++ and Python tie the unlock to a scope that always ends, Go ties it to `defer`, Java to `finally` or `synchronized`, and C ties it to nothing, which is where the bug lives.

## The question

A function locks, checks a precondition, and returns early when it fails — without unlocking. The second caller hangs. It is the most common lock bug there is, and the languages have five different answers to it, of which four make the bug hard to write. The page writes it in all six anyway, then shows each language's guard.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | impossible to forget: `MutexGuard` unlocks when dropped, on every path including `?` and panic |
| Go | `defer mu.Unlock()` right after `mu.Lock()` is the idiom; forget the `defer` and the early return leaks the lock |
| C | `pthread_mutex_unlock` on every path by hand; the early `return` without it hangs the next caller |
| C++ | `std::lock_guard` or `std::scoped_lock` unlocks in its destructor, including during unwinding |
| Java | `synchronized` releases on any exit; `ReentrantLock` needs `try`/`finally` |
| Python | `with lock:` releases on any exit, including an exception |

## What the programs have to show

- the early return that forgets, in Go, C and Java's `ReentrantLock`: the second caller hangs, killed by a timeout driver
- the guarded versions in all six: the second caller runs
- the exception path: a throw inside the critical section, and whether the lock is released

## See also

- Before this: [What happens when a thread takes a lock it already holds?](../a_lock_taken_twice/README.md)
- After this: [What state is the data in after a thread died holding the lock?](../a_panic_while_holding_the_lock/README.md)
- [What state is the data in after a thread died holding the lock?](../a_panic_while_holding_the_lock/README.md)
- [Why do two locks taken in different orders hang?](../two_locks_in_different_orders/README.md)
- The Rust library's [Forgotten unlock ↗](https://masiarek.github.io/rust-learning-library/31_C_and_Cpp/forgotten_unlock/index.html)
- Concepts: [Scoped locking](../../11_Concepts/synchronization/scoped_lock/README.md) · [Mutex](../../11_Concepts/synchronization/mutex/README.md) · [Deadlock](../../11_Concepts/hazards/deadlock/README.md) · [Critical section](../../11_Concepts/synchronization/critical_section/README.md)
