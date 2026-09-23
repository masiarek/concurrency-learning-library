# 04 — Waiting for each other

A lock says *not at the same time*. This chapter is about *not until*: a consumer that must not run until there is an item, a phase that must not begin until every worker has finished the last one, an initializer that must run once and before any reader. The primitives — condition variable, semaphore, barrier, latch, once — are older than the languages, and each language has repackaged them; the bugs, the lost wakeup above all, are the same everywhere.

Every lesson in this chapter is a **stub**: the question, the expected answer per language and what the programs will have to show, waiting for the programs. A stub becomes a lesson when its examples run in CI and its table is replaced by what they printed.

| Lesson | The one thing |
|---|---|
| [How does a thread wait for something to become true?](waiting_for_a_condition/README.md) | *stub* — wait until signalled — inside a loop, because the wait may return without a signal |
| [What happens when the signal comes before the wait?](the_lost_wakeup/README.md) | *stub* — a signal with no waiter is dropped; hold the lock across the check and the wait |
| [What does a semaphore count?](a_semaphore_counts_permits/README.md) | *stub* — N permits, no owner; any thread may release what another acquired |
| [How do N threads wait for each other?](a_barrier_and_a_latch/README.md) | *stub* — have all of us reached this point? — the latch once, the barrier every round |
| [How does initialization run exactly once with many threads racing to it?](run_exactly_once/README.md) | *stub* — check-then-initialize with a constructor in it; every language has a once-primitive |
| [What is a monitor, and which languages have one?](a_monitor_bundles_lock_and_condition/README.md) | *stub* — a lock and its conditions as one object, with the rule that you wait only while holding it |
| [How does a producer wait for room and a consumer wait for an item?](the_bounded_buffer/README.md) | *stub* — two conditions, *not full* and *not empty*; one condition and `notify_one` can hang |
| [Why do five philosophers with five forks starve?](the_dining_philosophers/README.md) | *stub* — five forks, five philosophers, the two-lock deadlock in its original clothes, and its four fixes |
| [What does a wait return when the time runs out?](waiting_with_a_timeout/README.md) | *stub* — three outcomes, not two: done, timed out, and timed out just as it happened |
