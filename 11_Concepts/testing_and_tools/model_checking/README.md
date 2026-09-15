# Model checking

**Category:** [Testing and tools](../README.md) · **Status:** stub · **Lessons:** chapter 09, Testing and tools *(planned)*

**One line:** Exploring every state and interleaving of a model of a program — in TLA+, SPIN, or loom — to prove a property or produce a counterexample.

Also called: TLA+, SPIN, Lincheck.

## How it connects


- **See also:** [Deterministic scheduling for tests](../deterministic_testing/README.md)

## In each language

| | |
|---|---|
| Rust | [loom ↗](https://docs.rs/loom/latest/loom/) simulates the operating system's scheduler and Rust's memory model so that all possible valid behaviours are explored |
| Kotlin | [Lincheck ↗](https://kotlinlang.org/docs/lincheck-guide.html) model checking inserts thread switches at synchronization points and shared memory accesses, and reports an exact failing trace |
| Elsewhere | [TLA+ ↗](https://lamport.azurewebsites.net/tla/tla.html) models concurrent and distributed systems; [Spin ↗](https://spinroot.com/spin/whatispin.html) formally verifies multi-threaded software |

## Where to read more

- **In the books:** [*The Art of Concurrency*](../../../10_Resources/books_general/README.md#breshears_art_of_concurrency), Clay Breshears — ch. 3, 'Proving Correctness and Measuring Performance'
- **Reference:** [Wikipedia: Model checking ↗](https://en.wikipedia.org/wiki/Model_checking)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
