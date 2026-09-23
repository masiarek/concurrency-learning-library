# Busy waiting

**Category:** [Scheduling](../README.md) · **Status:** stub

**One line:** Waiting for a condition by checking it in a loop, burning CPU the whole time; worth it for a few nanoseconds inside a spinlock, wasteful for anything longer.

Also called: spinning, spin-waiting, spin loop.

## How it connects

```mermaid
flowchart LR
  n_busy_waiting["Busy waiting"]
  n_condition_variable["Condition variable"]
  n_spinlock["Spinlock"]
  n_busy_waiting ---|or| n_condition_variable
  n_spinlock -->|uses| n_busy_waiting
  classDef center stroke-width:3px
  class n_busy_waiting center
  classDef outside stroke-dasharray: 4 3
  class n_condition_variable,n_spinlock outside
```

- **Is used by:** [Spinlock](../../synchronization/spinlock/README.md)
- **An alternative to:** [Condition variable](../../synchronization/condition_variable/README.md)
- **See also:** [Polling](../polling/README.md), [Spinlock](../../synchronization/spinlock/README.md)

## In each language

| | |
|---|---|
| Rust | [`std::hint::spin_loop` ↗](https://doc.rust-lang.org/std/hint/fn.spin_loop.html) tells the processor it is in a spin loop |
| Java | [`Thread.onSpinWait` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Thread.html#onSpinWait%28%29) tells the runtime that the caller is busy-waiting |
| C# | [`SpinWait` ↗](https://learn.microsoft.com/en-us/dotnet/api/system.threading.spinwait) spins for a while and then starts yielding |

## Where to read more

- **In this library:** [What does a sleep promise, and what does a yield?](../../../01_Threads/sleep_and_yield/README.md)
- **In this library:** [What does a spinlock cost when there is nowhere to spin?](../../../03_When_Locks_Go_Wrong/a_spinlock_on_one_core/README.md)
- **In this library:** [How does a thread wait for something to become true?](../../../04_Waiting_For_Each_Other/waiting_for_a_condition/README.md)
- **In the books:** [*Learn Concurrent Programming with Go*](../../../10_Resources/books_go/README.md#cutajar_learn_concurrent_programming_with_go), James Cutajar — ch. 12, 'Atomics, spin locks, and futexes' → 'Improving on spin locking'
- **Notes:** [busy-waiting ↗](https://docs.google.com/document/u/0/d/1VSUTXXyFhpf6E3ZTYXWKmkOTU-Dq73aqa6kX4EFRiNY/edit)
- **Reference:** [Wikipedia: Busy waiting ↗](https://en.wikipedia.org/wiki/Busy_waiting)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
