# 02 — Shared state

Two threads that share nothing cannot hurt each other. Give them one number to share and even adding to it goes wrong — which surprises almost everyone, because addition is the operation whose answer cannot depend on order. This chapter starts from the smallest shared state there is, a total that request handlers add to, and asks about it in order: how an addition gets lost, the three ways to keep it, the same bug one level down in a database, what besides timing can still change a sum, and which of these a compiler or a race detector can find for you.

| Lesson | The one thing |
|---|---|
| [Is `total += n` safe on two threads?](the_lost_update/README.md) | load, add, store: ten threads that each add 1 can leave a total of 1, even when every load and store is atomic |
| [Keeping every update](keeping_every_update/README.md) | a lock around the three steps, one atomic add, or one owner that the numbers are sent to |
| [The lost update in a database](the_lost_update_in_a_database/README.md) | `SELECT` and then `UPDATE` loses an update; `SET total = total + ?` does not, and a transaction may either refuse or quietly overwrite |
| [When does order change a sum?](when_order_changes_a_sum/README.md) | never for integers; for floats, for a request that can be refused, and for a request delivered twice |
| [Data race or race condition?](data_race_or_race_condition/README.md) | two threads that both write `1` are a data race with no race condition: the answer is always right, and safe Rust still refuses to compile it |
| [Can two atomics keep two values consistent?](two_values_that_must_change_together/README.md) | *stub* — an atomic per value makes each value safe and the pair unsafe; a lock around both, or one atomic holding both |
| [When is a read-write lock faster than a mutex?](readers_and_writers/README.md) | *stub* — many readers or one writer — faster only when reads are long and writes rare; Python has no such lock |
| [Can a read see half of a write?](a_torn_read/README.md) | *stub* — a value wider than one store can be read half-written; Java says so for `long`, C calls it undefined, Rust refuses it |
| [Why is checking and then acting two steps too many?](check_then_act/README.md) | *stub* — between the check and the act the world changes; the fix is one operation that does both |
| [Can a compare-and-swap succeed when it should have failed?](the_aba_problem/README.md) | *stub* — a compare-and-swap passes on A→B→A; the fix is a version stamp beside the pointer |
| [What may be handed to another thread?](what_may_cross_a_thread_boundary/README.md) | *stub* — Rust decides `Send` and `Sync` at compile time; the others let anything cross and find out at run time |
| [Can one thread see another's writes out of order?](reordering_and_the_memory_model/README.md) | *stub* — `data` then `ready` can be seen as `ready` first, unless the store is a release and the load an acquire |

Rows marked *stub* are questions with their expected answers written down and no program behind them yet; the page says so at the top.
