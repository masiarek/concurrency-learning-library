# Testing and tools

Finding concurrency bugs on purpose: race detectors, deterministic schedulers, stress runs, model checkers, and the tools that show what every thread is waiting for.

[All categories](../README.md) · [How they connect](../schema/README.md)

- [Race detector](race_detector/README.md) — A tool that instruments memory accesses as the program runs and reports the data races that actually happened in that run — ThreadSanitizer, Go's `-race`.
- [Deterministic scheduling for tests](deterministic_testing/README.md) — Running concurrent code under a controlled scheduler or a fake clock, so that an interleaving or a timeout can be reproduced on demand — Rust's loom, Go's `testing/synctest`.
- [Stress testing](stress_testing/README.md) — Running concurrent code many times, under load and with many threads, so that rare interleavings get a chance to show up.
- [Model checking](model_checking/README.md) — Exploring every state and interleaving of a model of a program — in TLA+, SPIN, or loom — to prove a property or produce a counterexample.
- [Debugging concurrent programs](concurrency_debugging/README.md) — Thread dumps, deadlock detectors and tracing that show what every thread or task is waiting for at a given moment.
- [Profiling concurrent programs](profiling_concurrency/README.md) — Measuring where the time goes when many threads run — waiting for locks, waiting to be scheduled, and bouncing cache lines — and not only which functions are hot.

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
