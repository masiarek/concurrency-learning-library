# Futex

**Category:** [Synchronization](../README.md) · **Status:** stub

**One line:** A Linux kernel facility for building locks: the uncontended case is a single atomic operation in user space, and only a thread that has to wait enters the kernel.

Also called: fast user-space mutex, WaitOnAddress.

## How it connects

```mermaid
flowchart LR
  n_futex["Futex"]
  n_mutex["Mutex"]
  n_mutex -->|uses| n_futex
  classDef center stroke-width:3px
  class n_futex center
  classDef outside stroke-dasharray: 4 3
  class n_mutex outside
```

- **Is used by:** [Mutex](../mutex/README.md)

## In each language

| | |
|---|---|
| C++ | [`std::atomic<T>::wait` ↗](https://en.cppreference.com/w/cpp/atomic/atomic/wait) and `notify_one` (C++20) block a thread until the atomic is notified and its value has changed |
| JavaScript | [`Atomics.wait` and `Atomics.notify` ↗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics) are modeled on Linux futexes |
| The operating system | Linux [futex(7) ↗](https://man7.org/linux/man-pages/man7/futex.7.html): the uncontended case happens entirely in user space; Windows has [`WaitOnAddress` ↗](https://learn.microsoft.com/en-us/windows/win32/api/synchapi/nf-synchapi-waitonaddress), which waits for the value at an address to change |

## Where to read more

- **In this library:** [What does a spinlock cost when there is nowhere to spin?](../../../03_When_Locks_Go_Wrong/a_spinlock_on_one_core/README.md)
- **In the books:** [*Learn Concurrent Programming with Go*](../../../10_Resources/books_go/README.md#cutajar_learn_concurrent_programming_with_go), James Cutajar — ch. 12, 'Atomics, spin locks, and futexes'
- **Reference:** [Linux man page: futex(2) ↗](https://man7.org/linux/man-pages/man2/futex.2.html)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
