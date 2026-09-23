# How does one event reach every subscriber?

**Level:** 201 · anyone who wants many readers of one stream

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A channel delivers each value to *one* receiver, so a value that several threads must all see needs a different shape — a broadcast — where each subscriber has its own queue and a slow subscriber either delays the publisher, is dropped behind, or loses messages, and the choice among those three is the whole design.

## The question

A price update must reach every one of five display threads. Put it on one channel and one display gets it. The page builds the broadcast: the publisher writes to five queues, one per subscriber. Then it slows one subscriber to a crawl and shows what happens to the other four — and to the publisher — under each of the three policies.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | five `mpsc` senders, one per subscriber; `tokio::sync::broadcast` implements the lagging-receiver policy (link, not run) |
| Go | five channels, or one `sync.Cond.Broadcast` with each subscriber holding the latest value |
| C | five pipes, or a shared ring buffer with a per-reader cursor |
| C++ | five hand-built queues; or one `std::condition_variable::notify_all` with a sequence number |
| Java | five `BlockingQueue`s; `SubmissionPublisher` from `java.util.concurrent.Flow` is the standard broadcast with backpressure |
| Python | five `Queue`s; or `asyncio.Condition.notify_all` |

## What the programs have to show

- one message, five subscribers: five receipts
- one slow subscriber: under a bounded queue the publisher stalls, under drop-oldest it loses the counted number, under unbounded its queue grows
- the Java `Flow` version with its request-N backpressure

## See also

- Before this: [What if only one thread is allowed to touch the data?](../one_owner_receives_the_numbers/README.md)
- [What stops a fast producer from filling memory?](../a_bounded_queue_pushes_back/README.md)
- [How does a loop await a sequence of values that arrive over time?](../../06_Async/an_async_stream/README.md)
- Concepts: [Publish-subscribe and broadcast](../../11_Concepts/communication/publish_subscribe/README.md) · [Backpressure](../../11_Concepts/communication/backpressure/README.md) · [Channel](../../11_Concepts/communication/channel/README.md) · [Event-driven programming](../../11_Concepts/async/event_driven_programming/README.md) · [Reactive programming](../../11_Concepts/async/reactive_programming/README.md)
