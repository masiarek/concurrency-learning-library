# Happens-before

**Category:** [Lock-free](../README.md) · **Status:** stub · **Lessons:** chapter 02, Shared state *(planned)*

**One line:** The rule a memory model states for when one thread is guaranteed to see another thread's write: only when synchronization orders the write before the read.

Also called: memory model, Java Memory Model, Go memory model, synchronized before.

## How it connects


- **See also:** [Data race](../../hazards/data_race/README.md), [Weak memory models and reordering](../../hazards/weak_memory_model/README.md)

## In each language

| | |
|---|---|
| Rust | [`std::sync::atomic` ↗](https://doc.rust-lang.org/std/sync/atomic/index.html) states a memory model for atomic accesses: conflicting accesses are fine only if one happens-before the other |
| Go | [The Go Memory Model ↗](https://go.dev/ref/mem): happens-before is the transitive closure of sequenced-before and synchronized-before, and each `sync` type documents what it synchronizes before what |
| C | [Memory model ↗](https://en.cppreference.com/w/c/language/memory_model): conflicting evaluations are no data race if one happens-before the other, as `mtx_unlock` does before the next `mtx_lock` |
| C++ | [Multi-threaded executions and data races ↗](https://en.cppreference.com/w/cpp/language/multithread): releasing a `std::mutex` happens-before another thread acquires it |
| Java | [JLS §17.4.5 Happens-before Order ↗](https://docs.oracle.com/javase/specs/jls/se25/html/jls-17.html#jls-17.4.5); the [`java.util.concurrent` memory consistency properties ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/package-summary.html#MemoryVisibility) list which actions happen-before which |
| Kotlin | [`Mutex` ↗](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.sync/-mutex/): an unlock happens-before every later successful lock, like `synchronized` on the JVM |

## Where to read more

- **In the books:** [*Effective Concurrency in Go*](../../../10_Resources/books_go/README.md#serdar_effective_concurrency_in_go), Burak Serdar — ch. 3, 'The Go Memory Model' → 'The happened-before relationship between memory operations'
- **In the books:** [*Rust Atomics and Locks*](../../../10_Resources/books_rust/README.md#bos_rust_atomics_and_locks), Mara Bos — ch. 3, 'Memory Ordering' → 'Happens-Before Relationship'
- **In the books:** [*Hands-On Concurrency with Rust*](../../../10_Resources/books_rust/README.md#troutwine_hands_on_concurrency_with_rust), Brian L. Troutwine — ch. 6, 'Atomics – the Primitives of Synchronization' → 'Memory ordering – happens-before and synchronizes-with'
- **Reference:** [The Go Memory Model ↗](https://go.dev/ref/mem)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
