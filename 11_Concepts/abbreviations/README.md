# Abbreviations

The short forms that turn up in concurrency books and documentation. Each has a source; an abbreviation we could not find a source for is left out rather than guessed at.

| Short form | Stands for | Concept | Source |
|---|---|---|---|
| ABA | the A → B → A sequence of values behind the ABA problem (not an acronym) | [ABA problem](../hazards/aba_problem/README.md) | [source ↗](https://en.wikipedia.org/wiki/ABA_problem) |
| ACID | atomicity, consistency, isolation, durability — the guarantees of a database transaction | [Consistency models](../distributed/consistency_models/README.md) | [source ↗](https://en.wikipedia.org/wiki/ACID) |
| BASE | basically available, soft state, eventually consistent — the usual contrast with ACID | [Consistency models](../distributed/consistency_models/README.md) | [source ↗](https://en.wikipedia.org/wiki/Eventual_consistency) |
| CAS | compare-and-swap | [Compare-and-swap](../lock_free/compare_and_swap/README.md) | [source ↗](https://en.wikipedia.org/wiki/Compare-and-swap) |
| CSP | communicating sequential processes | [Communicating sequential processes](../communication/csp/README.md) | [source ↗](https://en.wikipedia.org/wiki/Communicating_sequential_processes) |
| EDF | earliest deadline first | [Earliest deadline first](../real_time/earliest_deadline_first/README.md) | [source ↗](https://en.wikipedia.org/wiki/Earliest_deadline_first_scheduling) |
| FIFO | first in, first out — the order a channel or queue delivers in | [Channel](../communication/channel/README.md) | [source ↗](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics)) |
| futex | fast user-space mutex | [Futex](../synchronization/futex/README.md) | [source ↗](https://man7.org/linux/man-pages/man2/futex.2.html) |
| GCD | Grand Central Dispatch, Apple's task-queue concurrency library | [Thread pool and executor](../units_of_execution/thread_pool/README.md) | [source ↗](https://developer.apple.com/documentation/dispatch) |
| GIL | global interpreter lock | [Global interpreter lock](../parallelism/gil/README.md) | [source ↗](https://docs.python.org/3/glossary.html#term-global-interpreter-lock) |
| GPGPU | general-purpose computing on graphics processing units | [GPU computing](../parallelism/gpu_computing/README.md) | [source ↗](https://en.wikipedia.org/wiki/General-purpose_computing_on_graphics_processing_units) |
| IOCP | I/O completion port, Windows' mechanism for asynchronous I/O | [I/O multiplexing](../scheduling/io_multiplexing/README.md) | [source ↗](https://learn.microsoft.com/en-us/windows/win32/fileio/i-o-completion-ports) |
| IPC | inter-process communication (in CPU performance, the same letters also mean instructions per cycle) | [Inter-process communication](../communication/ipc/README.md) | [source ↗](https://en.wikipedia.org/wiki/Inter-process_communication) |
| M:N | M user-level threads scheduled onto N operating-system threads | [Green threads and M:N scheduling](../units_of_execution/green_thread/README.md) | [source ↗](https://en.wikipedia.org/wiki/Thread_(computing)#Threading_models) |
| MPI | Message Passing Interface | [MPI](../parallelism/mpi/README.md) | [source ↗](https://www.mpi-forum.org/) |
| MPSC | multi-producer, single-consumer — the shape of Rust's `std::sync::mpsc` channel; SPSC and MPMC are the other shapes | [Channel](../communication/channel/README.md) | [source ↗](https://doc.rust-lang.org/std/sync/mpsc/index.html) |
| MVCC | multi-version concurrency control | [Multi-version concurrency control](../distributed/mvcc/README.md) | [source ↗](https://en.wikipedia.org/wiki/Multiversion_concurrency_control) |
| NIO | New I/O, Java's buffer-and-channel I/O API (`java.nio`), which includes non-blocking I/O | [I/O multiplexing](../scheduling/io_multiplexing/README.md) | [source ↗](https://en.wikipedia.org/wiki/Non-blocking_I/O_(Java)) |
| NTP | Network Time Protocol | [Clock skew and drift](../distributed/clock_skew/README.md) | [source ↗](https://en.wikipedia.org/wiki/Network_Time_Protocol) |
| NUMA | non-uniform memory access | [NUMA](../parallelism/numa/README.md) | [source ↗](https://en.wikipedia.org/wiki/Non-uniform_memory_access) |
| PTP | Precision Time Protocol | [Clock skew and drift](../distributed/clock_skew/README.md) | [source ↗](https://en.wikipedia.org/wiki/Precision_Time_Protocol) |
| RAII | resource acquisition is initialization — the idiom behind scoped lock guards | [Scoped locking](../synchronization/scoped_lock/README.md) | [source ↗](https://en.wikipedia.org/wiki/Resource_acquisition_is_initialization) |
| RCU | read-copy-update | [Read-copy-update](../lock_free/rcu/README.md) | [source ↗](https://en.wikipedia.org/wiki/Read-copy-update) |
| RMS | rate-monotonic scheduling | [Rate-monotonic scheduling](../real_time/rate_monotonic_scheduling/README.md) | [source ↗](https://en.wikipedia.org/wiki/Rate-monotonic_scheduling) |
| RPC | remote procedure call (RMI, remote method invocation, is Java's object-oriented form) | [Remote procedure call](../distributed/rpc/README.md) | [source ↗](https://en.wikipedia.org/wiki/Remote_procedure_call) |
| SIMD | single instruction, multiple data | [SIMD](../parallelism/simd/README.md) | [source ↗](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data) |
| SMT | simultaneous multithreading (Intel's brand name for it is Hyper-Threading) | [Simultaneous multithreading](../parallelism/smt/README.md) | [source ↗](https://en.wikipedia.org/wiki/Simultaneous_multithreading) |
| STM | software transactional memory | [Transactional memory](../lock_free/transactional_memory/README.md) | [source ↗](https://en.wikipedia.org/wiki/Software_transactional_memory) |
| TLS | thread-local storage (not to be confused with Transport Layer Security) | [Thread-local storage](../units_of_execution/thread_local_storage/README.md) | [source ↗](https://en.wikipedia.org/wiki/Thread-local_storage) |
| TOCTOU | time of check to time of use (also written TOCTTOU) | [Time of check to time of use](../hazards/toctou/README.md) | [source ↗](https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use) |
| TSan | ThreadSanitizer | [Race detector](../testing_and_tools/race_detector/README.md) | [source ↗](https://github.com/google/sanitizers/wiki/ThreadSanitizerCppManual) |
| TSO | total store order, the memory model of x86 processors (x86-TSO) | [Weak memory models and reordering](../hazards/weak_memory_model/README.md) | [source ↗](https://www.cl.cam.ac.uk/~pes20/weakmemory/) |
| WCET | worst-case execution time | [Worst-case execution time](../real_time/wcet/README.md) | [source ↗](https://en.wikipedia.org/wiki/Worst-case_execution_time) |

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
