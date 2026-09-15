# Blocking and non-blocking calls

**Category:** [Foundations](../README.md) · **Status:** stub · **Lessons:** chapter 06, Async *(planned)*

**One line:** A blocking call does not return until its work is done, holding the caller's thread the whole time; a non-blocking call returns at once and reports that the work is not ready yet or will finish later.

Also called: synchronous and asynchronous calls, blocking I/O, non-blocking I/O.

## How it connects


- **See also:** [Asynchrony](../asynchrony/README.md), [I/O multiplexing](../../scheduling/io_multiplexing/README.md), [I/O-bound and CPU-bound work](../io_bound_and_cpu_bound/README.md), [Polling](../../scheduling/polling/README.md)

## In each language

| | |
|---|---|
| Rust | [`TcpStream::set_nonblocking` ↗](https://doc.rust-lang.org/std/net/struct.TcpStream.html#method.set_nonblocking) makes a read that would wait return an `io::ErrorKind::WouldBlock` error instead |
| Go | A send or receive on an [unbuffered channel ↗](https://go.dev/ref/spec#Channel_types) blocks until the other side is ready |
| C | With `O_NONBLOCK` set, [`read` ↗](https://pubs.opengroup.org/onlinepubs/9799919799/functions/read.html) fails with `EAGAIN` instead of waiting |
| Java | [`SelectableChannel.configureBlocking(false)` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/nio/channels/SelectableChannel.html#configureBlocking%28boolean%29) puts an NIO channel in non-blocking mode |
| Python | [`socket.setblocking(False)` ↗](https://docs.python.org/3/library/socket.html#socket.socket.setblocking); in `asyncio`, [`asyncio.to_thread` ↗](https://docs.python.org/3/library/asyncio-task.html#asyncio.to_thread) runs a blocking function that would otherwise block the event loop |
| C# | [Asynchronous file I/O ↗](https://learn.microsoft.com/en-us/dotnet/standard/io/asynchronous-file-i-o) methods such as `ReadAsync` do the work without blocking the main thread |
| JavaScript | [`Atomics.wait` ↗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics/wait) blocks, and so cannot be used in the main thread |
| The operating system | The `O_NONBLOCK` flag of [`open(2)` ↗](https://man7.org/linux/man-pages/man2/open.2.html); readiness is then waited for with `poll` or `epoll` |

## Where to read more

- **In the books:** [*Java Concurrency in Practice*](../../../10_Resources/books_java/README.md#goetz_java_concurrency_in_practice), Brian Goetz, Tim Peierls, Joshua Bloch, Joseph Bowbeer, David Holmes, Doug Lea — ch. 15, 'Atomic Variables and Nonblocking Synchronization'
- **In the books:** [*Grokking Concurrency*](../../../10_Resources/books_general/README.md#bobrov_grokking_concurrency), Kirill Bobrov — ch. 10, 'Nonblocking I/O'
- **In the books:** [*Rust Atomics and Locks*](../../../10_Resources/books_rust/README.md#bos_rust_atomics_and_locks), Mara Bos — ch. 5, 'Building Our Own Channels' → 'Blocking'
- **In the books:** [*Parallel and Concurrent Programming in Haskell*](../../../10_Resources/books_haskell/README.md#marlow_parallel_and_concurrent_programming_in_haskell), Simon Marlow — ch. 10, 'Software Transactional Memory' → 'Blocking'
- **In the books:** [*Concurrency in .NET*](../../../10_Resources/books_csharp_dotnet/README.md#terrell_concurrency_in_dotnet), Riccardo Terrell — ch. 13, 'Recipes and design patterns for successful concurrent programming' → 'Non-blocking synchronous message-passing model'
- **In the books:** [*Python Concurrency with asyncio*](../../../10_Resources/books_python/README.md#fowler_python_concurrency_with_asyncio), Matthew Fowler — ch. 3, 'A first asyncio application' → 'Working with non-blocking sockets'
- **Notes:** [non-blocking paradigms - general - nonblocking ↗](https://docs.google.com/document/d/13kt39FBd2i3HqEEjlgEcZg4KDG8mkR4Dc6XSVsP9WRY/edit?tab=t.0)
- **Notes:** [blocked synchronously - general ↗](https://docs.google.com/document/d/11tECUJ_valZsugbPQQAtQZSi5Je_lGih2rx-RYc7PSg/edit?tab=t.0)
- **Notes:** [Synchronous blocking vs nonblocking model ↗](https://docs.google.com/document/d/1frCynKXngtPaneaZ2Kt42hxWvV36gBoEy_kL3HkZFn4/edit?tab=t.0)
- **Notes:** [Asynchronous blocking vs nonblocking model ↗](https://docs.google.com/document/d/1XtbeBZlmovmbd8JDhDpGPyz2alLl0Jm3Uc4RUVildEQ/edit?tab=t.0)
- **Notes:** [Blocking vs. non-blocking code - rust ↗](https://docs.google.com/document/u/0/d/16_DxN3at4af-2FQFy--4b8TtdQs5OLicJLJNWYRjHyQ/edit)
- **Notes:** [blocking - thread - general ↗](https://docs.google.com/document/u/0/d/1rrnzJmAZvLCezYnxTj-QriOADeDaAHnmsd03y1t1gMU/edit)
- **Reference:** [Wikipedia: Asynchronous I/O ↗](https://en.wikipedia.org/wiki/Asynchronous_I/O)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
