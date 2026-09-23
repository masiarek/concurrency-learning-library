# 08 — Processes

A process shares nothing, which is the point. Threads that share memory are the subject of chapters 02 through 04; processes that share only what they are explicitly given — a pipe, a signal, a mapped file — are how the shell, the browser and Python's `multiprocessing` get isolation and, in Python's case, parallelism. This chapter covers what crosses the boundary, what happens to a child when it ends, and the one thing that never should have crossed it: a fork from a program that already had threads.

Every lesson in this chapter is a **stub**: the question, the expected answer per language and what the programs will have to show, waiting for the programs. A stub becomes a lesson when its examples run in CI and its table is replaced by what they printed.

| Lesson | The one thing |
|---|---|
| [What does the child get when a process forks?](fork_copies_the_process/README.md) | *stub* — the child gets the memory, the files and one thread — with every lock the other threads held, locked forever |
| [How does a parent learn how its child ended?](a_child_process_and_its_exit_status/README.md) | *stub* — an exit code or a signal, learned by waiting; an unwaited child is a zombie |
| [How do two processes talk through a pipe?](a_pipe_between_processes/README.md) | *stub* — a kernel buffer: the writer blocks when full, the reader when empty, zero at the end, `SIGPIPE` when nobody reads |
| [Which thread gets the signal?](a_signal_arrives_on_some_thread/README.md) | *stub* — delivered to one thread, any that has not blocked it; Go routes it to a channel, Python to the main thread |
| [When are processes the better workers?](multiprocessing_instead_of_threads/README.md) | *stub* — a copy per value that crosses, in exchange for isolation from a crash, from corruption, and from the GIL |
| [Can two processes share a variable after all?](shared_memory_between_processes/README.md) | *stub* — `mmap` the same region and chapter 02 applies across processes, with a process-shared lock |
| [What is a zombie process, and whose fault is it?](a_zombie_and_an_orphan/README.md) | *stub* — exited but not waited for; or the parent went first and `init` adopts |
