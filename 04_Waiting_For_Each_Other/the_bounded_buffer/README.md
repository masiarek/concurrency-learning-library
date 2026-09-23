# How does a producer wait for room and a consumer wait for an item?

**Level:** 201 · anyone building a queue between threads

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A bounded buffer has two conditions — *not full* for producers, *not empty* for consumers — and getting them right is the classic exercise of this chapter, which is why Go and Rust hand you the finished thing as a channel and the rest of the languages have a queue class that hides the same two condition variables.

## The question

A queue of capacity four. Producers push, and must wait when it is full. Consumers pop, and must wait when it is empty. With one condition variable and `notify_one`, a producer can wake another producer and both go back to sleep with a consumer still waiting — the page shows that hang, then the two-condition version, then the library queue that each language provides so that nobody writes this by hand.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `std::sync::mpsc::sync_channel(4)` is the finished bounded buffer; the hand-built one with two `Condvar`s beside it |
| Go | `make(chan T, 4)`, the finished thing |
| C | hand-built with two `pthread_cond_t`s; there is no standard queue |
| C++ | hand-built with two `std::condition_variable`s; no standard concurrent queue |
| Java | `ArrayBlockingQueue(4)` with `put` and `take` |
| Python | `queue.Queue(maxsize=4)` with `put` and `get` |

## What the programs have to show

- one condition and `notify_one` with two producers and one consumer, forced into the wrong wakeup: hangs under a timeout
- two conditions: a hundred items through, in order, with the buffer never over four
- the library queue in each language doing the same

## See also

- Before this: [What is a monitor, and which languages have one?](../a_monitor_bundles_lock_and_condition/README.md)
- After this: [Why do five philosophers with five forks starve?](../the_dining_philosophers/README.md)
- [What is a monitor, and which languages have one?](../a_monitor_bundles_lock_and_condition/README.md)
- [What stops a fast producer from filling memory?](../../05_Message_Passing/a_bounded_queue_pushes_back/README.md)
- The Go library's [A buffered channel is a bounded queue ↗](https://masiarek.github.io/go-learning-library/02_Channels/a_buffered_channel_is_a_bounded_queue/index.html)
- Concepts: [Producer-consumer](../../11_Concepts/communication/producer_consumer/README.md) · [Buffered and bounded channels](../../11_Concepts/communication/bounded_channel/README.md) · [Condition variable](../../11_Concepts/synchronization/condition_variable/README.md) · [Classic synchronization problems](../../11_Concepts/synchronization/classic_synchronization_problems/README.md) · [Backpressure](../../11_Concepts/communication/backpressure/README.md)
