# Multi-version concurrency control

**Category:** [Distributed systems](../README.md) · **Status:** stub

**One line:** Keeping several versions of each record so that readers see a consistent snapshot while writers add new versions, instead of readers and writers locking each other out.

Also called: MVCC, snapshot isolation.

## How it connects

```mermaid
flowchart LR
  n_mvcc["Multi-version concurrency control"]
  n_read_write_lock["Read-write lock"]
  n_mvcc ---|or| n_read_write_lock
  classDef center stroke-width:3px
  class n_mvcc center
  classDef outside stroke-dasharray: 4 3
  class n_read_write_lock outside
```

- **An alternative to:** [Read-write lock](../../synchronization/read_write_lock/README.md)
- **See also:** [Consistency models](../consistency_models/README.md), [Transactional memory](../../lock_free/transactional_memory/README.md)

## In each language

| | |
|---|---|
| Elsewhere | [PostgreSQL ↗](https://www.postgresql.org/docs/current/mvcc-intro.html): each statement sees a snapshot, so reading never blocks writing; [Clojure's STM ↗](https://clojure.org/reference/refs) also uses multiversion concurrency control |

## Where to read more

- **In this library:** [The lost update in a database](../../../02_Shared_State/the_lost_update_in_a_database/README.md)
- **Notes:** [Multi-Version Concurrency Control (MVCC) ↗](https://docs.google.com/document/d/1sNeZtAABmStuxsVW5tI9yvBA1WPZNcgAlRIula83CgU/edit?tab=t.0)
- **Reference:** [Wikipedia: Multiversion concurrency control ↗](https://en.wikipedia.org/wiki/Multiversion_concurrency_control)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
