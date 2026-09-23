# I/O-bound and CPU-bound work

**Category:** [Foundations](../README.md) · **Status:** stub · **Lessons:** [chapter 07, Parallelism](../../../07_Parallelism/README.md)

**One line:** Work that spends its time waiting for disks and networks gains from concurrency even on one core; work that spends its time computing gains only from parallelism.

Also called: I/O-bound, CPU-bound.

## How it connects


- **See also:** [Blocking and non-blocking calls](../blocking_and_nonblocking/README.md), [Global interpreter lock](../../parallelism/gil/README.md), [Parallelism](../parallelism/README.md)

## In each language

| | |
|---|---|
| Rust | [`tokio::task::spawn_blocking` ↗](https://docs.rs/tokio/latest/tokio/task/fn.spawn_blocking.html) moves blocking work off the async worker threads |
| Java | [Virtual threads ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Thread.html#virtual-threads) suit tasks that spend most of their time blocked on I/O, not long CPU-intensive work |
| Python | The [`threading` ↗](https://docs.python.org/3/library/threading.html) docs advise `multiprocessing` or `ProcessPoolExecutor` for CPU-bound work, and threads for I/O-bound tasks, because of the GIL |
| C# | [Asynchronous programming scenarios ↗](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/async-scenarios) separates I/O-bound work (`await` the I/O call) from CPU-bound work (`await Task.Run`) |
| Kotlin | [`Dispatchers.IO` ↗](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-dispatchers/-i-o.html) is for offloading blocking I/O; [`Dispatchers.Default` ↗](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-dispatchers/-default.html) uses at most one thread per CPU core (at least two) |
| Erlang and Elixir | A native function that cannot finish within a millisecond is marked dirty and runs on [dirty CPU or dirty I/O schedulers ↗](https://www.erlang.org/doc/apps/erts/erl_nif.html#dirty_nifs), apart from the ordinary ones |

## Where to read more

- **In this library:** [What does one blocking call do to every other task?](../../../06_Async/blocking_the_event_loop/README.md)
- **In this library:** [How does one thread watch a thousand sockets?](../../../06_Async/io_multiplexing_under_the_loop/README.md)
- **In this library:** [How much faster is real work on eight threads?](../../../07_Parallelism/cpu_bound_speedup/README.md)
- **In this library:** [Why do Python threads take turns?](../../../07_Parallelism/the_gil_and_free_threaded_python/README.md)
- **In this library:** [How many workers should a pool have?](../../../07_Parallelism/how_many_workers/README.md)
- **In the books:** [*Asynchronous Programming in Rust*](../../../10_Resources/books_rust/README.md#samson_asynchronous_programming_in_rust), Carl Fredrik Samson — ch. 6, 'Futures in Rust' → 'I/O vs CPU-intensive tasks'
- **In the books:** [*Python Concurrency with asyncio*](../../../10_Resources/books_python/README.md#fowler_python_concurrency_with_asyncio), Matthew Fowler — ch. 1, 'Getting to know asyncio' → 'What is I/O-bound and what is CPU-bound?'
- **In the books:** [*Grokking Concurrency*](../../../10_Resources/books_general/README.md#bobrov_grokking_concurrency), Kirill Bobrov — ch. 6, 'Multitasking' → 'CPU-bound and I/O-bound applications'
- **In the books:** [*Python in Practice*](../../../10_Resources/books_python/README.md#summerfield_python_in_practice), Mark Summerfield — ch. 4, 'High-Level Concurrency in Python' → 'CPU-Bound Concurrency'
- **Notes:** [CPU-Bound Tasks ↗](https://docs.google.com/document/d/1xw8T95umBjyeuxNkw4LM-WU_igooayxL6Ip-Cgu0yBk/edit?tab=t.0)
- **Notes:** [I/O-bound tasks ↗](https://docs.google.com/document/u/0/d/1jgLIEhaiavVwamvco5Sr0R-Diim7LY3TrclyFXmESZE/edit)
- **Notes:** [I/O bottlenecks - general ↗](https://docs.google.com/document/d/1RjYTibpNuLPzaR3ZiL0_sPr2e3hVsLTAUqmfZ_jCmgI/edit?tab=t.0)
- **Reference:** [Wikipedia: CPU-bound ↗](https://en.wikipedia.org/wiki/CPU-bound)
- **Reference:** [Wikipedia: I/O bound ↗](https://en.wikipedia.org/wiki/I/O_bound)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
