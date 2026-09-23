# Can two processes share a variable after all?

**Level:** 201 · anyone who needs processes and a shared counter

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** Two processes can map the same memory — `mmap` on a shared file or an anonymous shared region — and then every lesson in chapter 02 applies across processes too, with one addition: a lock inside shared memory must be a *process-shared* one, because an ordinary mutex is only meaningful inside the address space that created it.

## The question

A counter in a shared mapping, two processes each adding a million times. The lost update from chapter 02 appears between processes exactly as between threads. The page forces it, then fixes it with a process-shared mutex, an atomic in the mapping, and a semaphore — and shows what happens when an ordinary mutex is put in the shared region instead.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `memmap2` (link, not run); the std column uses `libc::mmap` in an `unsafe` block and an `AtomicU64` placed in it |
| Go | `syscall.Mmap` with `MAP_SHARED`; `sync/atomic` on the mapped bytes |
| C | `mmap(MAP_SHARED | MAP_ANONYMOUS)` before `fork`, and `PTHREAD_PROCESS_SHARED` on the mutex attribute |
| C++ | the same as C; `boost::interprocess` is the library answer (link) |
| Java | `FileChannel.map` gives a `MappedByteBuffer`; no process-shared lock without a library |
| Python | `multiprocessing.shared_memory.SharedMemory` and `multiprocessing.Lock`, which is process-shared |

## What the programs have to show

- the counter in shared memory without a lock, forced: the lost update across processes
- with a process-shared mutex, an atomic, and a semaphore: the right total
- an ordinary mutex in the shared region: the hang or the undefined behaviour, per language

## See also

- Before this: [When are processes the better workers?](../multiprocessing_instead_of_threads/README.md)
- After this: [What is a zombie process, and whose fault is it?](../a_zombie_and_an_orphan/README.md)
- [Is `total += n` safe on two threads?](../../02_Shared_State/the_lost_update/README.md)
- [When are processes the better workers?](../multiprocessing_instead_of_threads/README.md)
- Concepts: [Shared memory](../../11_Concepts/communication/shared_memory/README.md) · [Inter-process communication](../../11_Concepts/communication/ipc/README.md) · [Mutex](../../11_Concepts/synchronization/mutex/README.md) · [Atomic variable](../../11_Concepts/lock_free/atomic_variable/README.md) · [Multiprocessing](../../11_Concepts/parallelism/multiprocessing/README.md)
