# Lock ordering

**Category:** [Synchronization](../README.md) · **Status:** stub · **Lessons:** [chapter 03, When locks go wrong](../../../03_When_Locks_Go_Wrong/README.md)

**One line:** Always taking locks in one agreed order, so that no cycle of tasks waiting on each other — and so no deadlock — can form.

Also called: lock hierarchy.

## How it connects

```mermaid
flowchart LR
  n_deadlock["Deadlock"]
  n_lock_ordering["Lock ordering"]
  n_lock_ordering -->|prevents| n_deadlock
  classDef center stroke-width:3px
  class n_lock_ordering center
  classDef outside stroke-dasharray: 4 3
  class n_deadlock outside
```

- **Helps prevent:** [Deadlock](../../hazards/deadlock/README.md)

## In each language

| | |
|---|---|
| C++ | [`std::lock` ↗](https://en.cppreference.com/w/cpp/thread/lock) takes several mutexes with a deadlock avoidance algorithm instead of a fixed order |
| Java | [JLS §17.1 ↗](https://docs.oracle.com/javase/specs/jls/se25/html/jls-17.html#jls-17.1) tells programs holding locks on multiple objects to use conventional deadlock-avoidance techniques |
| The operating system | Linux [lockdep ↗](https://docs.kernel.org/locking/lockdep-design.html) records which lock is taken while holding which, and reports orders that could form a cycle |
| Elsewhere | Valgrind's [Helgrind ↗](https://valgrind.org/docs/manual/hg-manual.html) monitors the order threads acquire locks in to find potential deadlocks; [ThreadSanitizer ↗](https://clang.llvm.org/docs/ThreadSanitizer.html) reports lock-order inversions (`detect_deadlocks`) |

## Where to read more

- **In this library:** [Why do two locks taken in different orders hang?](../../../03_When_Locks_Go_Wrong/two_locks_in_different_orders/README.md)
- **In this library:** [Can two threads be busy forever and get nothing done?](../../../03_When_Locks_Go_Wrong/livelock/README.md)
- **In this library:** [Why do five philosophers with five forks starve?](../../../04_Waiting_For_Each_Other/the_dining_philosophers/README.md)
- **In the books:** [*Learn Concurrent Programming with Go*](../../../10_Resources/books_go/README.md#cutajar_learn_concurrent_programming_with_go), James Cutajar — ch. 11, 'Avoiding deadlocks'
- **In the books:** [*Multi-Threaded Programming in C++*](../../../10_Resources/books_cpp/README.md#walmsley_multithreaded_programming_in_cpp), Mark Walmsley — ch. 8, 'Multiple Mutexes'
- **In the books:** [*Python Parallel Programming Cookbook*](../../../10_Resources/books_python/README.md#zaccone_python_parallel_programming_cookbook), Giancarlo Zaccone — ch. 3, 'Process-based Parallelism' → 'Avoiding deadlock problems'
- **In the books:** [*The Art of Multiprocessor Programming*](../../../10_Resources/books_general/README.md#herlihy_shavit_art_of_multiprocessor_programming), Maurice Herlihy, Nir Shavit — ch. 7, 'Spin Locks and Contention' → 'Hierarchical Locks'
- **In the books:** [*Advanced Programming in the UNIX Environment*](../../../10_Resources/books_c/README.md#stevens_rago_apue), W. Richard Stevens, Stephen A. Rago — ch. 11, 'Threads' → 'Deadlock Avoidance'
- **In the books:** [*Operating System Concepts*](../../../10_Resources/books_c/README.md#silberschatz_operating_system_concepts), Abraham Silberschatz, Peter Baer Galvin, Greg Gagne — ch. 8, 'Deadlocks' → 'Deadlock Prevention'
- **Reference:** [Wikipedia: Dining philosophers problem ↗](https://en.wikipedia.org/wiki/Dining_philosophers_problem)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
