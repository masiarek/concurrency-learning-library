# Interleaving

**Category:** [Foundations](../README.md) · **Status:** stub · **Lessons:** [chapter 02, Shared state](../../../02_Shared_State/README.md)

**One line:** One of the many orders in which the steps of concurrent tasks can actually run; a concurrent program is correct only if it is correct under every one of them.

## How it connects

```mermaid
flowchart LR
  n_interleaving["Interleaving"]
  n_race_condition["Race condition"]
  n_interleaving -->|can cause| n_race_condition
  classDef center stroke-width:3px
  class n_interleaving center
  classDef outside stroke-dasharray: 4 3
  class n_race_condition outside
```

- **Can lead to:** [Race condition](../../hazards/race_condition/README.md)
- **See also:** [Concurrency](../concurrency/README.md), [Nondeterminism](../nondeterminism/README.md), [Preemptive scheduling](../../scheduling/preemptive_scheduling/README.md)

## Where to read more

- **In this library:** [Is total += n safe on two threads?](../../../02_Shared_State/the_lost_update/README.md)
- **In this library:** [How do you write a test that provokes the race?](../../../09_Testing_and_Tools/a_stress_test_that_actually_races/README.md)
- **In this library:** [Can every interleaving of a small program be checked?](../../../09_Testing_and_Tools/model_checking_a_small_program/README.md)
- **In a sibling library:** [Go: Fan-out, fan-in ↗](https://masiarek.github.io/go-learning-library/06_Patterns/fan_out_fan_in/index.html)
- **Notes:** [interleaving actions across threads ↗](https://docs.google.com/document/d/1JqRl9gJCA_tmJQPkipzg0sG5p773x-PuPIel-Nx5HdM/edit?tab=t.0)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
