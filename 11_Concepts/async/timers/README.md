# Timers and tickers

**Category:** [Async](../README.md) · **Status:** stub · **Lessons:** chapter 06, Async *(planned)*

**One line:** A runtime facility that fires once after a delay, or repeatedly at an interval, and delivers it as a callback, a value on a channel, or something to await.

Also called: ticker, interval, setTimeout.

## How it connects


- **See also:** [Event loop](../../scheduling/event_loop/README.md), [Timeout](../timeout/README.md)

## In each language

| | |
|---|---|
| Rust | Tokio's [`time` ↗](https://docs.rs/tokio/latest/tokio/time/index.html) module: `sleep`, `interval` and `timeout` |
| Go | [`time.Timer` ↗](https://pkg.go.dev/time#Timer) and [`time.Ticker` ↗](https://pkg.go.dev/time#Ticker), each delivering on a channel |
| Java | [`ScheduledExecutorService` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/ScheduledExecutorService.html) runs tasks after a delay or periodically |
| Python | [`loop.call_later` ↗](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_later) on the event loop, and [`threading.Timer` ↗](https://docs.python.org/3/library/threading.html#timer-objects) for threads |
| C# | [`PeriodicTimer` ↗](https://learn.microsoft.com/en-us/dotnet/api/system.threading.periodictimer), whose ticks are awaited |
| JavaScript | [`setTimeout` ↗](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout) and `setInterval` |
| The operating system | [`timerfd_create` ↗](https://man7.org/linux/man-pages/man2/timerfd_create.2.html) makes a timer readable as a file descriptor, so an event loop can wait on it |

## Where to read more

- **In a sibling library:** [Go: A timeout is a channel ↗](https://masiarek.github.io/go-learning-library/03_Select/a_timeout_is_a_channel/index.html)
- **In the books:** [*Effective Concurrency in Go*](../../../10_Resources/books_go/README.md#serdar_effective_concurrency_in_go), Burak Serdar — ch. 7, 'Timers and Tickers'
- **In the books:** [*Combine: Asynchronous Programming with Swift*](../../../10_Resources/books_swift/README.md#kodeco_combine_asynchronous_programming_swift), Shai Mishali, Florent Pillet, Marin Todorov, Scott Gardner — ch. 11, 'Timers'
- **In the books:** [*Pro Asynchronous Programming with .NET*](../../../10_Resources/books_csharp_dotnet/README.md#blewett_clymer_pro_asynchronous_programming_dotnet), Richard Blewett, Andrew Clymer — ch. 6, 'Asynchronous UI' → 'UI Timers'
- **In the books:** [*JavaScript Concurrency*](../../../10_Resources/books_javascript/README.md#boduch_javascript_concurrency), Adam Boduch — ch. 2, 'The JavaScript Execution Model' → 'Creating tasks using timers'
- **In the books:** [*Hands-On RTOS with Microcontrollers*](../../../10_Resources/books_c/README.md#amos_hands_on_rtos), Brian Amos — ch. 8, 'Protecting Data and Synchronizing Tasks' → 'Using software timers'
- **In the books:** [*C# 10 in a Nutshell*](../../../10_Resources/books_csharp_dotnet/README.md#albahari_csharp_in_a_nutshell), Joseph Albahari — ch. 21, 'Advanced Threading' → 'Timers'

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
