# Priority inversion

**Category:** [Hazards](../README.md) · **Status:** stub · **Lessons:** chapter 03, When locks go wrong *(planned)*

**One line:** A high-priority task waits for a lock held by a low-priority task, which is itself preempted by medium-priority work, so the most important task effectively runs last.

## How it connects

```mermaid
flowchart LR
  n_liveness_failure["Liveness failure"]
  n_mutex["Mutex"]
  n_priority_inversion["Priority inversion"]
  n_mutex -->|can cause| n_priority_inversion
  n_priority_inversion -->|is a| n_liveness_failure
  classDef center stroke-width:3px
  class n_priority_inversion center
  classDef outside stroke-dasharray: 4 3
  class n_liveness_failure,n_mutex outside
```

- **Is a kind of:** [Liveness failure](../liveness_failure/README.md)
- **Can be caused by:** [Mutex](../../synchronization/mutex/README.md)
- **See also:** [Real-time system](../../real_time/real_time_system/README.md)

## In each language

| | |
|---|---|
| The operating system | POSIX [`PTHREAD_PRIO_INHERIT` ↗](https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_mutexattr_getprotocol.html): a thread holding such a mutex runs at the priority of the highest-priority thread it blocks; Linux builds this on [priority-inheritance futexes ↗](https://man7.org/linux/man-pages/man2/futex.2.html) and [RT-mutexes ↗](https://docs.kernel.org/locking/rt-mutex.html) |

## Where to read more

- **Reference:** [Wikipedia: Priority inversion ↗](https://en.wikipedia.org/wiki/Priority_inversion)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
