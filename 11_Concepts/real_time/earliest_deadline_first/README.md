# Earliest deadline first

**Category:** [Real-time systems](../README.md) · **Status:** stub

**One line:** Dynamic priorities: whichever ready task has the nearest deadline runs next.

Also called: EDF, deadline scheduling.

## How it connects

```mermaid
flowchart LR
  n_earliest_deadline_first["Earliest deadline first"]
  n_preemptive_scheduling["Preemptive scheduling"]
  n_rate_monotonic_scheduling["Rate-monotonic scheduling"]
  n_wcet["Worst-case execution time"]
  n_earliest_deadline_first ---|vs| n_rate_monotonic_scheduling
  n_earliest_deadline_first -->|is a| n_preemptive_scheduling
  n_earliest_deadline_first -->|uses| n_wcet
  classDef center stroke-width:3px
  class n_earliest_deadline_first center
  classDef outside stroke-dasharray: 4 3
  class n_preemptive_scheduling,n_rate_monotonic_scheduling,n_wcet outside
```

- **Is a kind of:** [Preemptive scheduling](../../scheduling/preemptive_scheduling/README.md)
- **Is built on:** [Worst-case execution time](../wcet/README.md)
- **Often confused with:** [Rate-monotonic scheduling](../rate_monotonic_scheduling/README.md)

## In each language

| | |
|---|---|
| The operating system | Linux's [`SCHED_DEADLINE` ↗](https://man7.org/linux/man-pages/man7/sched.7.html), global EDF combined with a constant bandwidth server |
| Elsewhere | Ada's [Earliest Deadline First dispatching ↗](http://www.ada-auth.org/standards/22rm/html/RM-D-2-6.html) policy and its `Dispatching.EDF` package |

## Where to read more

- **Notes:** [Earliest Deadline First (EDF) ↗](https://docs.google.com/document/d/1Uvz4Cz3L1OSg1Ccla41i5hYqiCNKGV5cX4eLKEx3r1Y/edit?tab=t.0)
- **Reference:** [Wikipedia: Earliest deadline first scheduling ↗](https://en.wikipedia.org/wiki/Earliest_deadline_first_scheduling)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
