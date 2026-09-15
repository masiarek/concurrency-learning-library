# Liveness failure

**Category:** [Hazards](../README.md) · **Status:** stub · **Lessons:** chapter 03, When locks go wrong *(planned)*

**One line:** A task that should make progress never does, though nothing has crashed: it waits for ever, spins for ever, or never gets its turn.

## How it connects

```mermaid
flowchart LR
  n_deadlock["Deadlock"]
  n_task_leak["Leaked tasks"]
  n_livelock["Livelock"]
  n_liveness_failure["Liveness failure"]
  n_priority_inversion["Priority inversion"]
  n_scoped_lock["Scoped locking"]
  n_starvation["Starvation"]
  n_deadlock -->|is a| n_liveness_failure
  n_livelock -->|is a| n_liveness_failure
  n_priority_inversion -->|is a| n_liveness_failure
  n_scoped_lock -->|prevents| n_liveness_failure
  n_starvation -->|is a| n_liveness_failure
  n_task_leak -->|is a| n_liveness_failure
  classDef center stroke-width:3px
  class n_liveness_failure center
  classDef outside stroke-dasharray: 4 3
  class n_deadlock,n_task_leak,n_livelock,n_priority_inversion,n_scoped_lock,n_starvation outside
```

- **Kinds:** [Deadlock](../deadlock/README.md), [Leaked tasks](../task_leak/README.md), [Livelock](../livelock/README.md), [Priority inversion](../priority_inversion/README.md), [Starvation](../starvation/README.md)
- **Is prevented by:** [Scoped locking](../../synchronization/scoped_lock/README.md)
- **See also:** [Safety and liveness](../safety_and_liveness/README.md)

## In each language

| | |
|---|---|
| Rust | [The Rustonomicon ↗](https://doc.rust-lang.org/nomicon/races.html) counts getting deadlocked as safe: the compiler checks memory safety, not progress |
| Java | [JLS §17.1 ↗](https://docs.oracle.com/javase/specs/jls/se25/html/jls-17.html#jls-17.1): the language neither prevents nor requires detection of deadlock |
| Haskell | [`BlockedIndefinitelyOnMVar` ↗](https://hackage.haskell.org/package/base/docs/Control-Exception.html) is the exception for a thread blocked on an `MVar` that nothing else references, so it can never continue |

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
