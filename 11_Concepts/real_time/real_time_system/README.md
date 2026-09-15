# Real-time system

**Category:** [Real-time systems](../README.md) · **Status:** stub

**One line:** A system whose correctness depends on when results arrive as well as on what they are: a hard real-time system must never miss a deadline, a soft one should rarely.

Also called: hard real-time, soft real-time, mission-critical system.

## How it connects


- **See also:** [Priority inversion](../../hazards/priority_inversion/README.md), [Worst-case execution time](../wcet/README.md)

## In each language

| | |
|---|---|
| C | POSIX [`sched_setscheduler` ↗](https://pubs.opengroup.org/onlinepubs/9799919799/functions/sched_setscheduler.html) for a real-time policy, and [`clock_nanosleep` ↗](https://pubs.opengroup.org/onlinepubs/9799919799/functions/clock_nanosleep.html) with `TIMER_ABSTIME` for periodic work |
| The operating system | [`sched(7)` ↗](https://man7.org/linux/man-pages/man7/sched.7.html): Linux's real-time policies `SCHED_FIFO`, `SCHED_RR` and `SCHED_DEADLINE` |
| Elsewhere | Ada's [Real-Time Systems annex ↗](http://www.ada-auth.org/standards/22rm/html/RM-D.html) (Annex D) specifies what a real-time Ada implementation provides |

## Where to read more

- **Notes:** [Real-time systems - mission-critical applications - real-time processing ↗](https://docs.google.com/document/d/1Yz-VeK0_FKg1JSwXPg4iLpbATBv_Z6SLG2TxozCqHvw/edit?tab=t.0)
- **Notes:** [mission-critical systems ↗](https://docs.google.com/document/d/1Zxa9uwKIHR_RfZoWVMvM_aAiYt4PAIS-tKXwJVeWzpM/edit?tab=t.0)
- **Notes:** [Embedded systems - Raspberry Pi Pico ↗](https://docs.google.com/document/d/1CPx6OlSkYbOKRMLNuW0hs-lrKYGhk4JQ8hQa4z94b_Q/edit)
- **Reference:** [Wikipedia: Real-time computing ↗](https://en.wikipedia.org/wiki/Real-time_computing)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
