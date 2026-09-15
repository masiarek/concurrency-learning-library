# Concurrency books — Rust

[All book lists](../README.md#books) · [Concepts](../../11_Concepts/README.md)

<a id="flitton_morton_async_rust"></a>

## *Async Rust*: Unleashing the Power of Fearless Concurrency

Maxwell Flitton, Caroline Morton · 1st edition · O'Reilly Media · 2024  
dedicated to concurrency · on the shelf

<details markdown="1">
<summary>Chapters</summary>

- **1** Introduction to Async
- **2** Basic Async Rust
- **3** Building Our Own Async Queues
- **4** Integrating Networking into Our Own Async Runtime
- **5** Coroutines
- **6** Reactive Programming
- **7** Customizing Tokio
- **8** The Actor Model
- **9** Design Patterns
- **10** Building an Async Server with No Dependencies
- **11** Testing

</details>

Cited on: [Actor model](../../11_Concepts/communication/actor_model/README.md), [Async functions as state machines](../../11_Concepts/async/async_state_machine/README.md), [Async runtime (executor and reactor)](../../11_Concepts/scheduling/async_runtime/README.md), [Asynchrony](../../11_Concepts/foundations/asynchrony/README.md), [Buffered and bounded channels](../../11_Concepts/communication/bounded_channel/README.md), [Coroutine](../../11_Concepts/units_of_execution/coroutine/README.md), [Daemon and detached threads](../../11_Concepts/units_of_execution/daemon_thread/README.md), [Deadlock](../../11_Concepts/hazards/deadlock/README.md), [Deterministic scheduling for tests](../../11_Concepts/testing_and_tools/deterministic_testing/README.md), [Idempotency](../../11_Concepts/distributed/idempotency/README.md), [Join](../../11_Concepts/async/join/README.md), [Process](../../11_Concepts/units_of_execution/process/README.md), [Publish-subscribe and broadcast](../../11_Concepts/communication/publish_subscribe/README.md), [Race condition](../../11_Concepts/hazards/race_condition/README.md), [Race detector](../../11_Concepts/testing_and_tools/race_detector/README.md), [Reactive programming](../../11_Concepts/async/reactive_programming/README.md), [Shared memory](../../11_Concepts/communication/shared_memory/README.md), [Supervision](../../11_Concepts/communication/supervision/README.md), [Task (async)](../../11_Concepts/units_of_execution/async_task/README.md), [Thread-local storage](../../11_Concepts/units_of_execution/thread_local_storage/README.md), [Work stealing](../../11_Concepts/scheduling/work_stealing/README.md), [Worker pool](../../11_Concepts/communication/worker_pool/README.md)

<a id="samson_asynchronous_programming_in_rust"></a>

## *Asynchronous Programming in Rust*: Learn asynchronous programming by building working examples of futures, green threads, and runtimes

Carl Fredrik Samson · 1st edition · Packt Publishing · 2024  
dedicated to concurrency · on the shelf · [example code ↗](https://github.com/PacktPublishing/Asynchronous-Programming-in-Rust)

<details markdown="1">
<summary>Chapters</summary>

- **1** Concurrency and Asynchronous Programming: a Detailed Overview
- **2** How Programming Languages Model Asynchronous Program Flow
- **3** Understanding OS-Backed Event Queues, System Calls, and Cross-Platform Abstractions
- **4** Create Your Own Event Queue
- **5** Creating Our Own Fibers
- **6** Futures in Rust
- **7** Coroutines and async/await
- **8** Runtimes, Wakers, and the Reactor-Executor Pattern
- **9** Coroutines, Self-Referential Structs, and Pinning
- **10** Creating Your Own Runtime

</details>

Cited on: [Async and await](../../11_Concepts/async/async_await/README.md), [Async functions as state machines](../../11_Concepts/async/async_state_machine/README.md), [Async runtime (executor and reactor)](../../11_Concepts/scheduling/async_runtime/README.md), [Callback](../../11_Concepts/async/callback/README.md), [Concurrency models](../../11_Concepts/foundations/concurrency_models/README.md), [Coroutine](../../11_Concepts/units_of_execution/coroutine/README.md), [Event loop](../../11_Concepts/scheduling/event_loop/README.md), [Fiber](../../11_Concepts/units_of_execution/fiber/README.md), [Future and promise](../../11_Concepts/async/future_and_promise/README.md), [Green threads and M:N scheduling](../../11_Concepts/units_of_execution/green_thread/README.md), [I/O multiplexing](../../11_Concepts/scheduling/io_multiplexing/README.md), [I/O-bound and CPU-bound work](../../11_Concepts/foundations/io_bound_and_cpu_bound/README.md), [Multitasking](../../11_Concepts/foundations/multitasking/README.md), [Pinning](../../11_Concepts/async/pinning/README.md), [Polling](../../11_Concepts/scheduling/polling/README.md)

<a id="bos_rust_atomics_and_locks"></a>

## *Rust Atomics and Locks*: Low-Level Concurrency in Practice

Mara Bos · 1st edition · O'Reilly Media · 2023  
dedicated to concurrency · on the shelf · [read it free ↗](https://marabos.nl/atomics/)

<details markdown="1">
<summary>Chapters</summary>

- **1** Basics of Rust Concurrency
- **2** Atomics
- **3** Memory Ordering
- **4** Building Our Own Spin Lock
- **5** Building Our Own Channels
- **6** Building Our Own “Arc”
- **7** Understanding the Processor
- **8** Operating System Primitives
- **9** Building Our Own Locks
- **10** Ideas and Inspiration

</details>

Cited on: [Atomic variable](../../11_Concepts/lock_free/atomic_variable/README.md), [Blocking and non-blocking calls](../../11_Concepts/foundations/blocking_and_nonblocking/README.md), [Channel](../../11_Concepts/communication/channel/README.md), [Compare-and-swap](../../11_Concepts/lock_free/compare_and_swap/README.md), [Concurrent data structures](../../11_Concepts/lock_free/concurrent_data_structures/README.md), [Data race](../../11_Concepts/hazards/data_race/README.md), [Data-race freedom by construction](../../11_Concepts/safety_in_languages/data_race_freedom/README.md), [Happens-before](../../11_Concepts/lock_free/happens_before/README.md), [Interior mutability](../../11_Concepts/safety_in_languages/interior_mutability/README.md), [Read-copy-update](../../11_Concepts/lock_free/rcu/README.md), [Read-write lock](../../11_Concepts/synchronization/read_write_lock/README.md), [Scoped locking](../../11_Concepts/synchronization/scoped_lock/README.md), [Semaphore](../../11_Concepts/synchronization/semaphore/README.md), [Send and Sync](../../11_Concepts/safety_in_languages/send_and_sync/README.md), [Sequential consistency](../../11_Concepts/safety_in_languages/sequential_consistency/README.md), [Spinlock](../../11_Concepts/synchronization/spinlock/README.md), [Structured concurrency](../../11_Concepts/async/structured_concurrency/README.md), [Thread safety](../../11_Concepts/safety_in_languages/thread_safety/README.md), [Weak memory models and reordering](../../11_Concepts/hazards/weak_memory_model/README.md)

<a id="troutwine_hands_on_concurrency_with_rust"></a>

## *Hands-On Concurrency with Rust*: Confidently build memory-safe, parallel, and efficient software in Rust

Brian L. Troutwine · 1st edition · Packt Publishing · 2018  
dedicated to concurrency · on the shelf · [example code ↗](https://github.com/PacktPublishing/Hands-On-Concurrency-with-Rust)

<details markdown="1">
<summary>Chapters</summary>

- **1** Preliminaries – Machine Architecture and Getting Started with Rust
- **2** Sequential Rust Performance and Testing
- **3** The Rust Memory Model – Ownership, References and Manipulation
- **4** Sync and Send – the Foundation of Rust Concurrency
- **5** Locks – Mutex, Condvar, Barriers and RWLock
- **6** Atomics – the Primitives of Synchronization
- **7** Atomics – Safely Reclaiming Memory
- **8** High-Level Parallelism – Threadpools, Parallel Iterators and Processes
- **9** FFI and Embedding – Combining Rust and Other Languages
- **10** Futurism – Near-Term Rust

</details>

Cited on: [Atomic variable](../../11_Concepts/lock_free/atomic_variable/README.md), [Barrier](../../11_Concepts/synchronization/barrier/README.md), [Condition variable](../../11_Concepts/synchronization/condition_variable/README.md), [Happens-before](../../11_Concepts/lock_free/happens_before/README.md), [Hazard pointers](../../11_Concepts/lock_free/hazard_pointers/README.md), [Linearizability](../../11_Concepts/safety_in_languages/linearizability/README.md), [Mutex](../../11_Concepts/synchronization/mutex/README.md), [Parallel iterators and streams](../../11_Concepts/parallelism/parallel_iterators/README.md), [Parallelism](../../11_Concepts/foundations/parallelism/README.md), [Read-write lock](../../11_Concepts/synchronization/read_write_lock/README.md), [Send and Sync](../../11_Concepts/safety_in_languages/send_and_sync/README.md), [Sequential execution](../../11_Concepts/foundations/sequential_execution/README.md), [Speedup and Amdahl's law](../../11_Concepts/foundations/speedup_and_amdahls_law/README.md), [Thread pool and executor](../../11_Concepts/units_of_execution/thread_pool/README.md)

<a id="harmouch_ultimate_rust_for_systems_programming"></a>

## *Ultimate Rust for Systems Programming*: Master Core Programming for Architecting Secure and Reliable Software Systems with Rust and WebAssembly

Mahmoud Harmouch · 1st edition · Orange Education Pvt Ltd (AVA) · 2024  
a concurrency chapter in a broader book · on the shelf · [publisher ↗](https://orangeava.com/products/ultimate-rust-for-systems-programming) · [example code ↗](https://github.com/OrangeAVA/Ultimate-Rust-for-Systems-Programming)

<details markdown="1">
<summary>The concurrency chapters</summary>

- **7** Managing Concurrency
- **14** Asynchronous Programming

</details>

Cited on: [Async runtime (executor and reactor)](../../11_Concepts/scheduling/async_runtime/README.md)

<a id="gjengset_rust_for_rustaceans"></a>

## *Rust for Rustaceans*: Idiomatic Programming for Experienced Developers

Jon Gjengset · 1st edition · No Starch Press · 2022  
a concurrency chapter in a broader book · on the shelf · [publisher ↗](https://nostarch.com/rust-rustaceans)

<details markdown="1">
<summary>The concurrency chapters</summary>

- **8** Asynchronous Programming
- **10** Concurrency (and Parallelism)

</details>

Cited on: [Concurrency models](../../11_Concepts/foundations/concurrency_models/README.md), [Data-race freedom by construction](../../11_Concepts/safety_in_languages/data_race_freedom/README.md)

<a id="blandy_programming_rust"></a>

## *Programming Rust*: Fast, Safe Systems Development

Jim Blandy, Jason Orendorff, Leonora F. S. Tindall · 2nd edition · O'Reilly Media · 2021  
a concurrency chapter in a broader book · on the shelf · [example code ↗](https://github.com/ProgrammingRust)

<details markdown="1">
<summary>The concurrency chapters</summary>

- **19** Concurrency
- **20** Asynchronous Programming

</details>

Cited on: [Async runtime (executor and reactor)](../../11_Concepts/scheduling/async_runtime/README.md), [Fork-join](../../11_Concepts/parallelism/fork_join/README.md), [Pinning](../../11_Concepts/async/pinning/README.md), [Polling](../../11_Concepts/scheduling/polling/README.md)

<a id="mcnamara_rust_in_action"></a>

## *Rust in Action*

Tim McNamara · 1st edition · Manning Publications · 2021  
a concurrency chapter in a broader book · on the shelf · [publisher ↗](https://www.manning.com/books/rust-in-action) · [example code ↗](https://github.com/rust-in-action/code)

<details markdown="1">
<summary>The concurrency chapters</summary>

- **10** Processes, threads, and containers

</details>

<a id="kolodin_hands_on_microservices_with_rust"></a>

## *Hands-On Microservices with Rust*: Build, test, and deploy scalable and reactive microservices with Rust 2018

Denis Kolodin · 1st edition · Packt Publishing · 2019  
a concurrency chapter in a broader book · on the shelf · [example code ↗](https://github.com/PacktPublishing/Hands-On-Microservices-with-Rust)

<details markdown="1">
<summary>The concurrency chapters</summary>

- **5** Understanding Asynchronous Operations with Futures Crate
- **6** Reactive Microservices - Increasing Capacity and Performance
- **10** Background Tasks and Thread Pools in Microservices
- **11** Involving Concurrency with Actors and the Actix Crate

</details>

<a id="klabnik_nichols_rust_programming_language"></a>

## *The Rust Programming Language*

Steve Klabnik, Carol Nichols · Covers Rust 2018 edition · No Starch Press · 2019  
a concurrency chapter in a broader book · on the shelf · [example code ↗](https://github.com/rust-lang/book)

<details markdown="1">
<summary>The concurrency chapters</summary>

- **16** Fearless Concurrency
- **20** Final Project: Building a Multithreaded Web Server

</details>

Cited on: [Data-race freedom by construction](../../11_Concepts/safety_in_languages/data_race_freedom/README.md), [Message passing](../../11_Concepts/communication/message_passing/README.md), [Send and Sync](../../11_Concepts/safety_in_languages/send_and_sync/README.md)

<a id="gomez_boucher_rust_programming_by_example"></a>

## *Rust Programming By Example*: Enter the world of Rust by building engaging, concurrent, reactive, and robust applications

Antoni Boucher, Guillaume Gomez · 1st edition · Packt Publishing · 2018  
a concurrency chapter in a broader book · on the shelf · [example code ↗](https://github.com/PacktPublishing/Rust-Programming-By-Example)

<details markdown="1">
<summary>The concurrency chapters</summary>

- **9** Implementing an Asynchronous FTP Server
- **10** Implementing Asynchronous File Transfer

</details>

Cited on: [Async runtime (executor and reactor)](../../11_Concepts/scheduling/async_runtime/README.md)

<a id="kaihlavirta_mastering_rust"></a>

## *Mastering Rust*: Advanced concurrency, macros, and safe database access

Vesa Kaihlavirta · 1st edition · Packt Publishing · 2017  
a concurrency chapter in a broader book · on the shelf · [example code ↗](https://github.com/PacktPublishing/Mastering-Rust)

<details markdown="1">
<summary>The concurrency chapters</summary>

- **7** Concurrency

</details>

<a id="balbaert_rust_essentials"></a>

## *Rust Essentials*: A quick guide to writing fast, safe, and concurrent systems and applications

Ivo Balbaert · 2nd edition · Packt Publishing · 2017  
a concurrency chapter in a broader book · on the shelf · [example code ↗](https://github.com/PacktPublishing/Rust-Essentials-Second-Edition)

<details markdown="1">
<summary>The concurrency chapters</summary>

- **9** Concurrency - Coding for Multicore Execution

</details>

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
