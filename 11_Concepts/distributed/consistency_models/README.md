# Consistency models

**Category:** [Distributed systems](../README.md) · **Status:** stub

**One line:** The promise a distributed store makes about what a reader will see — from strong consistency, where every read sees the latest write, to eventual consistency, where replicas agree only in the end.

Also called: ACID, BASE, eventual consistency, external consistency.

## How it connects


- **See also:** [Linearizability](../../safety_in_languages/linearizability/README.md), [Multi-version concurrency control](../mvcc/README.md), [Sequential consistency](../../safety_in_languages/sequential_consistency/README.md)

## In each language

| | |
|---|---|
| Elsewhere | [etcd ↗](https://etcd.io/docs/v3.6/learning/api_guarantees/) is linearizable by default and serializable on request; [Cassandra ↗](https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html) lets each operation choose how many replicas must respond, from `ONE` to `QUORUM` and beyond |

## Where to read more

- **In the books:** [*Concurrent Programming on Windows*](../../../10_Resources/books_csharp_dotnet/README.md#duffy_concurrent_programming_on_windows), Joe Duffy — ch. 10, 'Memory Models and Lock Freedom' → 'Memory Consistency Models'
- **In the books:** [*Concurrent Programming: Algorithms, Principles, and Foundations*](../../../10_Resources/books_general/README.md#raynal_concurrent_programming_algorithms), Michel Raynal — ch. 4, 'Atomicity: Formal Definition and Properties' → 'Alternatives to Atomicity'
- **In the books:** [*Distributed Computing*](../../../10_Resources/books_general/README.md#kshemkalyani_singhal_distributed_computing), Ajay D. Kshemkalyani, Mukesh Singhal — ch. 12, 'Distributed Shared Memory' → 'Memory Consistency Models'
- **In the books:** [*Designing Data-Intensive Applications*](../../../10_Resources/books_general/README.md#kleppmann_designing_data_intensive_applications), Martin Kleppmann — ch. 9, 'Consistency and Consensus'
- **In the books:** [*Database Internals*](../../../10_Resources/books_general/README.md#petrov_database_internals), Alex Petrov — ch. 11, 'Replication and Consistency'
- **Reference:** [Wikipedia: Consistency model ↗](https://en.wikipedia.org/wiki/Consistency_model)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
