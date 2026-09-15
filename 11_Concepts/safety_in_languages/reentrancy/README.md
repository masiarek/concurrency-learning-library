# Reentrancy

**Category:** [Safety in languages](../README.md) · **Status:** stub

**One line:** A function is reentrant if it can be entered again — by another thread, a signal handler, or itself — before an earlier call has finished, usually because it keeps its state in structures the caller owns instead of in statics.

Also called: reentrant function, async-signal-safe.

## How it connects

```mermaid
flowchart LR
  n_reentrancy["Reentrancy"]
  n_reentrant_lock["Reentrant lock"]
  n_reentrancy ---|vs| n_reentrant_lock
  classDef center stroke-width:3px
  class n_reentrancy center
  classDef outside stroke-dasharray: 4 3
  class n_reentrant_lock outside
```

- **Often confused with:** [Reentrant lock](../../synchronization/reentrant_lock/README.md)
- **See also:** [Thread safety](../thread_safety/README.md)

## In each language

| | |
|---|---|
| Python | [`signal` ↗](https://docs.python.org/3/library/signal.html): a Python handler does not run inside the low-level C signal handler, which only sets a flag for the interpreter |
| The operating system | [signal-safety(7) ↗](https://man7.org/linux/man-pages/man7/signal-safety.7.html): an async-signal-safe function is one that can be safely called from within a signal handler |

## Where to read more

- **Reference:** [Wikipedia: Reentrancy (computing) ↗](https://en.wikipedia.org/wiki/Reentrancy_(computing))

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
