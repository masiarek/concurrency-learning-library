# 02 — Shared state

Two threads that share nothing cannot hurt each other. Give them one number to share and even adding to it goes wrong — which surprises almost everyone, because addition is the operation whose answer cannot depend on order. This chapter starts from the smallest shared state there is, a total that request handlers add to, and asks about it in order: how an addition gets lost, the three ways to keep it, the same bug one level down in a database, what besides timing can still change a sum, and which of these a compiler or a race detector can find for you.

| Lesson | The one thing |
|---|---|
| [Is `total += n` safe on two threads?](the_lost_update/README.md) | load, add, store: ten threads that each add 1 can leave a total of 1, even when every load and store is atomic |
| [Keeping every update](keeping_every_update/README.md) | a lock around the three steps, one atomic add, or one owner that the numbers are sent to |
| [The lost update in a database](the_lost_update_in_a_database/README.md) | `SELECT` and then `UPDATE` loses an update; `SET total = total + ?` does not, and a transaction may either refuse or quietly overwrite |
| [When does order change a sum?](when_order_changes_a_sum/README.md) | never for integers; for floats, for a request that can be refused, and for a request delivered twice |
| [Data race or race condition?](data_race_or_race_condition/README.md) | two threads that both write `1` are a data race with no race condition: the answer is always right, and safe Rust still refuses to compile it |

## Planned

- **Two values that must change together** — a total and a count, or two account balances: why an atomic per value does not make the pair consistent, and a lock around both does.
- **Readers and writers** — `RwLock`, `sync.RWMutex`, `pthread_rwlock_t`, `std::shared_mutex` and `ReentrantReadWriteLock`, and Python, which has none.
