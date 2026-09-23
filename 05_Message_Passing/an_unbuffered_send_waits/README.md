# Does a send return before anyone receives?

**Level:** 201 · anyone whose producer hung on its first send

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** An unbuffered channel makes the sender wait until a receiver takes the value — the send *is* the rendezvous — and a buffered one lets the sender go on until the buffer is full; the difference decides whether a send in a goroutine with no receiver is a stall or a leak, and Rust's `mpsc::channel` is unbounded, which is a third answer.

## The question

Send one value, then print "sent". With nobody receiving, does the print happen? On Go's unbuffered channel, never. On a Go channel of capacity 1, once. On Rust's unbounded channel, always — the value sits in the queue forever. The page runs the send with a receiver that arrives two seconds later and records whether "sent" was printed before or after "received".

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `mpsc::channel()` is unbounded: the send returns at once; `sync_channel(0)` is the rendezvous |
| Go | `make(chan T)` blocks the send until the receive; `make(chan T, 1)` does not |
| C | a pipe has a kernel buffer (64 KiB on Linux); `write` blocks only when it is full |
| C++ | no standard channel; a hand-built queue with a condition variable, bounded to zero |
| Java | `SynchronousQueue` is the rendezvous; `LinkedBlockingQueue` is unbounded |
| Python | `queue.Queue(maxsize=0)` is unbounded; `SimpleQueue` too; a rendezvous has to be built |

## What the programs have to show

- the send with a receiver two seconds late: the order of "sent" and "received" per channel kind
- a send with no receiver ever, under a timeout driver: the hang, the leak, or the success
- Go's runtime reporting the total deadlock when the only goroutine is the blocked sender

## See also

- Before this: [Who owns a value after it has been sent?](../sending_a_value_moves_it/README.md)
- After this: [What stops a fast producer from filling memory?](../a_bounded_queue_pushes_back/README.md)
- [What stops a fast producer from filling memory?](../a_bounded_queue_pushes_back/README.md)
- [What happens when the signal comes before the wait?](../../04_Waiting_For_Each_Other/the_lost_wakeup/README.md)
- The Go library's [An unbuffered send waits for a receiver ↗](https://masiarek.github.io/go-learning-library/02_Channels/an_unbuffered_send_waits_for_a_receiver/index.html)
- The Go library's [All goroutines are asleep ↗](https://masiarek.github.io/go-learning-library/02_Channels/all_goroutines_are_asleep/index.html)
- The Rust library's [Channels ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/channels/index.html)
- Concepts: [Unbuffered channel](../../11_Concepts/communication/unbuffered_channel/README.md) · [Channel](../../11_Concepts/communication/channel/README.md) · [Buffered and bounded channels](../../11_Concepts/communication/bounded_channel/README.md) · [Message passing](../../11_Concepts/communication/message_passing/README.md)
