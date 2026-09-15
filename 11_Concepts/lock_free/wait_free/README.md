# Wait-free

**Category:** [Lock-free](../README.md) · **Status:** stub

**One line:** Stronger than lock-free: every thread finishes its own operation in a bounded number of its own steps, whatever the other threads do.

## How it connects

```mermaid
flowchart LR
  n_lock_free["Lock-free"]
  n_wait_free["Wait-free"]
  n_wait_free -->|is a| n_lock_free
  classDef center stroke-width:3px
  class n_wait_free center
  classDef outside stroke-dasharray: 4 3
  class n_lock_free outside
```

- **Is a kind of:** [Lock-free](../lock_free/README.md)

## Where to read more

- **In the books:** [*Concurrent Programming: Algorithms, Principles, and Foundations*](../../../10_Resources/books_general/README.md#raynal_concurrent_programming_algorithms), Michel Raynal — ch. 7, 'Wait-Free Objects from Read/Write Registers Only'
- **In the books:** [*The Art of Multiprocessor Programming*](../../../10_Resources/books_general/README.md#herlihy_shavit_art_of_multiprocessor_programming), Maurice Herlihy, Nir Shavit — ch. 6, 'Universality of Consensus' → 'A Wait-Free Universal Construction'
- **In the books:** [*Distributed Computing*](../../../10_Resources/books_general/README.md#kshemkalyani_singhal_distributed_computing), Ajay D. Kshemkalyani, Mukesh Singhal — ch. 12, 'Distributed Shared Memory' → 'Wait-freedom'
- **Reference:** [Wikipedia: Non-blocking algorithm — wait-freedom ↗](https://en.wikipedia.org/wiki/Non-blocking_algorithm#Wait-freedom)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
