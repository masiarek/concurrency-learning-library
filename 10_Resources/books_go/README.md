# Concurrency books — Go

[All book lists](../README.md#books) · [Concepts](../../11_Concepts/README.md)

<a id="cutajar_learn_concurrent_programming_with_go"></a>

## *Learn Concurrent Programming with Go*

James Cutajar · 1st edition · Manning Publications · 2024  
dedicated to concurrency · on the shelf · [publisher ↗](https://www.manning.com/books/learn-concurrent-programming-with-go) · [example code ↗](https://github.com/cutajarj/ConcurrentProgrammingWithGo)

<details markdown="1">
<summary>Chapters</summary>

- **1** Stepping into concurrent programming
- **2** Dealing with threads
- **3** Thread communication using memory sharing
- **4** Synchronization with mutexes
- **5** Condition variables and semaphores
- **6** Synchronizing with waitgroups and barriers
- **7** Communication using message passing
- **8** Selecting channels
- **9** Programming with channels
- **10** Concurrency patterns
- **11** Avoiding deadlocks
- **12** Atomics, spin locks, and futexes

</details>

Cited on: [Atomic variable](../../11_Concepts/lock_free/atomic_variable/README.md), [Barrier](../../11_Concepts/synchronization/barrier/README.md), [Busy waiting](../../11_Concepts/scheduling/busy_waiting/README.md), [Communicating sequential processes](../../11_Concepts/communication/csp/README.md), [Condition variable](../../11_Concepts/synchronization/condition_variable/README.md), [Critical section](../../11_Concepts/synchronization/critical_section/README.md), [Deadlock](../../11_Concepts/hazards/deadlock/README.md), [Futex](../../11_Concepts/synchronization/futex/README.md), [Goroutine](../../11_Concepts/units_of_execution/goroutine/README.md), [Join](../../11_Concepts/async/join/README.md), [Lock ordering](../../11_Concepts/synchronization/lock_ordering/README.md), [Lock-free](../../11_Concepts/lock_free/lock_free/README.md), [Message passing](../../11_Concepts/communication/message_passing/README.md), [Multiprocessing](../../11_Concepts/parallelism/multiprocessing/README.md), [Mutex](../../11_Concepts/synchronization/mutex/README.md), [Process](../../11_Concepts/units_of_execution/process/README.md), [Race condition](../../11_Concepts/hazards/race_condition/README.md), [Read-write lock](../../11_Concepts/synchronization/read_write_lock/README.md), [Select](../../11_Concepts/communication/select/README.md), [Semaphore](../../11_Concepts/synchronization/semaphore/README.md), [Shared memory](../../11_Concepts/communication/shared_memory/README.md), [Speedup and Amdahl's law](../../11_Concepts/foundations/speedup_and_amdahls_law/README.md), [Spinlock](../../11_Concepts/synchronization/spinlock/README.md), [Thread](../../11_Concepts/units_of_execution/thread/README.md)

<a id="serdar_effective_concurrency_in_go"></a>

## *Effective Concurrency in Go*

Burak Serdar · 1st edition · Packt Publishing · 2023  
dedicated to concurrency · on the shelf · [example code ↗](https://github.com/PacktPublishing/Effective-Concurrency-in-Go)

<details markdown="1">
<summary>Chapters</summary>

- **1** Concurrency – A High-Level Overview
- **2** Go Concurrency Primitives
- **3** The Go Memory Model
- **4** Some Well-Known Concurrency Problems
- **5** Worker Pools and Pipelines
- **6** Error Handling
- **7** Timers and Tickers
- **8** Handling Requests Concurrently
- **9** Atomic Memory Operations
- **10** Troubleshooting Concurrency Issues

</details>

Cited on: [Async stream](../../11_Concepts/async/async_stream/README.md), [Atomic variable](../../11_Concepts/lock_free/atomic_variable/README.md), [Backpressure](../../11_Concepts/communication/backpressure/README.md), [Classic synchronization problems](../../11_Concepts/synchronization/classic_synchronization_problems/README.md), [Compare-and-swap](../../11_Concepts/lock_free/compare_and_swap/README.md), [Debugging concurrent programs](../../11_Concepts/testing_and_tools/concurrency_debugging/README.md), [Fan-out, fan-in](../../11_Concepts/communication/fan_out_fan_in/README.md), [Goroutine](../../11_Concepts/units_of_execution/goroutine/README.md), [Happens-before](../../11_Concepts/lock_free/happens_before/README.md), [Join](../../11_Concepts/async/join/README.md), [Pipeline](../../11_Concepts/communication/pipeline/README.md), [Producer-consumer](../../11_Concepts/communication/producer_consumer/README.md), [Starvation](../../11_Concepts/hazards/starvation/README.md), [Supervision](../../11_Concepts/communication/supervision/README.md), [Timers and tickers](../../11_Concepts/async/timers/README.md), [Weak memory models and reordering](../../11_Concepts/hazards/weak_memory_model/README.md), [Worker pool](../../11_Concepts/communication/worker_pool/README.md)

<a id="cox_buday_concurrency_in_go"></a>

## *Concurrency in Go*: Tools and Techniques for Developers

Katherine Cox-Buday · 1st edition · O'Reilly Media · 2017  
dedicated to concurrency · on the shelf

<details markdown="1">
<summary>Chapters</summary>

- **1** An Introduction to Concurrency
- **2** Modeling Your Code: Communicating Sequential Processes
- **3** Go’s Concurrency Building Blocks
- **4** Concurrency Patterns in Go
- **5** Concurrency at Scale
- **6** Goroutines and the Go Runtime
- Appendix

</details>

Cited on: [Async runtime (executor and reactor)](../../11_Concepts/scheduling/async_runtime/README.md), [Backpressure](../../11_Concepts/communication/backpressure/README.md), [Cancellation](../../11_Concepts/async/cancellation/README.md), [Channel](../../11_Concepts/communication/channel/README.md), [Communicating sequential processes](../../11_Concepts/communication/csp/README.md), [Concurrency](../../11_Concepts/foundations/concurrency/README.md), [Fan-out, fan-in](../../11_Concepts/communication/fan_out_fan_in/README.md), [Goroutine](../../11_Concepts/units_of_execution/goroutine/README.md), [Idempotency](../../11_Concepts/distributed/idempotency/README.md), [Leaked tasks](../../11_Concepts/hazards/task_leak/README.md), [Race detector](../../11_Concepts/testing_and_tools/race_detector/README.md), [Select](../../11_Concepts/communication/select/README.md), [Supervision](../../11_Concepts/communication/supervision/README.md), [Thread confinement](../../11_Concepts/safety_in_languages/thread_confinement/README.md), [Timeout](../../11_Concepts/async/timeout/README.md), [Work stealing](../../11_Concepts/scheduling/work_stealing/README.md)

<a id="butcher_farina_go_in_practice"></a>

## *Go in Practice*

Nathan Kozyra, Matt Butcher, Matt Farina · 2nd edition · Manning Publications · 2025  
a concurrency chapter in a broader book · on the shelf · [publisher ↗](https://www.manning.com/books/go-in-practice-second-edition) · [example code ↗](https://github.com/nkozyra/go-in-practice)

<details markdown="1">
<summary>The concurrency chapters</summary>

- **5** Concurrency in Go

</details>

Cited on: [Concurrency models](../../11_Concepts/foundations/concurrency_models/README.md)

<a id="bodner_learning_go"></a>

## *Learning Go*: An Idiomatic Approach to Real-World Go Programming

Jon Bodner · 2nd edition · O'Reilly Media · 2024  
a concurrency chapter in a broader book · on the shelf · [example code ↗](https://github.com/learning-go-book-2e)

<details markdown="1">
<summary>The concurrency chapters</summary>

- **12** Concurrency in Go
- **14** The Context

</details>

Cited on: [Select](../../11_Concepts/communication/select/README.md)

<a id="tsoukalos_go_systems_programming"></a>

## *Go Systems Programming*: Master Linux and Unix system level programming with Go

Mihalis Tsoukalos · 1st edition · Packt Publishing · 2017  
a concurrency chapter in a broader book · on the shelf · [example code ↗](https://github.com/PacktPublishing/Go-Systems-Programming)

<details markdown="1">
<summary>The concurrency chapters</summary>

- **9** Goroutines — Basic Features
- **10** Goroutines — Advanced Features

</details>

Cited on: [Buffered and bounded channels](../../11_Concepts/communication/bounded_channel/README.md), [Goroutine](../../11_Concepts/units_of_execution/goroutine/README.md), [Race detector](../../11_Concepts/testing_and_tools/race_detector/README.md)

<a id="kennedy_go_in_action"></a>

## *Go in Action*

William Kennedy, Brian Ketelsen, Erik St. Martin · 1st edition · Manning Publications · 2016  
a concurrency chapter in a broader book · on the shelf · [publisher ↗](https://www.manning.com/books/go-in-action) · [example code ↗](https://github.com/goinaction/code)

<details markdown="1">
<summary>The concurrency chapters</summary>

- **6** Concurrency
- **7** Concurrency patterns

</details>

<a id="doxsey_introducing_go"></a>

## *Introducing Go*: Build Reliable, Scalable Programs

Caleb Doxsey · 1st edition · O'Reilly Media · 2016  
a concurrency chapter in a broader book · on the shelf

<details markdown="1">
<summary>The concurrency chapters</summary>

- **10** Concurrency

</details>

<a id="donovan_kernighan_go_programming_language"></a>

## *The Go Programming Language*

Alan A. A. Donovan, Brian W. Kernighan · 1st edition · Addison-Wesley (Pearson Education) · 2015  
a concurrency chapter in a broader book · on the shelf · [publisher ↗](https://www.informit.com/store/go-programming-language-9780134190440) · [example code ↗](https://github.com/adonovan/gopl.io)

<details markdown="1">
<summary>The concurrency chapters</summary>

- **8** Goroutines and Channels
- **9** Concurrency with Shared Variables

</details>

Cited on: [Goroutine](../../11_Concepts/units_of_execution/goroutine/README.md), [I/O multiplexing](../../11_Concepts/scheduling/io_multiplexing/README.md), [Race detector](../../11_Concepts/testing_and_tools/race_detector/README.md), [Run-once initialization](../../11_Concepts/synchronization/once_initialization/README.md), [Select](../../11_Concepts/communication/select/README.md)

<a id="chisnall_go_phrasebook"></a>

## *The Go Programming Language Phrasebook*

David Chisnall · 1st edition · Addison-Wesley (Pearson Education) · 2012  
a concurrency chapter in a broader book · on the shelf · [publisher ↗](https://www.informit.com/store/go-programming-language-phrasebook-9780321817143)

<details markdown="1">
<summary>The concurrency chapters</summary>

- **9** Goroutines
- **10** Concurrency Design Patterns

</details>

Cited on: [Communicating sequential processes](../../11_Concepts/communication/csp/README.md), [Daemon and detached threads](../../11_Concepts/units_of_execution/daemon_thread/README.md), [Goroutine](../../11_Concepts/units_of_execution/goroutine/README.md), [Map-reduce](../../11_Concepts/parallelism/map_reduce/README.md), [Run-once initialization](../../11_Concepts/synchronization/once_initialization/README.md), [Thread confinement](../../11_Concepts/safety_in_languages/thread_confinement/README.md)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
