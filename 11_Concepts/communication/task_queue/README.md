# Task queue

**Category:** [Communication](../README.md) · **Status:** stub · **Lessons:** [chapter 05, Message passing](../../../05_Message_Passing/README.md)

**One line:** A queue of jobs that workers take and run — within one program, or across processes and machines with a broker in between.

Also called: job queue, work queue, Celery.

## How it connects

```mermaid
flowchart LR
  n_producer_consumer["Producer-consumer"]
  n_task_queue["Task queue"]
  n_task_queue -->|uses| n_producer_consumer
  classDef center stroke-width:3px
  class n_task_queue center
  classDef outside stroke-dasharray: 4 3
  class n_producer_consumer outside
```

- **Is built on:** [Producer-consumer](../producer_consumer/README.md)
- **See also:** [Publish-subscribe and broadcast](../publish_subscribe/README.md), [Worker pool](../worker_pool/README.md)

## In each language

| | |
|---|---|
| Java | [`BlockingQueue` ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/BlockingQueue.html), which an `ExecutorService` uses for its waiting tasks |
| Python | [`queue.Queue` ↗](https://docs.python.org/3/library/queue.html) between threads, [`asyncio.Queue` ↗](https://docs.python.org/3/library/asyncio-queue.html) between tasks |
| Elsewhere | [Celery ↗](https://docs.celeryq.dev/en/stable/) runs Python tasks on workers fed through a message broker |

## Where to read more

- **In this library:** [Why reuse a thread at all?](../../../01_Threads/reusing_threads_in_a_pool/README.md)
- **In this library:** [How do N workers share one queue of jobs?](../../../05_Message_Passing/a_worker_pool/README.md)
- **In the books:** [*Programming with POSIX Threads*](../../../10_Resources/books_c/README.md#butenhof_programming_with_posix_threads), David R. Butenhof — ch. 7, '"Real Code"' → 'Work queue manager'
- **In the books:** [*Python Concurrency with asyncio*](../../../10_Resources/books_python/README.md#fowler_python_concurrency_with_asyncio), Matthew Fowler — ch. 12, 'Asynchronous queues'
- **In the books:** [*Parallel Programming with Python*](../../../10_Resources/books_python/README.md#palach_parallel_programming_with_python), Jan Palach — ch. 7, 'Distributing Tasks with Celery'
- **In the books:** [*Designing Distributed Systems*](../../../10_Resources/books_general/README.md#burns_designing_distributed_systems), Brendan Burns — ch. 10, 'Work Queue Systems'
- **In the books:** [*High Performance Python*](../../../10_Resources/books_python/README.md#gorelick_ozsvald_high_performance_python), Micha Gorelick, Ian Ozsvald — ch. 10, 'Clusters and Job Queues'
- **In the books:** [*Python Parallel Programming Cookbook*](../../../10_Resources/books_python/README.md#zaccone_python_parallel_programming_cookbook), Giancarlo Zaccone — ch. 5, 'Distributed Python' → 'Using Celery to distribute tasks'

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
