# Virtual thread

**Category:** [Units of execution](../README.md) · **Status:** stub · **Lessons:** [chapter 01, Threads](../../../01_Threads/README.md)

**One line:** Java's lightweight thread, final in JDK 21: a `Thread` that the JVM schedules onto a few carrier platform threads, cheap enough to start one per task.

Also called: Project Loom.

## How it connects

```mermaid
flowchart LR
  n_green_thread["Green threads and M:N scheduling"]
  n_virtual_thread["Virtual thread"]
  n_virtual_thread -->|is a| n_green_thread
  classDef center stroke-width:3px
  class n_virtual_thread center
  classDef outside stroke-dasharray: 4 3
  class n_green_thread outside
```

- **Is a kind of:** [Green threads and M:N scheduling](../green_thread/README.md)
- **See also:** [Daemon and detached threads](../daemon_thread/README.md)

## In each language

| | |
|---|---|
| Go | Goroutines, [multiplexed onto OS threads ↗](https://go.dev/doc/faq#goroutines), are the same idea |
| Java | [`Thread.ofVirtual()` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Thread.html#ofVirtual%28%29) and [`Executors.newVirtualThreadPerTaskExecutor()` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/Executors.html#newVirtualThreadPerTaskExecutor%28%29) |

## Where to read more

- **In this library:** [Who waits when main returns?](../../../01_Threads/who_waits_when_main_returns/README.md)
- **In this library:** [How many threads can you start?](../../../01_Threads/how_many_threads_can_you_start/README.md)
- **In this library:** [What is a goroutine, if not a thread?](../../../01_Threads/a_goroutine_is_not_a_thread/README.md)
- **In this library:** [Why can't a normal function call an async one?](../../../06_Async/function_coloring/README.md)
- **Reference:** [JEP 444: Virtual Threads ↗](https://openjdk.org/jeps/444)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
