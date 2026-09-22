# Object lifetime

**Category:** [Safety in languages](../README.md) · **Status:** stub · **Lessons:** [chapter 01, Threads](../../../01_Threads/README.md)

**One line:** The span in which a value's storage is valid, and the question of who guarantees that every reference to it is dropped first — the compiler, the programmer, or a garbage collector.

Also called: lifetime, storage duration, extent.

## How it connects


- **See also:** [Dangling pointer](../../hazards/dangling_pointer/README.md), [Detached thread](../../units_of_execution/detached_thread/README.md), [Escape analysis](../escape_analysis/README.md), [Scoped thread](../../units_of_execution/scoped_thread/README.md), [Thread confinement](../thread_confinement/README.md)

## In each language

| | |
|---|---|
| Rust | [Lifetimes ↗](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html) are part of a reference's type, and `'static` means the reference may outlive any caller |
| Go | Decided by the compiler: the [FAQ ↗](https://go.dev/doc/faq#stack_or_heap) says a local whose address escapes is allocated on the heap, and the collector frees it |
| C | [Lifetime ↗](https://en.cppreference.com/w/c/language/lifetime): an automatic object's lifetime ends when its block does, and a pointer to it is then indeterminate |
| C++ | [Lifetime ↗](https://en.cppreference.com/w/cpp/language/lifetime), and [storage duration ↗](https://en.cppreference.com/w/cpp/language/storage_duration) for where it comes from |
| Java | Decided by reachability: [JLS 12.6 ↗](https://docs.oracle.com/javase/specs/jls/se25/html/jls-12.html#jls-12.6) says an object is finalizable once it is no longer reachable |
| Python | [Reference counting and the cyclic collector ↗](https://docs.python.org/3/library/gc.html); [`weakref` ↗](https://docs.python.org/3/library/weakref.html) holds a reference that does not keep the object alive |

## Where to read more

- **In this library:** [Can a thread borrow a local variable?](../../../01_Threads/lending_a_local_to_a_thread/README.md)
- **Reference:** [Wikipedia: Object lifetime ↗](https://en.wikipedia.org/wiki/Object_lifetime)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
