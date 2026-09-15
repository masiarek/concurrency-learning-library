# Child process

**Category:** [Units of execution](../README.md) · **Status:** stub · **Lessons:** chapter 08, Processes *(planned)*

**One line:** A process started by another program, which can pass it input, read its output, wait for it and learn how it ended.

Also called: subprocess, spawn, fork and exec.

## How it connects

```mermaid
flowchart LR
  n_subprocess["Child process"]
  n_process["Process"]
  n_subprocess -->|is a| n_process
  classDef center stroke-width:3px
  class n_subprocess center
  classDef outside stroke-dasharray: 4 3
  class n_process outside
```

- **Is a kind of:** [Process](../process/README.md)
- **See also:** [Inter-process communication](../../communication/ipc/README.md)

## In each language

| | |
|---|---|
| Rust | [`std::process::Command` ↗](https://doc.rust-lang.org/std/process/struct.Command.html) |
| Go | [`os/exec` ↗](https://pkg.go.dev/os/exec) |
| C | [`posix_spawn` ↗](https://pubs.opengroup.org/onlinepubs/9799919799/functions/posix_spawn.html), or `fork` then `exec`, and [`waitpid` ↗](https://pubs.opengroup.org/onlinepubs/9799919799/functions/waitpid.html) for the exit status |
| Java | [`ProcessBuilder` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/ProcessBuilder.html) |
| Python | [`subprocess` ↗](https://docs.python.org/3/library/subprocess.html), and [asyncio subprocesses ↗](https://docs.python.org/3/library/asyncio-subprocess.html) for use inside an event loop |
| JavaScript | Node's [`child_process` ↗](https://nodejs.org/api/child_process.html) |

## Where to read more

- **In this library:** [Who waits when main returns?](../../../01_Threads/who_waits_when_main_returns/README.md)
- **In the books:** [*Python Concurrency with asyncio*](../../../10_Resources/books_python/README.md#fowler_python_concurrency_with_asyncio), Matthew Fowler — ch. 13, 'Managing subprocesses'
- **In the books:** [*Python Asyncio Jump-Start*](../../../10_Resources/books_python/README.md#brownlee_python_asyncio_jump_start), Jason Brownlee — ch. 6, 'Subprocesses and Streams'
- **In the books:** [*JavaScript Concurrency*](../../../10_Resources/books_javascript/README.md#boduch_javascript_concurrency), Adam Boduch — ch. 9, 'Advanced NodeJS Concurrency' → 'Child Processes'
- **In the books:** [*Effective Python*](../../../10_Resources/books_python/README.md#slatkin_effective_python), Brett Slatkin — ch. 7, 'Concurrency and Parallelism' → 'Item 52: Use subprocess to Manage Child Processes'
- **In the books:** [*Python in a Nutshell*](../../../10_Resources/books_python/README.md#martelli_python_in_a_nutshell), Alex Martelli, Anna Ravenscroft, Steve Holden — ch. 14, 'Threads and Processes' → 'Running Other Programs'
- **Reference:** [Wikipedia: Child process ↗](https://en.wikipedia.org/wiki/Child_process)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
