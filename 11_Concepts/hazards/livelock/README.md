# Livelock

**Category:** [Hazards](../README.md) · **Status:** stub · **Lessons:** chapter 03, When locks go wrong *(planned)*

**One line:** Tasks keep changing state in response to each other — backing off, retrying, stepping aside — without any of them getting work done.

## How it connects

```mermaid
flowchart LR
  n_deadlock["Deadlock"]
  n_livelock["Livelock"]
  n_liveness_failure["Liveness failure"]
  n_deadlock ---|vs| n_livelock
  n_livelock -->|is a| n_liveness_failure
  classDef center stroke-width:3px
  class n_livelock center
  classDef outside stroke-dasharray: 4 3
  class n_deadlock,n_liveness_failure outside
```

- **Is a kind of:** [Liveness failure](../liveness_failure/README.md)
- **Often confused with:** [Deadlock](../deadlock/README.md)

## Where to read more

- **In the books:** [*Grokking Concurrency*](../../../10_Resources/books_general/README.md#bobrov_grokking_concurrency), Kirill Bobrov — ch. 9, 'Solving concurrency problems: Deadlocks and starvation' → 'Livelocks'
- **In the books:** [*Modern Multithreading*](../../../10_Resources/books_general/README.md#carver_tai_modern_multithreading), Richard H. Carver, Kuo-Chung Tai — ch. 2, 'The Critical Section Problem' → 'Deadlock, Livelock, and Starvation'
- **In the books:** [*Advanced Python Programming*](../../../10_Resources/books_python/README.md#nguyen_advanced_python_programming), Quan Nguyen — ch. 12, 'Deadlocks' → 'The concept of livelocks'
- **Reference:** [Wikipedia: Deadlock — livelock ↗](https://en.wikipedia.org/wiki/Deadlock_(computer_science)#Livelock)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
