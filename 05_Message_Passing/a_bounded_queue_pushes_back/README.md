# What stops a fast producer from filling memory?

**Level:** 201 · anyone whose queue grew until the process was killed

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A bounded queue makes a producer that is faster than its consumer *wait*, which is backpressure, and an unbounded one lets it run ahead until the difference between the two rates has consumed all the memory there is; the bound is not a tuning parameter but the thing that keeps the program's memory finite.

## The question

A producer makes an item every millisecond; the consumer takes ten to handle one. After a second, an unbounded queue holds nine hundred items. After a minute, fifty-four thousand. The page runs both for a fixed time and reports the queue's peak length: the bound, or a number that grows with the run. Then it shows what the producer does when it is blocked — and the third option, dropping.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `sync_channel(8)` blocks the sender at eight; `channel()` grows without limit |
| Go | `make(chan T, 8)` blocks at eight; there is no unbounded channel, on purpose |
| C | a pipe blocks the writer at the kernel's buffer size |
| C++ | a hand-built queue with a capacity and two condition variables |
| Java | `ArrayBlockingQueue(8)` blocks `put`; `offer` returns `false` instead; `LinkedBlockingQueue` grows |
| Python | `Queue(maxsize=8)` blocks `put`; `put_nowait` raises `Full` |

## What the programs have to show

- the fast producer, slow consumer, one second: peak queue length under a bound of eight and under no bound
- the blocked producer's wall time, and the dropped-item count under `offer`/`put_nowait`
- a *Real runs* fence of memory after a minute unbounded

## See also

- Before this: [Does a send return before anyone receives?](../an_unbuffered_send_waits/README.md)
- After this: [How does a receiver learn that no more values will come?](../closing_a_channel/README.md)
- [Does a send return before anyone receives?](../an_unbuffered_send_waits/README.md)
- [How does a producer wait for room and a consumer wait for an item?](../../04_Waiting_For_Each_Other/the_bounded_buffer/README.md)
- The Go library's [A buffered channel is a bounded queue ↗](https://masiarek.github.io/go-learning-library/02_Channels/a_buffered_channel_is_a_bounded_queue/index.html)
- The Rust library's [Backpressure ↗](https://masiarek.github.io/rust-learning-library/35_Async/building_minidb/backpressure/index.html)
- Concepts: [Buffered and bounded channels](../../11_Concepts/communication/bounded_channel/README.md) · [Backpressure](../../11_Concepts/communication/backpressure/README.md) · [Producer-consumer](../../11_Concepts/communication/producer_consumer/README.md) · [Channel](../../11_Concepts/communication/channel/README.md)
