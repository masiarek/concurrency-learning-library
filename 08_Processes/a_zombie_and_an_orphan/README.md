# What is a zombie process, and whose fault is it?

**Level:** 201 · anyone who saw `<defunct>` in `ps`

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A child that has exited but not been waited for is a zombie — its memory is gone, its exit status is not, and it occupies a process-table slot until the parent waits or dies — and an orphan is the reverse, a child whose parent exited first, which the system reparents to `init` so that someone will eventually wait for it.

## The question

Start a child, let it exit, and do not wait. `ps` shows it `<defunct>`. Start a thousand of them and the process table fills. The page makes one zombie in each language's spawn API, shows it in `ps` as *Real runs*, then reaps it, and shows the two ways to never make one: wait, or set `SIGCHLD` to ignore. Then the orphan, and its new parent's id.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | a `Child` not `wait`ed is a zombie; the docs say so; dropping a `Child` does not wait |
| Go | `cmd.Start()` without `Wait()` leaves a zombie |
| C | `fork` without `waitpid`; `signal(SIGCHLD, SIG_IGN)` makes the kernel reap |
| C++ | the same as C |
| Java | `Process` not `waitFor`ed; the JVM's reaper thread waits on its behalf, so there is no zombie |
| Python | `Popen` without `wait()`; `Popen.__del__` warns `ResourceWarning: subprocess N is still running` |

## What the programs have to show

- the zombie in `ps` output, abridged, as *Real runs*, per language that leaves one
- the reap, and the status recovered from it
- the orphan's parent pid before and after the parent exits

## See also

- Before this: [Can two processes share a variable after all?](../shared_memory_between_processes/README.md)
- [How does a parent learn how its child ended?](../a_child_process_and_its_exit_status/README.md)
- [Who waits when main returns?](../../01_Threads/who_waits_when_main_returns/README.md)
- Concepts: [Process](../../11_Concepts/units_of_execution/process/README.md) · [Child process](../../11_Concepts/units_of_execution/subprocess/README.md) · [Leaked tasks](../../11_Concepts/hazards/task_leak/README.md) · [Signals](../../11_Concepts/communication/signals/README.md)
