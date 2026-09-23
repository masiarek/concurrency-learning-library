# How does a parent learn how its child ended?

**Level:** 201 · anyone who ran a command and did not check its status

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A child process ends with an exit status or a signal, and the parent learns which by *waiting* for it — which also frees the kernel's record of the child; a parent that never waits leaves a zombie, and a child whose parent exits first is adopted by `init`, which waits on its behalf.

## The question

Start `sh -c 'exit 3'` and read the status. Start `sh -c 'kill -9 $$'` and read that. Start a child and exit without waiting: what does `ps` show? The page runs the three, in each language's spawn API, and reads the status the way each reports it — a number, a signal name, an exception — then shows the zombie as *Real runs*.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `Command::status()` gives an `ExitStatus`; `.code()` is `None` when a signal killed it, `.signal()` on Unix says which |
| Go | `cmd.Run()` returns an `*exec.ExitError`; `ProcessState.ExitCode()` is −1 for a signal |
| C | `waitpid` and the `WIFEXITED`/`WEXITSTATUS`/`WIFSIGNALED`/`WTERMSIG` macros |
| C++ | the same as C |
| Java | `Process.waitFor()` returns the code; a signal death shows as 128 + signal |
| Python | `subprocess.run` gives `returncode`; negative for a signal |

## What the programs have to show

- the three children — exit 3, killed by 9, exit 0 — and the status as each language reports it
- the unwaited child in `ps` as `<defunct>`, as *Real runs*
- the orphan, and who its parent becomes

## See also

- Before this: [What does the child get when a process forks?](../fork_copies_the_process/README.md)
- After this: [How do two processes talk through a pipe?](../a_pipe_between_processes/README.md)
- [What does the child get when a process forks?](../fork_copies_the_process/README.md)
- [Getting a result back](../../01_Threads/getting_a_result_back/README.md)
- Concepts: [Child process](../../11_Concepts/units_of_execution/subprocess/README.md) · [Process](../../11_Concepts/units_of_execution/process/README.md) · [Join](../../11_Concepts/async/join/README.md)
