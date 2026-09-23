# What if only one thread is allowed to touch the data?

**Level:** 201 · anyone who has met an actor, or Go's proverb about sharing memory

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** Instead of locking a total that many threads add to, give the total to *one* thread and have the others send it their numbers — no lock, no race, and every update applied in the order received — which is the actor model in one sentence, the third fix in [Keeping every update](../../02_Shared_State/keeping_every_update/README.md), and the design Erlang built a language around.

## The question

The counter from chapter 02, once more. This time no thread but the owner ever sees it: ten senders, one owner goroutine with a channel, and a final query message that asks for the total. The page runs it, then asks the questions an actor raises — what happens to a message sent to an owner that has stopped, how the owner is asked a question and answered, and what the mailbox costs against a lock.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | an owner thread on an `mpsc::Receiver` of an `enum Message { Add(u64), Total(Sender<u64>) }` |
| Go | an owner goroutine on a channel of a struct with a reply channel inside; "do not communicate by sharing memory" |
| C | an owner thread on a pipe, with the reply through a second pipe |
| C++ | an owner `std::jthread` on a hand-built queue of `std::variant` messages |
| Java | an owner thread on a `BlockingQueue`, replying through a `CompletableFuture` in the message |
| Python | an owner thread on a `Queue`, replying through a `Future`, or an `asyncio` task |

## What the programs have to show

- ten senders, one owner: the total is right without a lock, and the order of application is the order of receipt
- the ask-and-reply message, and the sender that waits for the reply
- a message to an owner that has exited: the error, the panic, or the silent loss, per language

## See also

- Before this: [How do N workers share one queue of jobs?](../a_worker_pool/README.md)
- After this: [How does one event reach every subscriber?](../publish_and_subscribe/README.md)
- [Keeping every update](../../02_Shared_State/keeping_every_update/README.md)
- [Who owns a value after it has been sent?](../sending_a_value_moves_it/README.md)
- The Rust library's [Who owns the state ↗](https://masiarek.github.io/rust-learning-library/35_Async/building_minidb/who_owns_the_state/index.html)
- The Go library's [A goroutine has no handle ↗](https://masiarek.github.io/go-learning-library/01_Goroutines/a_goroutine_has_no_handle/index.html)
- Concepts: [Actor model](../../11_Concepts/communication/actor_model/README.md) · [Communicating sequential processes](../../11_Concepts/communication/csp/README.md) · [Message passing](../../11_Concepts/communication/message_passing/README.md) · [Thread confinement](../../11_Concepts/safety_in_languages/thread_confinement/README.md) · [Supervision](../../11_Concepts/communication/supervision/README.md) · [OTP behaviours](../../11_Concepts/communication/otp_behaviours/README.md)
