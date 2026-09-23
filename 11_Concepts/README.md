# 11 — Concepts

**The structure of concurrency, as one map.** The numbered chapters teach by asking a question and running programs. This part names things. Every concept has a short page: what it is, what it is called in each language, what it connects to, and where to read more — in this library, in the sibling libraries, in the books, and in the notes this library grew from.

## Three platforms

One axis runs under everything here. It comes from Dominik Tornow's talk [*Distributed Async Await* ↗](https://www.youtube.com/watch?v=lfSIunYUsSg):

| | [Sequential](foundations/sequential_execution/README.md) | [Concurrent](foundations/concurrency/README.md) | [Distributed](distributed/distributed_computing/README.md) |
|---|---|---|---|
| Order of events | total | partial | partial |
| Failure | total | total | [partial](distributed/partial_failure/README.md) |
| Unit of composition | functions | async functions and tasks | durable, resumable executions |

A sequential program does one thing after another and, if it fails, fails as a whole. A concurrent program's steps may interleave in many orders, so only some orders are fixed — but it still lives or dies as one process. A distributed program is partially ordered *and* can lose one part while the rest keeps running, which is the source of most of what makes it hard.

## How the map is arranged

- **The ontology** — this page. Thirteen categories; inside each, concepts nested under what they are a kind of.
- **[The schema](schema/README.md)** — every other connection: what a concept is built on, what it helps prevent, what it can lead to, what it is an alternative to, and what it is often confused with, drawn as diagrams.
- **[Keywords](keywords/README.md)** — every title and alias, alphabetically, pointing at its concept.
- **[Abbreviations](abbreviations/README.md)** — CAS, RCU, TLS and the rest, each with a source.

**Concurrency primitives** — the building blocks languages provide — fall into four groups, and each group has a home here: *synchronization* primitives (mutex, semaphore, read-write lock, condition variable) are in [Synchronization](synchronization/README.md); *communication* primitives (channels, futures and promises, signals, shared memory) in [Communication](communication/README.md) and [Async](async/README.md); *thread and task management* (threads, tasks, pools) in [Units of execution](units_of_execution/README.md); *atomic* primitives (atomic variables, compare-and-swap) in [Lock-free](lock_free/README.md). See [Concurrency primitives](foundations/concurrency_primitives/README.md).

**Every concept page starts as a stub**: a one-line definition, the name of the construct in each language with a link to that language's documentation, its connections, and links outward. A stub becomes a lesson when a numbered chapter has a program that measures it, and the stub then links the lesson.

Each language also takes its own view of the same idea — a Go channel is not quite a Rust channel, and "async" means an event loop in Python and a state machine in Rust. The **In each language** table on a concept page is where those differences are named, briefly, with a link to the documentation that states them.

<!-- concepts:ontology -->

## [Foundations](foundations/README.md)

What the words mean before any language gets involved: several tasks over the same period of time, several computations at the same instant, and not waiting for an answer.

- [Concurrency](foundations/concurrency/README.md) — Structuring a program as tasks whose lifetimes overlap, so that all of them make progress over the same period of time — interleaved on one core, or at the same instant on several.
- [Parallelism](foundations/parallelism/README.md) — Running several computations at the same instant on separate processing units so the whole finishes sooner; it needs more than one core, and concurrency does not.
- [Asynchrony](foundations/asynchrony/README.md) — Starting an operation and carrying on with other work instead of waiting for it; the result arrives later, through a callback, a future, or an await.
- [Sequential execution](foundations/sequential_execution/README.md) — Steps run one after another in a fixed order, each finishing before the next starts: a single total order of events, and the baseline every concurrent program is measured against.
- [Blocking and non-blocking calls](foundations/blocking_and_nonblocking/README.md) — A blocking call does not return until its work is done, holding the caller's thread the whole time; a non-blocking call returns at once and reports that the work is not ready yet or will finish later.
- [I/O-bound and CPU-bound work](foundations/io_bound_and_cpu_bound/README.md) — Work that spends its time waiting for disks and networks gains from concurrency even on one core; work that spends its time computing gains only from parallelism.
- [Interleaving](foundations/interleaving/README.md) — One of the many orders in which the steps of concurrent tasks can actually run; a concurrent program is correct only if it is correct under every one of them.
- [Nondeterminism](foundations/nondeterminism/README.md) — The same program with the same input gives different results on different runs, because the scheduler chose a different interleaving.
- [Multitasking](foundations/multitasking/README.md) — An operating system or runtime running several tasks over the same period by switching between them — by force (preemptive) or when a task gives way (cooperative).
- [Speedup and Amdahl's law](foundations/speedup_and_amdahls_law/README.md) — How much faster more processors make a program is capped by the part that must still run sequentially: if a tenth of the work is serial, no number of cores gives more than ten times the speed.
- [Granularity](foundations/granularity/README.md) — How big the pieces of work handed to separate tasks are: too coarse leaves cores idle, too fine spends more on coordinating the pieces than on the work in them.
- [Oversubscription](foundations/oversubscription/README.md) — More busy threads than there are cores, so the machine spends its time switching between them instead of running them.
- [Concurrency models](foundations/concurrency_models/README.md) — The families of answers to how tasks share work and coordinate: threads and locks, communicating processes, actors, async tasks on an event loop, data parallelism, transactional memory.
- [Concurrency primitives](foundations/concurrency_primitives/README.md) — The building blocks a language or library provides for concurrent code, in four groups: synchronization (mutex, semaphore, condition variable), communication (channels, futures), task management (threads, tasks, pools) and atomics.

## [Units of execution](units_of_execution/README.md)

The things that run: processes, threads, and the lighter units — goroutines, virtual threads, coroutines, tasks — that runtimes schedule on top of them.

- [Process](units_of_execution/process/README.md) — A running program with its own address space, open files and at least one thread; two processes share nothing unless they arrange to.
    - [Child process](units_of_execution/subprocess/README.md) — A process started by another program, which can pass it input, read its output, wait for it and learn how it ended.
- [Thread](units_of_execution/thread/README.md) — A sequence of execution inside a process, with its own stack but sharing the process's memory with every other thread in it.
    - [Daemon and detached threads](units_of_execution/daemon_thread/README.md) — A thread that does not keep its program alive: when the program ends, the thread is stopped wherever it happens to be.
    - [Green threads and M:N scheduling](units_of_execution/green_thread/README.md) — Threads implemented by a language runtime instead of the operating system, many of them multiplexed onto a smaller number of OS threads.
        - [Goroutine](units_of_execution/goroutine/README.md) — Go's unit of concurrency: a function call started with the `go` statement and scheduled by the Go runtime onto a small pool of operating-system threads.
        - [Virtual thread](units_of_execution/virtual_thread/README.md) — Java's lightweight thread, final in JDK 21: a `Thread` that the JVM schedules onto a few carrier platform threads, cheap enough to start one per task.
    - [UI thread](units_of_execution/ui_thread/README.md) — The one thread a graphical toolkit allows to touch its widgets: long work goes to other threads or tasks, and its results are posted back to that thread.
    - [Scoped thread](units_of_execution/scoped_thread/README.md) — A thread whose life is bounded by a block: the block cannot be left until the thread has been joined, which is what lets the thread borrow the block's own local variables.
    - [Detached thread](units_of_execution/detached_thread/README.md) — A thread nobody will join: its result is unreachable, its end is unobserved, and whatever it borrowed must outlive it by some other argument.
- [Coroutine](units_of_execution/coroutine/README.md) — A function that can suspend itself part-way through and be resumed later from the same point, keeping its local state in between.
    - [Fiber](units_of_execution/fiber/README.md) — A coroutine with its own stack that is switched to explicitly — the building block several green-thread runtimes are made of.
- [Task (async)](units_of_execution/async_task/README.md) — A unit of async work handed to a runtime — a future being driven to completion — far cheaper than a thread because it holds no stack of its own while it waits.
- [Thread pool and executor](units_of_execution/thread_pool/README.md) — A set of threads that run submitted tasks one after another, so the cost of starting a thread is paid once rather than once per task.
- [Context switch](units_of_execution/context_switch/README.md) — Saving one thread's or process's CPU state and loading another's so that it can run; switching between threads is cheaper than between processes, and between async tasks cheaper still.
- [Thread-local storage](units_of_execution/thread_local_storage/README.md) — A variable with a separate copy per thread, so each thread sees only its own value and no lock is needed.

## [Scheduling](scheduling/README.md)

Who decides what runs next, when, and on which core — the operating system's scheduler, or a runtime's event loop and executor.

- [Scheduler](scheduling/scheduler/README.md) — The part of an operating system or runtime that decides which ready thread or task runs next, on which core, and for how long.
- [Event loop](scheduling/event_loop/README.md) — A loop on one thread that waits for events — a socket ready, a timer due, work finished — and runs the callbacks or resumes the tasks waiting on each.
- [Async runtime (executor and reactor)](scheduling/async_runtime/README.md) — The library that drives async tasks: an executor that polls the tasks that can make progress, and a reactor that wakes them when the I/O they wait for is ready.
- [I/O multiplexing](scheduling/io_multiplexing/README.md) — Asking the operating system to watch many sockets or file descriptors at once and report which are ready, so that one thread can serve thousands of connections.
- [Polling](scheduling/polling/README.md) — Asking repeatedly whether something is ready instead of being told; in Rust, an executor polls a future and the future answers Ready or Pending.
- [Suspension point](scheduling/suspension_point/README.md) — A place where a coroutine or async function can pause and hand control back — an await, a yield — and where other tasks may run before it resumes.
- [Busy waiting](scheduling/busy_waiting/README.md) — Waiting for a condition by checking it in a loop, burning CPU the whole time; worth it for a few nanoseconds inside a spinlock, wasteful for anything longer.
- [Scheduling policy](scheduling/scheduling_policy/README.md) — The rule a scheduler follows to pick what runs next: whether a running task can be interrupted, how priorities are set, and where idle cores find work.
    - [Preemptive scheduling](scheduling/preemptive_scheduling/README.md) — The scheduler may stop a running thread at any moment, usually on a timer interrupt, and run another — no thread can hog the CPU, and any step can be interrupted.
    - [Cooperative scheduling](scheduling/cooperative_scheduling/README.md) — A task runs until it gives way — at an await, a yield or a blocking call — so switches happen only at known points, and one task that never gives way stalls all the others.
    - [Work stealing](scheduling/work_stealing/README.md) — Each worker thread keeps its own queue of tasks, and an idle worker takes tasks from a busy worker's queue, balancing the load without one central queue.

## [Hazards](hazards/README.md)

What goes wrong: the failures that exist only because more than one thing runs at once, and why they are so hard to reproduce.

- [Safety and liveness](hazards/safety_and_liveness/README.md) — The two kinds of correctness for a concurrent program: safety means nothing bad ever happens, liveness means something good eventually does.
- [Safety failure](hazards/safety_failure/README.md) — The program reaches a state it must never reach — a lost update, a torn read, a broken invariant — usually because two tasks interleaved badly.
    - [Race condition](hazards/race_condition/README.md) — The result depends on the relative timing of tasks, and some timings give a wrong result — whether or not there is also a data race.
        - [Time of check to time of use](hazards/toctou/README.md) — Checking a condition and then acting on it as two separate steps, so that the condition can change in between — the classic check-then-act race.
        - [ABA problem](hazards/aba_problem/README.md) — A compare-and-swap succeeds because a value changed from A to B and back to A, although what it stands for is no longer the same.
    - [Data race](hazards/data_race/README.md) — Two threads access the same memory at the same time, at least one of them writing, with nothing synchronizing them — undefined behaviour in C and C++, a compile error in safe Rust.
    - [Dangling pointer](hazards/dangling_pointer/README.md) — A pointer or reference to storage whose lifetime has ended — the classic way for a thread to outlive the stack frame it was reading.
- [Weak memory models and reordering](hazards/weak_memory_model/README.md) — CPUs and compilers may perform memory reads and writes in a different order from the source code, and without synchronization another thread can see that order.
- [Liveness failure](hazards/liveness_failure/README.md) — A task that should make progress never does, though nothing has crashed: it waits for ever, spins for ever, or never gets its turn.
    - [Deadlock](hazards/deadlock/README.md) — Tasks each hold something another of them needs and wait for it, so none of them can ever continue.
    - [Livelock](hazards/livelock/README.md) — Tasks keep changing state in response to each other — backing off, retrying, stepping aside — without any of them getting work done.
    - [Starvation](hazards/starvation/README.md) — A task that is ready never gets to run, or never gets the lock, because others keep being chosen ahead of it.
    - [Priority inversion](hazards/priority_inversion/README.md) — A high-priority task waits for a lock held by a low-priority task, which is itself preempted by medium-priority work, so the most important task effectively runs last.
    - [Leaked tasks](hazards/task_leak/README.md) — A thread, goroutine or task blocked for ever on something nobody will provide, holding its memory until the process ends.
- [Heisenbug](hazards/heisenbug/README.md) — A bug that disappears or changes when you look for it — adding a print, attaching a debugger or changing the optimizer shifts the timing it depends on.
- [Contention](hazards/contention/README.md) — Tasks competing for the same lock or resource, so their time goes to waiting instead of working — the reason adding threads can make a program slower.
- [False sharing](hazards/false_sharing/README.md) — Threads writing unrelated variables that happen to sit on the same CPU cache line keep invalidating each other's cache, slowing down with no logical sharing at all.
- [Undefined behaviour](hazards/undefined_behaviour/README.md) — A program the language standard stops describing: once it has one, no requirement is placed on what it does, so a right answer on this build is not evidence of anything.

## [Synchronization](synchronization/README.md)

The primitives that make tasks take turns or wait for each other: locks, condition variables, semaphores, latches and barriers.

- [Synchronization](synchronization/synchronization/README.md) — Coordinating concurrent tasks so that their interactions happen safely — only one at a time, or one waiting until another is ready.
    - [Mutual exclusion](synchronization/mutual_exclusion/README.md) — The guarantee that at most one task is inside a critical section at any moment.
        - [Mutex](synchronization/mutex/README.md) — A lock that one task holds at a time; any other task that tries to take it waits until it is released.
            - [Spinlock](synchronization/spinlock/README.md) — A lock that waits by looping and retrying instead of sleeping, which pays off only when it is held for very short times.
            - [Read-write lock](synchronization/read_write_lock/README.md) — A lock that lets many readers in at once but lets a writer in only alone.
            - [Reentrant lock](synchronization/reentrant_lock/README.md) — A lock that the thread already holding it may take again without deadlocking itself; it is released only when every acquisition has been undone.
    - [Condition variable](synchronization/condition_variable/README.md) — Lets a thread that holds a lock sleep until another thread signals that what it waits for may now be true; wake-ups can be spurious, so the condition is checked again in a loop.
    - [Monitor](synchronization/monitor/README.md) — An object whose methods all run under one built-in lock, with condition variables for waiting inside it — Java's `synchronized` with `wait` and `notify`.
    - [Semaphore](synchronization/semaphore/README.md) — A counter of permits: taking one waits while none are left, and returning one lets a waiter in — a lock that up to n tasks may hold at once.
    - [Latch](synchronization/latch/README.md) — A one-shot gate: tasks wait on it until a set number of other tasks have each signalled, then every waiter proceeds and the gate stays open.
    - [Barrier](synchronization/barrier/README.md) — A meeting point for a fixed number of tasks: each waits there until all of them have arrived, then all continue together.
    - [Run-once initialization](synchronization/once_initialization/README.md) — Running an initializer exactly once however many threads ask for it at the same moment, and handing all of them the same result.
- [Critical section](synchronization/critical_section/README.md) — A stretch of code that touches shared state and must not be run by two tasks at once.
- [Lock poisoning](synchronization/lock_poisoning/README.md) — Marking a lock as suspect when a thread panics while holding it, so that the next thread to take it learns the data may be half-updated.
- [Scoped locking](synchronization/scoped_lock/README.md) — Tying a lock's release to leaving a scope — a guard object, `defer`, `with`, `synchronized` — so that no path out of the code can forget to unlock.
- [Lock ordering](synchronization/lock_ordering/README.md) — Always taking locks in one agreed order, so that no cycle of tasks waiting on each other — and so no deadlock — can form.
- [Futex](synchronization/futex/README.md) — A Linux kernel facility for building locks: the uncontended case is a single atomic operation in user space, and only a thread that has to wait enters the kernel.
- [Classic synchronization problems](synchronization/classic_synchronization_problems/README.md) — Small puzzles that each stand for a family of real bugs: the dining philosophers (deadlock and starvation), readers and writers, producer and consumer, the sleeping barber.

## [Lock-free](lock_free/README.md)

Sharing without locks: atomic operations, the algorithms built on them, and the memory rules that decide what one thread can see of another's writes.

- [Atomic variable](lock_free/atomic_variable/README.md) — A number or pointer whose reads, writes and increments each happen as one indivisible CPU operation, so threads can share it without a lock.
- [Compare-and-swap](lock_free/compare_and_swap/README.md) — Replace a value only if it still holds what you last read, in one atomic step; if another thread changed it first, read again and retry.
- [Lock-free](lock_free/lock_free/README.md) — A progress guarantee for a shared data structure: however the threads are scheduled, some thread always completes an operation, and there is no lock to deadlock on.
    - [Wait-free](lock_free/wait_free/README.md) — Stronger than lock-free: every thread finishes its own operation in a bounded number of its own steps, whatever the other threads do.
- [Read-copy-update](lock_free/rcu/README.md) — Readers use shared data without any lock while a writer publishes a modified copy, and the old version is freed only after every reader that might still see it has finished.
- [Happens-before](lock_free/happens_before/README.md) — The rule a memory model states for when one thread is guaranteed to see another thread's write: only when synchronization orders the write before the read.
- [Hazard pointers](lock_free/hazard_pointers/README.md) — Each thread publishes the pointers it is about to use, and memory is freed only when no thread has it published — safe memory reclamation for lock-free data structures.
- [Transactional memory](lock_free/transactional_memory/README.md) — Running a block of memory reads and writes as a transaction that either commits atomically or rolls back and retries, instead of taking locks.
- [Concurrent data structures](lock_free/concurrent_data_structures/README.md) — Queues, maps, stacks and lists built to be used by many threads at once — with locks inside, lock-free algorithms, or both — so that their callers need no synchronization of their own.

## [Communication](communication/README.md)

Tasks that hand data to each other instead of sharing it — channels, queues, actors, processes — and the patterns built from them.

- [Message passing](communication/message_passing/README.md) — Tasks share nothing and interact only by sending each other values, so that each value has one owner at a time.
    - [Channel](communication/channel/README.md) — A typed conduit between tasks: one side sends values, the other receives them, in order.
        - [Unbuffered channel](communication/unbuffered_channel/README.md) — A channel with no buffer: a send waits until a receiver takes the value, so every message is also a meeting of the two tasks.
        - [Buffered and bounded channels](communication/bounded_channel/README.md) — A channel with a fixed-size buffer: sends succeed until it is full and then wait, which is how a slow receiver pushes back on a fast sender; an unbounded channel never waits and never pushes back.
    - [Publish-subscribe and broadcast](communication/publish_subscribe/README.md) — A sender publishes to a topic and every subscriber gets its own copy, without the sender knowing who the subscribers are.
    - [Communicating sequential processes](communication/csp/README.md) — Tony Hoare's model of independent processes that interact only through synchronous channels — the idea behind Go's goroutines and channels.
    - [Actor model](communication/actor_model/README.md) — Actors are isolated units with a mailbox: each handles one message at a time, and can send messages, create actors and change its own state.
- [Shared memory](communication/shared_memory/README.md) — Tasks read and write the same memory directly and coordinate with locks or atomics — the fastest way to share data, and the easiest to get wrong.
- [Select](communication/select/README.md) — Waiting on several channel operations or futures at once, and continuing with whichever becomes ready first.
- [Backpressure](communication/backpressure/README.md) — Letting a slow consumer slow its producers down — by making sends wait or fail — instead of letting unprocessed work pile up without limit.
- [Producer-consumer](communication/producer_consumer/README.md) — One or more tasks make work items and one or more take them from a shared queue, each side running at its own speed.
- [Pipeline](communication/pipeline/README.md) — A chain of stages, each a task that reads from the previous stage's channel and writes to the next one's.
- [Fan-out, fan-in](communication/fan_out_fan_in/README.md) — Spreading the items of one channel across several workers, then merging their results back into one channel.
- [Worker pool](communication/worker_pool/README.md) — A fixed number of workers take jobs from one shared queue, which bounds how much work runs at once.
- [Supervision](communication/supervision/README.md) — Letting a failed actor or task crash and having a supervisor restart it, instead of defending against every error inside it — the approach of Erlang and OTP.
- [Inter-process communication](communication/ipc/README.md) — The ways separate processes exchange data: pipes, sockets, shared-memory segments, signals and message queues.
    - [Signals](communication/signals/README.md) — Asynchronous notifications the operating system delivers to a process — an interrupt from the keyboard, a closed pipe, a child that exited — and which, in a threaded program, one thread has to be chosen to receive.
- [Task queue](communication/task_queue/README.md) — A queue of jobs that workers take and run — within one program, or across processes and machines with a broker in between.
- [Dataflow programming](communication/dataflow/README.md) — A program as a graph of blocks through which data flows, each block running when its inputs are ready — so the graph, not the programmer, decides what runs in parallel.
- [OTP behaviours](communication/otp_behaviours/README.md) — Erlang/OTP's reusable process patterns — a generic server, a supervisor, an application — where the library owns the concurrency and your module supplies the callbacks.

## [Async](async/README.md)

Not waiting: callbacks, futures and promises, async and await, and what cancelling, timing out and blocking mean once a task can pause.

- [Event-driven programming](async/event_driven_programming/README.md) — A program built as handlers that run when events arrive — a click, a message, a ready socket — instead of as one flow from top to bottom.
- [Callback](async/callback/README.md) — A function handed to an operation to be called when the operation finishes — the oldest way to write asynchronous code, and the source of deeply nested callback code.
- [Future and promise](async/future_and_promise/README.md) — A placeholder for a result that is not ready yet: the future is the side that waits for the value, the promise the side that supplies it.
- [Async and await](async/async_await/README.md) — Syntax that lets asynchronous code read like sequential code: an async function returns a future, and await pauses the caller until that future resolves, without blocking the thread.
- [Async functions as state machines](async/async_state_machine/README.md) — A compiler turns an async function into a state machine whose states are its suspension points, storing the local variables that live across each await.
- [Structured concurrency](async/structured_concurrency/README.md) — Concurrent tasks are started inside a scope that does not end until all of them have, so no task outlives the code that started it and every error reaches that code.
- [Cancellation](async/cancellation/README.md) — Asking a running task to stop early and release what it holds; in most languages the task has to cooperate by noticing the request.
- [Timeout](async/timeout/README.md) — Giving up on an operation after a time limit — which, in concurrent code, means cancelling or abandoning whatever was still running on its behalf.
- [Join](async/join/README.md) — Waiting for a thread or task to finish, usually receiving its result or its failure through a handle.
- [Function coloring](async/function_coloring/README.md) — An async function can call a sync one, but not the other way round without help, so async-ness spreads up the call graph and splits libraries into two colors.
- [Async stream](async/async_stream/README.md) — An asynchronous iterator: a sequence whose items arrive over time, each one awaited in turn.
- [Pinning](async/pinning/README.md) — Rust's guarantee that a value will not move in memory, needed because an async state machine may hold pointers into itself.
- [Blocking the event loop](async/blocking_the_event_loop/README.md) — A task that computes for a long time, or makes a blocking call, on the runtime's thread stops every other task on that thread until it is done.
- [Reactive programming](async/reactive_programming/README.md) — Describing a program as streams of values over time and the values derived from them, with changes propagating through automatically.
- [Timers and tickers](async/timers/README.md) — A runtime facility that fires once after a delay, or repeatedly at an interval, and delivers it as a callback, a value on a channel, or something to await.

## [Parallelism](parallelism/README.md)

Using more cores to finish sooner: splitting data and work across them, and the hardware facts that decide whether it helps.

- [Data parallelism](parallelism/data_parallelism/README.md) — The same operation applied to many pieces of data at once, each piece on its own core or vector lane.
    - [Map-reduce](parallelism/map_reduce/README.md) — Apply a function to every item independently, then combine the results with an associative operation, so that both halves can be split across workers.
    - [Parallel prefix sum](parallelism/parallel_prefix_sum/README.md) — Computing every running total of a sequence in a number of rounds that grows with the logarithm of its length — a building block of many data-parallel algorithms.
    - [Parallel iterators and streams](parallelism/parallel_iterators/README.md) — A library that spreads an iterator's work over a thread pool with one method call — Rayon's `par_iter`, Java's `parallelStream`.
    - [SIMD](parallelism/simd/README.md) — One CPU instruction applied to several numbers at once: parallelism inside a single core.
    - [GPU computing](parallelism/gpu_computing/README.md) — Running thousands of small data-parallel computations on a graphics processor instead of the CPU.
- [Task parallelism](parallelism/task_parallelism/README.md) — Different tasks, possibly doing different things, running at the same time on different cores.
    - [Fork-join](parallelism/fork_join/README.md) — Split a task into subtasks, run them in parallel, wait for all of them and combine their results — recursively, until the pieces are small enough to do directly.
- [OpenMP](parallelism/openmp/README.md) — Compiler directives and a runtime that parallelize loops and sections of C, C++ and Fortran programs over shared memory.
- [MPI](parallelism/mpi/README.md) — The Message Passing Interface: separate processes, often on separate machines, exchanging messages — the standard for distributed-memory parallel programs.
- [NUMA](parallelism/numa/README.md) — Non-uniform memory access: on a multi-socket machine some memory is closer to some cores, so where a thread runs changes how fast its memory is.
- [Simultaneous multithreading](parallelism/smt/README.md) — One physical core presenting two or more logical cores to the operating system, sharing its execution resources between them.
- [Cache coherence](parallelism/cache_coherence/README.md) — Keeping several cached copies of the same data consistent when one of them is written — done in hardware between a CPU's cores, at a cost that false sharing exposes.
- [Global interpreter lock](parallelism/gil/README.md) — A lock that lets only one thread run interpreter code at a time — CPython's, and Ruby's — so threads give concurrency but not CPU parallelism; CPython 3.13 added an optional build without it.
- [Multiprocessing](parallelism/multiprocessing/README.md) — Using several processes instead of several threads — for isolation, or to get parallelism in a runtime whose threads share one global lock.
- [Parallel algorithms](parallelism/parallel_algorithms/README.md) — Sorting, searching, graph and numeric algorithms rebuilt so that their work splits across cores — not always by the obvious split.

## [Safety in languages](safety_in_languages/README.md)

How languages and libraries promise that code is safe to share — thread safety, reentrancy, ownership, immutability — and the formal conditions that say what correct means.

- [Thread safety](safety_in_languages/thread_safety/README.md) — Code or data is thread-safe if it behaves correctly when used from several threads at once, without its callers adding any synchronization.
- [Reentrancy](safety_in_languages/reentrancy/README.md) — A function is reentrant if it can be entered again — by another thread, a signal handler, or itself — before an earlier call has finished, usually because it keeps its state in structures the caller owns instead of in statics.
- [Send and Sync](safety_in_languages/send_and_sync/README.md) — Rust's two marker traits: a `Send` value may move to another thread, a `Sync` value may be shared with one by reference, and the compiler checks both.
- [Data-race freedom by construction](safety_in_languages/data_race_freedom/README.md) — A language rule that makes data races impossible to write in the first place — Rust's ownership with Send and Sync, or actors that never share memory.
- [Immutability](safety_in_languages/immutability/README.md) — Data that cannot change after it is built can be shared by any number of threads with no synchronization at all.
- [Interior mutability](safety_in_languages/interior_mutability/README.md) — Changing data behind a shared reference through a type that enforces the rules itself — `Cell` and `RefCell` within one thread, `Mutex` and atomics across threads.
- [Thread confinement](safety_in_languages/thread_confinement/README.md) — Keeping a piece of data reachable from one thread only — a GUI's main thread, a goroutine that owns its state — so that it needs no synchronization.
- [Linearizability](safety_in_languages/linearizability/README.md) — A concurrent object is linearizable if every operation appears to take effect at a single instant between its start and its end, so it can be reasoned about as if it were sequential.
- [Sequential consistency](safety_in_languages/sequential_consistency/README.md) — Operations appear to happen in some single order that respects each task's own order, though not necessarily real time — weaker than linearizability.
- [Object lifetime](safety_in_languages/object_lifetime/README.md) — The span in which a value's storage is valid, and the question of who guarantees that every reference to it is dropped first — the compiler, the programmer, or a garbage collector.
- [Escape analysis](safety_in_languages/escape_analysis/README.md) — The compiler deciding whether a local's address can outlive its frame, and moving the local to the heap when it can — which is how a language with a garbage collector lets a thread capture a local safely.

## [Distributed systems](distributed/README.md)

When the tasks are on different machines: partial failure, no shared clock, and the protocols that reach agreement anyway.

- [Distributed computing](distributed/distributed_computing/README.md) — Tasks on separate machines that communicate over a network: their events are only partially ordered, and one part can fail while the rest keeps running.
- [Partial failure](distributed/partial_failure/README.md) — In a distributed system one component can fail while the others continue, and a caller often cannot tell a slow peer from a dead one.
- [Clock skew and drift](distributed/clock_skew/README.md) — Skew is how far apart two machines' clocks are at one moment, drift how fast they move apart — the reason timestamps from different machines cannot reliably order events.
- [Logical clocks](distributed/logical_clocks/README.md) — Counters that order events by cause instead of by wall-clock time: a Lamport clock gives every event a consistent order, a vector clock can also tell that two events were concurrent.
- [Consensus](distributed/consensus/README.md) — Getting a group of machines to agree on one value, or one log of commands, even though some of them fail — the problem Paxos and Raft solve.
- [Idempotency](distributed/idempotency/README.md) — An operation that has the same effect whether it runs once or several times, which is what makes retrying after a timeout safe.
- [Consistency models](distributed/consistency_models/README.md) — The promise a distributed store makes about what a reader will see — from strong consistency, where every read sees the latest write, to eventual consistency, where replicas agree only in the end.
- [Multi-version concurrency control](distributed/mvcc/README.md) — Keeping several versions of each record so that readers see a consistent snapshot while writers add new versions, instead of readers and writers locking each other out.
- [Remote procedure call](distributed/rpc/README.md) — Calling a function that runs on another machine as though it were local — convenient until the network fails in a way no local call can.
- [Durable execution](distributed/durable_execution/README.md) — Recording a long-running workflow's progress — checkpoints, an event log — so that after a crash it resumes where it stopped instead of starting over.

## [Real-time systems](real_time/README.md)

When a late answer is a wrong answer: deadlines, worst-case timing, and the scheduling policies that can prove every deadline is met.

- [Real-time system](real_time/real_time_system/README.md) — A system whose correctness depends on when results arrive as well as on what they are: a hard real-time system must never miss a deadline, a soft one should rarely.
- [Worst-case execution time](real_time/wcet/README.md) — The longest a piece of code can take on given hardware; real-time schedules are built from this bound, never from typical timings.
- [Rate-monotonic scheduling](real_time/rate_monotonic_scheduling/README.md) — Fixed priorities by period: the task that runs most often gets the highest priority, which is optimal among fixed-priority policies for periodic tasks.
- [Earliest deadline first](real_time/earliest_deadline_first/README.md) — Dynamic priorities: whichever ready task has the nearest deadline runs next.

## [Testing and tools](testing_and_tools/README.md)

Finding concurrency bugs on purpose: race detectors, deterministic schedulers, stress runs, model checkers, and the tools that show what every thread is waiting for.

- [Race detector](testing_and_tools/race_detector/README.md) — A tool that instruments memory accesses as the program runs and reports the data races that actually happened in that run — ThreadSanitizer, Go's `-race`.
- [Deterministic scheduling for tests](testing_and_tools/deterministic_testing/README.md) — Running concurrent code under a controlled scheduler or a fake clock, so that an interleaving or a timeout can be reproduced on demand — Rust's loom, Go's `testing/synctest`.
- [Stress testing](testing_and_tools/stress_testing/README.md) — Running concurrent code many times, under load and with many threads, so that rare interleavings get a chance to show up.
- [Model checking](testing_and_tools/model_checking/README.md) — Exploring every state and interleaving of a model of a program — in TLA+, SPIN, or loom — to prove a property or produce a counterexample.
- [Debugging concurrent programs](testing_and_tools/concurrency_debugging/README.md) — Thread dumps, deadlock detectors and tracing that show what every thread or task is waiting for at a given moment.
- [Profiling concurrent programs](testing_and_tools/profiling_concurrency/README.md) — Measuring where the time goes when many threads run — waiting for locks, waiting to be scheduled, and bouncing cache lines — and not only which functions are hot.
- [Memory error detector](testing_and_tools/memory_error_detector/README.md) — A tool that instruments allocations and stack frames so that reading or writing storage whose lifetime has ended is reported at run time — AddressSanitizer, Valgrind's Memcheck.

<!-- /concepts:ontology -->
