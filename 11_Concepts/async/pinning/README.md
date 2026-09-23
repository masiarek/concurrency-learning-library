# Pinning

**Category:** [Async](../README.md) · **Status:** stub · **Lessons:** [chapter 06, Async](../../../06_Async/README.md)

**One line:** Rust's guarantee that a value will not move in memory, needed because an async state machine may hold pointers into itself.

Also called: Pin, Unpin.

## How it connects


- **See also:** [Async functions as state machines](../async_state_machine/README.md)

## In each language

| | |
|---|---|
| Rust | [`Pin` ↗](https://doc.rust-lang.org/std/pin/struct.Pin.html) keeps a pointee from being moved unless it implements `Unpin` |
| C# | a different pinning: [`fixed` ↗](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/fixed) stops the garbage collector from relocating a variable while a pointer to it is in use, and so does a [`Pinned` ↗](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.interopservices.gchandletype) `GCHandle` |

## Where to read more

- **In the books:** [*Asynchronous Programming in Rust*](../../../10_Resources/books_rust/README.md#samson_asynchronous_programming_in_rust), Carl Fredrik Samson — ch. 9, 'Coroutines, Self-Referential Structs, and Pinning'
- **In the books:** [*Programming Rust*](../../../10_Resources/books_rust/README.md#blandy_programming_rust), Jim Blandy, Jason Orendorff, Leonora F. S. Tindall — ch. 20, 'Asynchronous Programming' → 'Pinning'
- **Reference:** [Rust std: module pin ↗](https://doc.rust-lang.org/std/pin/index.html)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
