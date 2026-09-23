# Why may only one thread touch the user interface?

**Level:** 201 · anyone whose app froze during a download

> **Stub — a question and its expected answers, not yet a lesson.** No program behind this page has been written or run, so nothing on it has been through [the check that backs every finished page](../../CONTRIBUTING.md). The table is what the finished lesson is expected to find, and every cell is unverified until a program prints it. (Not machine-checked here.)

**One line:** Every GUI toolkit runs its event loop on one designated thread and forbids the others from touching a widget, so that a long task on that thread freezes the interface and a widget update from another thread crashes it — and the fix is the same one as for any event loop: do the work elsewhere and post the result back to the loop's thread.

## The question

No GUI runs in CI, so this page is the event-loop lesson in the shape every toolkit has: a loop thread that owns the widgets, a worker that must not touch them, and a *post to the loop* primitive that carries the result over. The page builds that shape with a queue, in each language, and shows the frozen-loop case and the wrong-thread case — then links the toolkits' own rules.

## What each language is expected to say

| | Expected answer, to be verified by the program |
|---|---|
| Rust | the pattern with a channel and a loop thread; the toolkit rules of `gtk-rs` and `winit` are linked |
| Go | the same with a channel; Fyne and Gio document their single-thread rule |
| C | the same with a pipe; GTK's `g_idle_add` is the post primitive |
| C++ | Qt's `QMetaObject::invokeMethod` with `QueuedConnection` |
| Java | `SwingUtilities.invokeLater` and JavaFX's `Platform.runLater`; touching Swing off the EDT is documented as unsafe |
| Python | `tkinter` is not thread-safe; `after()` from the loop thread is the post primitive |

## What the programs have to show

- the loop thread processing a hundred posted updates, and a worker computing for two seconds without freezing it
- the same work on the loop thread: the updates stall for two seconds
- the toolkit documentation for each language's rule, linked

## See also

- Before this: [How does one thread watch a thousand sockets?](../io_multiplexing_under_the_loop/README.md)
- [What does one blocking call do to every other task?](../blocking_the_event_loop/README.md)
- [What does an event loop do all day?](../what_an_event_loop_does/README.md)
- Concepts: [UI thread](../../11_Concepts/units_of_execution/ui_thread/README.md) · [Event loop](../../11_Concepts/scheduling/event_loop/README.md) · [Thread confinement](../../11_Concepts/safety_in_languages/thread_confinement/README.md) · [Blocking the event loop](../../11_Concepts/async/blocking_the_event_loop/README.md)
