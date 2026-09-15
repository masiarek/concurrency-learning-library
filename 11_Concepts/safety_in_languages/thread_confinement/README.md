# Thread confinement

**Category:** [Safety in languages](../README.md) · **Status:** stub

**One line:** Keeping a piece of data reachable from one thread only — a GUI's main thread, a goroutine that owns its state — so that it needs no synchronization.

Also called: ownership by one thread, confinement, thread-local storage.

## How it connects

```mermaid
flowchart LR
  n_data_race["Data race"]
  n_thread_confinement["Thread confinement"]
  n_thread_confinement -->|prevents| n_data_race
  classDef center stroke-width:3px
  class n_thread_confinement center
  classDef outside stroke-dasharray: 4 3
  class n_data_race outside
```

- **Helps prevent:** [Data race](../../hazards/data_race/README.md)
- **See also:** [Message passing](../../communication/message_passing/README.md), [Thread-local storage](../../units_of_execution/thread_local_storage/README.md), [UI thread](../../units_of_execution/ui_thread/README.md)

## In each language

| | |
|---|---|
| Rust | Enforced for some types: [`Rc` ↗](https://doc.rust-lang.org/std/rc/struct.Rc.html) is not `Send`, so it cannot leave its thread; [`thread_local!` ↗](https://doc.rust-lang.org/std/macro.thread_local.html) declares per-thread statics |
| Go | By convention: [Effective Go ↗](https://go.dev/doc/effective_go#sharing) passes values on channels so that only one goroutine has access at any given time |
| C | [`_Thread_local` ↗](https://en.cppreference.com/w/c/language/storage_duration) (C11), spelled `thread_local` since C23 |
| Java | [`ThreadLocal` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/ThreadLocal.html): each thread has its own, independently initialized copy |
| Python | [`threading.local` ↗](https://docs.python.org/3/library/threading.html#thread-local-data) holds data whose values are thread specific |
| C# | [`ThreadLocal<T>` ↗](https://learn.microsoft.com/en-us/dotnet/api/system.threading.threadlocal-1) provides thread-local storage of data |
| JavaScript | [Web workers ↗](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API) receive copies of message data, not the sender's objects |

## Where to read more

- **In the books:** [*Pro TBB*](../../../10_Resources/books_cpp/README.md#voss_pro_tbb), Michael Voss, Rafael Asenjo, James Reinders — ch. 12, 'Using Work Isolation for Correctness and Performance'
- **In the books:** [*Programming Concurrency on the JVM*](../../../10_Resources/books_java/README.md#subramaniam_programming_concurrency_on_the_jvm), Venkat Subramaniam — ch. 8, 'Favoring Isolated Mutability'
- **In the books:** [*Concurrency in Go*](../../../10_Resources/books_go/README.md#cox_buday_concurrency_in_go), Katherine Cox-Buday — ch. 4, 'Concurrency Patterns in Go' → 'Confinement'
- **In the books:** [*Java Concurrency in Practice*](../../../10_Resources/books_java/README.md#goetz_java_concurrency_in_practice), Brian Goetz, Tim Peierls, Joshua Bloch, Joseph Bowbeer, David Holmes, Doug Lea — ch. 3, 'Sharing Objects' → 'Thread Confinement'
- **In the books:** [*The Go Programming Language Phrasebook*](../../../10_Resources/books_go/README.md#chisnall_go_phrasebook), David Chisnall — ch. 10, 'Concurrency Design Patterns' → 'Aliased xor Mutable'

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
