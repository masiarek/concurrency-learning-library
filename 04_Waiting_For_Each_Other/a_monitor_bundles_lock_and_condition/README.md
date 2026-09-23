# What is a monitor, and which languages have one?

**Level:** 201 · anyone who has written `synchronized` and `wait()` on the same object

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A monitor is a lock and its condition variables bundled into one object with the rule that the condition can only be waited on while the lock is held — Java built it into every object, Python's `Condition` is one, Go's `sync.Cond` is half of one, and C, C++ and Rust make you assemble it from a mutex and a condition variable, which is where the rule gets forgotten.

## The question

Every `wait` on this chapter's first page happened under a lock, and every language required or assumed it. The monitor is the construct that makes that requirement structural: the lock, the shared state and the conditions are one thing. The page shows the bounded buffer written as a monitor in the languages that have one, and assembled in the ones that do not, and then breaks the rule to show what a wait without the lock does.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | a struct holding `Mutex<State>` and `Condvar`; `Condvar::wait` takes the guard, which enforces the rule |
| Go | `sync.Cond` with its `L` locker: `Wait` unlocks and relocks `L`, and calling it without holding `L` is a bug the runtime does not catch |
| C | `pthread_cond_wait(&c, &m)` requires `m` held; calling it unlocked is undefined |
| C++ | `std::condition_variable::wait(unique_lock&)`; the lock type enforces holding |
| Java | every object is a monitor: `synchronized`, `wait`, `notify`; `wait()` outside `synchronized` throws `IllegalMonitorStateException` |
| Python | `threading.Condition` wraps a lock; `wait()` without `acquire()` raises `RuntimeError` |

## What the programs have to show

- the bounded buffer as a monitor in each language, a hundred items through, in order
- the wait without the lock: the exception in Java and Python, the undefined behaviour or hang elsewhere
- one monitor with two conditions, *not full* and *not empty*, against one condition with `broadcast`

## See also

- Before this: [How does initialization run exactly once with many threads racing to it?](../run_exactly_once/README.md)
- After this: [How does a producer wait for room and a consumer wait for an item?](../the_bounded_buffer/README.md)
- [How does a thread wait for something to become true?](../waiting_for_a_condition/README.md)
- [How does a producer wait for room and a consumer wait for an item?](../the_bounded_buffer/README.md)
- Concepts: [Monitor](../../11_Concepts/synchronization/monitor/README.md) · [Condition variable](../../11_Concepts/synchronization/condition_variable/README.md) · [Mutex](../../11_Concepts/synchronization/mutex/README.md) · [Critical section](../../11_Concepts/synchronization/critical_section/README.md)
