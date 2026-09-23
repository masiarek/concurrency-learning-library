# Is a thread-local variable really one per thread?

**Level:** 201 · anyone who reached for a global and was told to make it thread-local instead

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A thread-local variable is a separate copy in every thread, initialized on that thread's first use and destroyed when the thread ends — which is what makes it safe without a lock and is also why a value set in `main` is invisible to a worker; Go has no such thing on purpose, and its answer is to pass a `context.Context`.

## The question

Two threads write a thread-local counter and each reads its own back. Then `main` sets the variable before starting the workers, and the workers read it. What do they see? When does each copy come into existence, when does it go, and what does the destructor or finalizer run on? This is the lesson behind `errno`, behind Java's `ThreadLocal` in a thread pool, and behind Go's refusal to have any of it.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `thread_local!` with a lazily initialized `static`; each thread gets its own, dropped at thread exit |
| Go | none: goroutines have no identity to key on, and the Go authors say to pass values explicitly |
| C | `_Thread_local` (C11) — one copy per thread, zero-initialized |
| C++ | `thread_local` (C++11), constructed on first use in that thread, destroyed at thread exit |
| Java | `ThreadLocal<T>` with `withInitial`; a pooled thread keeps its value between tasks unless `remove()` is called |
| Python | `threading.local()`: an object whose attributes are per thread |

## What the programs have to show

- each worker incrementing its copy three times and handing back what it saw: 3, not 6
- `main` setting the variable to 100 first, and each worker still reading its own initial value
- the thread-pool trap in Java: a task that sets the value, and the next task on the same pooled thread reading it

## See also

- Before this: [How many threads can you start?](../how_many_threads_can_you_start/README.md)
- After this: [Why reuse a thread at all?](../reusing_threads_in_a_pool/README.md)
- [Keeping every update](../../02_Shared_State/keeping_every_update/README.md)
- Concepts: [Thread-local storage](../../11_Concepts/units_of_execution/thread_local_storage/README.md) · [Thread confinement](../../11_Concepts/safety_in_languages/thread_confinement/README.md) · [Thread](../../11_Concepts/units_of_execution/thread/README.md)
