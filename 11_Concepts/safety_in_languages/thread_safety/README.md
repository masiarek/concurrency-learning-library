# Thread safety

**Category:** [Safety in languages](../README.md) · **Status:** stub · **Lessons:** [chapter 02, Shared state](../../../02_Shared_State/README.md)

**One line:** Code or data is thread-safe if it behaves correctly when used from several threads at once, without its callers adding any synchronization.

Also called: thread-safe, MT-safe.

## How it connects


- **See also:** [Concurrent data structures](../../lock_free/concurrent_data_structures/README.md), [Reentrancy](../reentrancy/README.md)

## In each language

| | |
|---|---|
| Rust | Checked by the compiler through [`Send` ↗](https://doc.rust-lang.org/std/marker/trait.Send.html) and [`Sync` ↗](https://doc.rust-lang.org/std/marker/trait.Sync.html): a type is `Sync` if and only if `&T` is `Send` |
| Go | Documented type by type: [`sync.Map` ↗](https://pkg.go.dev/sync#Map) is safe for concurrent use without extra locking, [built-in maps are not ↗](https://go.dev/doc/faq#atomic_maps) |
| C++ | [Containers ↗](https://en.cppreference.com/w/cpp/container): different containers may be used from different threads, and `const` member functions on the same container concurrently |
| Java | [`ArrayList` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/ArrayList.html) is not synchronized and suggests wrapping it with `Collections.synchronizedList` at creation |
| Python | [Thread Safety Guarantees ↗](https://docs.python.org/3/library/threadsafety.html) grades built-in types from incompatible through safe on shared objects to atomic |
| C# | The [`System.Collections.Concurrent` ↗](https://learn.microsoft.com/en-us/dotnet/standard/collections/thread-safe/) collections are thread-safe and scalable |
| Swift | [`Sendable` ↗](https://developer.apple.com/documentation/swift/sendable): a thread-safe type whose values can be shared across concurrent contexts without risk of data races |
| The operating system | [POSIX §2.9.1 ↗](https://pubs.opengroup.org/onlinepubs/9799919799/functions/V2_chap02.html#tag_16_09_01): every function is thread-safe except a listed set, such as `strtok` and `asctime` |

## Where to read more

- **In a sibling library:** [Python: The format mini-language — a formatting call that changes process-wide state ↗](https://masiarek.github.io/python-learning-library/01_Text_and_Bytes/the_format_mini_language/index.html)
- **In the books:** [*Java Concurrency in Practice*](../../../10_Resources/books_java/README.md#goetz_java_concurrency_in_practice), Brian Goetz, Tim Peierls, Joshua Bloch, Joseph Bowbeer, David Holmes, Doug Lea — ch. 2, 'Thread Safety'
- **In the books:** [*Pro Asynchronous Programming with .NET*](../../../10_Resources/books_csharp_dotnet/README.md#blewett_clymer_pro_asynchronous_programming_dotnet), Richard Blewett, Andrew Clymer — ch. 4, 'Basic Thread Safety'
- **In the books:** [*Rust Atomics and Locks*](../../../10_Resources/books_rust/README.md#bos_rust_atomics_and_locks), Mara Bos — ch. 1, 'Basics of Rust Concurrency' → 'Thread Safety: Send and Sync'
- **In the books:** [*Programming with POSIX Threads*](../../../10_Resources/books_c/README.md#butenhof_programming_with_posix_threads), David R. Butenhof — ch. 6, 'POSIX Adjusts to Threads' → 'Thread-safe functions'
- **In the books:** [*Concurrency with Modern C++*](../../../10_Resources/books_cpp/README.md#grimm_concurrency_with_modern_cpp), Rainer Grimm — ch. 5, 'Case Studies' → 'Thread-Safe Initialisation of a Singleton'
- **In the books:** [*The Art of Concurrency*](../../../10_Resources/books_general/README.md#breshears_art_of_concurrency), Clay Breshears — ch. 4, 'Eight Simple Rules for Designing Multithreaded Applications' → 'Rule 4: Make Use of Thread-Safe Libraries Wherever Possible'
- **Notes:** [threads - general - thread safety ↗](https://docs.google.com/document/d/1cOzooElU4zoopDmG959t42v0O--IXdGOWIPWtVmJ0ag/edit?tab=t.0)
- **Reference:** [Wikipedia: Thread safety ↗](https://en.wikipedia.org/wiki/Thread_safety)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
