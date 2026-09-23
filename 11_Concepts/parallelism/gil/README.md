# Global interpreter lock

**Category:** [Parallelism](../README.md) · **Status:** stub · **Lessons:** [chapter 07, Parallelism](../../../07_Parallelism/README.md)

**One line:** A lock that lets only one thread run interpreter code at a time — CPython's, and Ruby's — so threads give concurrency but not CPU parallelism; CPython 3.13 added an optional build without it.

Also called: GIL, GVL, free threading.

## How it connects

```mermaid
flowchart LR
  n_gil["Global interpreter lock"]
  n_mutex["Mutex"]
  n_gil -->|uses| n_mutex
  classDef center stroke-width:3px
  class n_gil center
  classDef outside stroke-dasharray: 4 3
  class n_mutex outside
```

- **Is built on:** [Mutex](../../synchronization/mutex/README.md)
- **See also:** [I/O-bound and CPU-bound work](../../foundations/io_bound_and_cpu_bound/README.md), [Multiprocessing](../multiprocessing/README.md)

## In each language

| | |
|---|---|
| Python | CPython's [GIL ↗](https://docs.python.org/3/glossary.html#term-global-interpreter-lock); the [free-threaded build ↗](https://docs.python.org/3/howto/free-threading-python.html), available since 3.13, disables it |
| Elsewhere | CRuby holds its Global VM Lock (GVL) per [`Ractor` ↗](https://docs.ruby-lang.org/en/master/Ractor.html), so ractors run in parallel where threads cannot |

## Where to read more

- **In this library:** [How much faster is real work on eight threads?](../../../07_Parallelism/cpu_bound_speedup/README.md)
- **In this library:** [Why do Python threads take turns?](../../../07_Parallelism/the_gil_and_free_threaded_python/README.md)
- **In this library:** [When are processes the better workers?](../../../08_Processes/multiprocessing_instead_of_threads/README.md)
- **In the books:** [*Python Concurrency with asyncio*](../../../10_Resources/books_python/README.md#fowler_python_concurrency_with_asyncio), Matthew Fowler — ch. 1, 'Getting to know asyncio' → 'Understanding the global interpreter lock'
- **In the books:** [*Parallel Programming with Python*](../../../10_Resources/books_python/README.md#palach_parallel_programming_with_python), Jan Palach — ch. 1, 'Contextualizing Parallel, Concurrent, and Distributed Programming' → 'Taking care of Python GIL'
- **In the books:** [*Advanced Python Programming*](../../../10_Resources/books_python/README.md#nguyen_advanced_python_programming), Quan Nguyen — ch. 15, 'The Global Interpreter Lock'
- **In the books:** [*Fluent Python*](../../../10_Resources/books_python/README.md#ramalho_fluent_python), Luciano Ramalho — ch. 19, 'Concurrency Models in Python' → 'The Real Impact of the GIL'
- **In the books:** [*Python Cookbook*](../../../10_Resources/books_python/README.md#beazley_jones_python_cookbook), David Beazley, Brian K. Jones — ch. 12, 'Concurrency' → 'Dealing with the GIL (and How to Stop Worrying About It)'
- **Reference:** [PEP 703: Making the Global Interpreter Lock Optional in CPython ↗](https://peps.python.org/pep-0703/)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
