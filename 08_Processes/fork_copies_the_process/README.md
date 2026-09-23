# What does the child get when a process forks?

**Level:** 201 · anyone who called `fork` from a program with threads

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** `fork` copies the calling process — its memory, its open files, its one calling thread and not the others — so a child forked from a multithreaded program has every mutex the other threads held locked forever with no thread to unlock it, which is why every language here except C either forbids `fork` after threads exist or warns about it, and why the modern way to start a program is `posix_spawn`.

## The question

A process with a counter forks. Parent and child each add one. Each prints its counter: 1 and 1, not 2 — the memory was copied. Then the same with a second thread holding a lock at the moment of the fork: the child tries to take the lock and hangs. The page runs both, then shows what each language does instead of a raw fork.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `libc::fork` is unsafe and `std::process::Command` uses `posix_spawn` or fork+exec at once |
| Go | no `fork` in the standard library; `os/exec` and `syscall.ForkExec` spawn a new program |
| C | `fork()`; the page's C column is the reference, including the locked-mutex child |
| C++ | the same as C; `std::system` and no standard spawn until C++26 (link) |
| Java | no `fork`; `ProcessBuilder` spawns a new program |
| Python | `os.fork()` works; `multiprocessing`'s default start method became `forkserver` on Linux in 3.14 because of exactly this |

## What the programs have to show

- parent and child each incrementing a copied counter: 1 and 1
- the fork with a locked mutex in another thread: the child hangs, under a timeout driver
- `multiprocessing.get_start_method()` printed per platform

## See also

- After this: [How does a parent learn how its child ended?](../a_child_process_and_its_exit_status/README.md)
- [How does a parent learn how its child ended?](../a_child_process_and_its_exit_status/README.md)
- [When are processes the better workers?](../multiprocessing_instead_of_threads/README.md)
- Concepts: [Process](../../11_Concepts/units_of_execution/process/README.md) · [Multiprocessing](../../11_Concepts/parallelism/multiprocessing/README.md) · [Child process](../../11_Concepts/units_of_execution/subprocess/README.md) · [Deadlock](../../11_Concepts/hazards/deadlock/README.md)
