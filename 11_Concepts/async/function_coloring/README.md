# Function coloring

**Category:** [Async](../README.md) · **Status:** stub · **Lessons:** chapter 06, Async *(planned)*

**One line:** An async function can call a sync one, but not the other way round without help, so async-ness spreads up the call graph and splits libraries into two colors.

Also called: what color is your function, sync and async functions.

## How it connects


- **See also:** [Async and await](../async_await/README.md), [Blocking the event loop](../blocking_the_event_loop/README.md)

## In each language

| | |
|---|---|
| Rust | futures are lazy until awaited, and Rust bundles no runtime, so sync code needs one from a crate to run an async function ([Book ↗](https://doc.rust-lang.org/book/ch17-01-futures-and-syntax.html)) |
| Go | no colors: any function can run in its own goroutine with a [`go` statement ↗](https://go.dev/ref/spec#Go_statements), and a blocking call does not hold up the other goroutines ([FAQ ↗](https://go.dev/doc/faq#goroutines)) |
| Java | [JEP 444 ↗](https://openjdk.org/jeps/444) chose virtual threads over async/await because async/await would split the world between APIs for threads and APIs for coroutines |
| Python | `await`, `async for` and `async with` are allowed only in a [coroutine function ↗](https://docs.python.org/3/reference/compound_stmts.html#coroutine-function-definition); sync code starts one with [`asyncio.run` ↗](https://docs.python.org/3/library/asyncio-runner.html#asyncio.run), and async code can hand a blocking call to [`asyncio.to_thread` ↗](https://docs.python.org/3/library/asyncio-task.html#asyncio.to_thread) |
| JavaScript | [`await` ↗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await) is allowed only inside async functions and at the top level of a module |
| Kotlin | a suspending function can be called only from another suspending function ([basics ↗](https://kotlinlang.org/docs/coroutines-basics.html)); [`runBlocking` ↗](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/run-blocking.html) bridges from blocking code by blocking the thread |

## Where to read more

- **Notes:** [async and ffi - async & FFI - not exactly a love story ↗](https://docs.google.com/document/d/1vBvNkxdRh2b88PkKupNiZssYZAyUFY3IFQ1UEgbfa-Y/edit?tab=t.0)
- **Reference:** [Bob Nystrom: What Color is Your Function? ↗](https://journal.stuffwithstuff.com/2015/02/01/what-color-is-your-function/)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
