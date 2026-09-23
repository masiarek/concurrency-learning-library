# 03 — When locks go wrong

A lock is the simplest fix in chapter 02 and the source of every failure in this one. Two locks taken in different orders stop a program dead; one lock taken twice hangs its own thread; a lock not released on the early return hangs the next caller; a lock released by a thread that died leaves the data half-changed. None of these is a data race and no race detector finds any of them. This chapter forces each one, watches what the runtimes say — mostly nothing — and shows the discipline or the type that rules it out.

Every lesson in this chapter is a **stub**: the question, the expected answer per language and what the programs will have to show, waiting for the programs. A stub becomes a lesson when its examples run in CI and its table is replaced by what they printed.

| Lesson | The one thing |
|---|---|
| [Why do two locks taken in different orders hang?](two_locks_in_different_orders/README.md) | *stub* — A holds 1 and wants 2, B holds 2 and wants 1: deadlock, and only lock ordering rules it out |
| [What happens when a thread takes a lock it already holds?](a_lock_taken_twice/README.md) | *stub* — a hang in Rust, Go and C; undefined in C++; a count in Java and `RLock` |
| [Who unlocks when the function returns early?](the_forgotten_unlock/README.md) | *stub* — the early return that skips the unlock; guards tie the unlock to the scope, C ties it to nothing |
| [What state is the data in after a thread died holding the lock?](a_panic_while_holding_the_lock/README.md) | *stub* — the data is half-updated and unlocked for the next thread; Rust poisons the mutex so someone notices |
| [Can two threads be busy forever and get nothing done?](livelock/README.md) | *stub* — two polite threads that back off and retry in lockstep forever; a random backoff breaks it |
| [Can a thread wait forever for a lock that is always free eventually?](starvation_and_fairness/README.md) | *stub* — a mutex promises exclusion, not turns; Java's fairness flag and Go's starvation mode cost throughput for the promise |
| [How does a low-priority thread block a high-priority one?](priority_inversion/README.md) | *stub* — High waits for a lock Low holds while Medium keeps Low off the CPU; POSIX's priority inheritance is the fix |
| [What does a spinlock cost when there is nowhere to spin?](a_spinlock_on_one_core/README.md) | *stub* — cheaper than a mutex for a few hundred nanoseconds, ruinous on one core |
| [How do you find out where a deadlocked program is stuck?](detecting_a_deadlock/README.md) | *stub* — Go reports a total deadlock unasked, `jstack` names the cycle, everyone else needs a debugger |
