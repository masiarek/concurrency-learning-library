# How does a receiver learn that no more values will come?

**Level:** 201 · anyone whose consumer loop never ended

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A consumer looping on a channel needs a signal that the producer is done, and the languages give three: Go closes the channel and a receive then returns the zero value with `ok == false`, Rust drops the last sender and `recv` returns `Err`, and the queue-based languages have no close at all, so a sentinel value — a poison pill — has to be sent by hand.

## The question

`for item in channel` — how does the loop end? In Go, when the channel is closed and drained. In Rust, when every `Sender` has been dropped. In Java and Python, never, unless the producer sends something the consumer recognizes as *the end*. The page runs three producers and one consumer to completion in each language, and then shows the two mistakes: closing a Go channel twice, and forgetting to drop a cloned Rust sender.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `for x in rx` ends when every `Sender` is dropped; a forgotten clone keeps it open forever |
| Go | `close(ch)`; `range` ends after the buffer drains; a second `close` panics, a send after close panics |
| C | closing the write end of a pipe makes `read` return 0 |
| C++ | no close; a sentinel, or a `stop` flag checked under the queue's lock |
| Java | no close on `BlockingQueue`; a poison pill, or a `CompletableFuture` per item |
| Python | no close on `Queue`; a `None` sentinel, or `shutdown()` since Python 3.13 |

## What the programs have to show

- three producers, one consumer, the consumer's loop ending on its own: the count received
- the forgotten sender clone under a timeout driver: the hang, and the line that fixes it
- Go's double close and send-after-close as panics with their exact messages

## See also

- Before this: [What stops a fast producer from filling memory?](../a_bounded_queue_pushes_back/README.md)
- After this: [How does one thread wait on several channels at once?](../waiting_on_several_channels/README.md)
- [Does a send return before anyone receives?](../an_unbuffered_send_waits/README.md)
- [How do three stages run at once on one stream of values?](../a_pipeline_of_stages/README.md)
- The Go library's [Closing a channel ends a range ↗](https://masiarek.github.io/go-learning-library/02_Channels/closing_a_channel_ends_a_range/index.html)
- The Rust library's [Channels ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/channels/index.html)
- Concepts: [Channel](../../11_Concepts/communication/channel/README.md) · [Message passing](../../11_Concepts/communication/message_passing/README.md) · [Leaked tasks](../../11_Concepts/hazards/task_leak/README.md) · [Liveness failure](../../11_Concepts/hazards/liveness_failure/README.md)
