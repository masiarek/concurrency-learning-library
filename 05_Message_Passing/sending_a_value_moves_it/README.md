# Who owns a value after it has been sent?

**Level:** 201 · anyone who sent a pointer down a channel and kept using it

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** Sending a value on a Rust channel *moves* it — the sender cannot touch it afterwards, and the compiler says so — while every other language here *copies a reference* and leaves the sender an alias, so that "share memory by communicating" is a guarantee in one language and an honour system in the rest.

## The question

A worker builds a buffer and sends it to a collector. Then the worker keeps writing to the buffer. Does the collector see the writes? In Rust the second write is a compile error: the buffer moved. In Go, Java and Python the collector and the worker now share the buffer, and the writes race. The page sends a buffer, mutates it after sending, and reports what each side sees — and, in Rust, what the compiler said instead.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | `tx.send(buf)` moves `buf`; a later `buf.push` is `error[E0382]: use of moved value` |
| Go | `ch <- buf` sends the slice header; the sender and the receiver alias the same array |
| C | a pointer through a pipe or a queue is just a pointer; both sides hold it |
| C++ | `std::move` into the queue makes the sender's object empty by convention, not by rule |
| Java | a `BlockingQueue.put(list)` shares the list; both sides may mutate it |
| Python | `queue.put(list)` shares the list |

## What the programs have to show

- the send-then-mutate program: Rust's compile error, and in the others the collector reading the mutated buffer
- the same in Go under `-race`, which reports it
- the copy-before-send that each other language has to write by hand to get Rust's guarantee

## See also

- After this: [Does a send return before anyone receives?](../an_unbuffered_send_waits/README.md)
- [What may be handed to another thread?](../../02_Shared_State/what_may_cross_a_thread_boundary/README.md)
- [Keeping every update](../../02_Shared_State/keeping_every_update/README.md)
- The Rust library's [Channels ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/channels/index.html)
- The Rust library's [Send and Sync ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/send_and_sync/index.html)
- Concepts: [Message passing](../../11_Concepts/communication/message_passing/README.md) · [Channel](../../11_Concepts/communication/channel/README.md) · [Shared memory](../../11_Concepts/communication/shared_memory/README.md) · [Send and Sync](../../11_Concepts/safety_in_languages/send_and_sync/README.md) · [Communicating sequential processes](../../11_Concepts/communication/csp/README.md)
