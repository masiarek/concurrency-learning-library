# Where does a callback keep its state?

**Level:** 201 · anyone who has written `on_done(result)` and lost the variable it needed

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** A callback is a function called later by someone else, and every local it needs has to be carried to it — in a closure, in a `void *`, in an object — which is the problem `async`/`await` was invented to hide: the state that a callback has to carry by hand is exactly what an `await` keeps in the future.

## The question

Start a timer, and when it fires, print a message that was known when the timer was started. In C the message travels as a `void *` and the type is lost. In Go it is a closure. In Python it is a closure or a `functools.partial`. The page writes the same timer-and-message in each language, shows the state's journey, and then chains three callbacks to show why the shape became known as the pyramid of doom — and rewrites it with `await`.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | a boxed `FnOnce` closure; the `async` rewrite is the same closure with its state in the future |
| Go | `time.AfterFunc(d, func() {...})` with a closure |
| C | `void (*)(void *)` and the state cast back from a `void *`; the page's C column is the reason the others exist |
| C++ | `std::function` capturing by value; or a coroutine |
| Java | a lambda passed to `CompletableFuture.thenAccept`; `thenCompose` for the chain |
| Python | `loop.call_later(d, cb, arg)`; the chain, then the `await` rewrite |

## What the programs have to show

- the timer firing with its message, per language
- three chained callbacks as a pyramid, and the same as three `await`s
- the C `void *` cast to the wrong type: compiles, and what happens

## See also

- Before this: [What does one blocking call do to every other task?](../blocking_the_event_loop/README.md)
- After this: [How is a running task told to stop, and does it?](../cancelling_an_async_task/README.md)
- [What happens at an `await`?](../async_and_await/README.md)
- [What does an event loop do all day?](../what_an_event_loop_does/README.md)
- Concepts: [Callback](../../11_Concepts/async/callback/README.md) · [Event-driven programming](../../11_Concepts/async/event_driven_programming/README.md) · [Async and await](../../11_Concepts/async/async_await/README.md) · [Timers and tickers](../../11_Concepts/async/timers/README.md) · [Async functions as state machines](../../11_Concepts/async/async_state_machine/README.md)
