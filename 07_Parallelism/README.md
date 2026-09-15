# 07 — Parallelism

The earlier chapters are about doing several things at once correctly. This one is about doing one thing on several cores so that it finishes sooner — and about the ways the parallel version stops being the same computation as the serial one. It starts where the textbooks start, with a sum split across workers.

| Lesson | The one thing |
|---|---|
| [Splitting a sum across workers](splitting_a_sum_across_workers/README.md) | private partial sums need no lock; a tree combines them in fewer rounds; and a float total depends on how the additions were grouped |

## Planned

- **CPU-bound speedup** — the same split with real work in each worker, timed with one worker and with many, as real runs.
- **The GIL and free-threaded Python** — why the Python threads in the first lesson take turns, and what changes without the lock.
- **Amdahl's law** — the part that stays serial, and the ceiling it puts on the speedup.
- **False sharing** — eight workers each writing their own slot of one array, against eight local variables written once.
