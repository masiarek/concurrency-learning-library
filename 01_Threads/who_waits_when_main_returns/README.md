# Who waits when main returns?

**Level:** 101 · anyone who has started a thread and lost its output

**One line:** When `main` returns, a Rust, Go, C or C++ program ends, and every thread still running ends with it, mid-line if need be; Java and Python wait for their ordinary threads first — and each of the six has a construct that does the opposite of its default.

## The question

Two threads that print, and a `main` that prints and returns. This is the shape of the first program in Mara Bos's [*Rust Atomics and Locks* ↗](https://marabos.nl/atomics/basics.html), with the messages changed:

```rust
use std::thread;

fn main() {
    thread::spawn(worker);
    thread::spawn(worker);
    println!("main: hello");
}

fn worker() {
    println!("worker: hello");
    let id = thread::current().id();
    println!("worker: my id is {id:?}");
}
```

Five lines, if everything prints. Here is the same program run 300 times, with each distinct transcript counted and each newline shown as `|`:

```text title="Real runs — rustc 1.98.0, x86-64 Mac, macOS 26, 300 runs, 2026-09-14"
  88 main: hello|worker: hello|worker: my id is 
  82 main: hello|worker: hello|worker: my id is ThreadId(
  46 main: hello|worker: hello|worker: my id is ThreadId
  20 main: hello|worker: hello|
  16 main: hello|worker: hello|worker: my id is ThreadId(2)|
  16 main: hello|
   7 main: hello|worker: hello|worker: my id is ThreadId(3)|
   6 main: hello|worker: hello|worker: hello|worker: my id is 
   3 worker: hello|worker: my id is ThreadId(3)|worker: hello|worker: my id is ThreadId(2)|main: hello|
   2 main: hello|worker: hello|worker: my id is ThreadId(2)|worker: hello|
   2 main: hello|worker: hello|worker: my id is ThreadId(2
   2 main: hello|worker: hello|worker: hello|
   1 worker: hello|worker: my id is ThreadId(3)|main: hello|worker: hello|worker: my id is ThreadId(2)|
   1 worker: hello|worker: my id is ThreadId(3)|main: hello|worker: hello|
   1 worker: hello|worker: my id is ThreadId(2)|worker: hello|worker: my id is ThreadId(3)|main: hello|
   1 worker: hello|worker: my id is ThreadId(2)|main: hello|worker: hello|worker: my id is ThreadId(
   1 worker: hello|worker: my id is ThreadId(2)|main: hello|worker: hello|
   1 worker: hello|worker: hello|main: hello|worker: my id is ThreadId(3)|
   1 worker: hello|worker: hello|main: hello|worker: my id is ThreadId(2)
   1 worker: hello|worker: hello|main: hello|worker: my id is ThreadId(
   1 main: hello|worker: hello|worker: my id is ThreadId(3)
   1 main: hello|worker: hello|worker: hello|worker: my id is ThreadId
```

Twenty-two different transcripts from one program. Five of the 300 runs printed all five lines. Sixteen printed only `main: hello`. And 229 stopped in the middle of a line — after `my id is `, after `ThreadId`, after `ThreadId(` — with no newline to follow.

Nothing crashed, and nothing is wrong with `println!`. `main` returned while the workers were still running, and the process ended, taking them with it. The documentation for [`std::thread` ↗](https://doc.rust-lang.org/std/thread/index.html) says so in one sentence: when the main thread of a Rust program ends, the whole program shuts down, even if other threads are still running.

**Why a line can stop halfway.** After `main` returns, Rust's runtime runs a cleanup step before the process exits ([`rt.rs` ↗](https://github.com/rust-lang/rust/blob/1.98.0/library/std/src/rt.rs)). Part of it ([`cleanup` in `io/stdio.rs` ↗](https://github.com/rust-lang/rust/blob/1.98.0/library/std/src/io/stdio.rs)) flushes standard output and replaces its line buffer with one of zero capacity, provided no thread holds stdout's lock at that instant. From then on, a worker's `println!` is no longer held back until its newline: each piece of the formatted line is written as soon as it is produced — the text before `{id:?}`, then `ThreadId`, `(`, the number, `)`, and finally the newline — and the process can end between any two of them. The fragments in the tally are those pieces.

To count on your own machine, run `bash demo/tally.sh` from this folder. Your list will not match this one; that is the point of it.

## Six languages, one question

The programs below leave nothing to chance. Each worker sleeps before it prints — one second when something should wait for it, three seconds when nothing should — so a line either appears or it does not, on any machine.

| | A thread still running when `main` returns | Waits | Does not wait |
|---|---|---|---|
| Rust | ends with the process | `thread::scope` | `thread::spawn` |
| Go | ends with the process | nothing waits by itself; a `sync.WaitGroup` is a wait you write | `go f()` |
| C | ends with the process: returning from `main` calls `exit` | `pthread_exit` at the end of `main` | `return` from `main` |
| C++ | never gets that far unless its `std::thread` was joined or detached: the program aborts | `std::jthread` | a detached `std::thread` |
| Java | is waited for, unless it is a daemon — and every virtual thread is one | a platform thread | a virtual thread |
| Python | is waited for, unless it is a daemon | a `threading.Thread` | a thread started with `daemon=True` |

## Rust

<!-- output:who_waits_rs -->
*Verified output of [`who_waits_rs.rs`](examples/who_waits_rs.rs) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
thread in a scope:  finished
main:               returning
```
<!-- /output -->

`thread::scope` returned only after its thread had printed. The thread from `thread::spawn` was still asleep when `main` returned, and it never printed. `spawn` hands back a [`JoinHandle` ↗](https://doc.rust-lang.org/std/thread/struct.JoinHandle.html); this program drops it without calling `join`, and a dropped handle detaches its thread. `scope` is the other answer: it cannot return until every thread started inside it has finished, which is also what lets a scoped thread borrow the caller's local variables — the Rust library's [Spawning a thread ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/spawning_a_thread/index.html) shows that half.

<details markdown="1">
<summary><code>who_waits_rs.rs</code></summary>

<!-- source:who_waits_rs -->
*[`who_waits_rs.rs`](examples/who_waits_rs.rs) in full — pasted here by `tools/run_examples.py` from the file CI runs.*

```rust
//! Who waits when main returns? In Rust, nothing waits for a spawned thread:
//! returning from main ends the process. `thread::scope` is the construct that waits.
//!
//!   rustc --edition 2024 who_waits_rs.rs -o who_waits_rs && ./who_waits_rs

use std::thread;
use std::time::Duration;

fn main() {
    // `scope` does not return until every thread started inside it has finished.
    thread::scope(|s| {
        s.spawn(|| {
            thread::sleep(Duration::from_secs(1));
            println!("thread in a scope:  finished");
        });
    });

    // `spawn` hands back a JoinHandle. Dropping it detaches the thread; nothing waits.
    thread::spawn(|| {
        thread::sleep(Duration::from_secs(3));
        println!("spawned thread:     finished");
    });

    println!("main:               returning");
}
```
<!-- /source -->

</details>

## Go

<!-- output:who_waits_go -->
*Verified output of [`who_waits_go.go`](examples/who_waits_go.go) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
goroutine in a WaitGroup:  finished
main:                      returning
```
<!-- /output -->

The [Go specification ↗](https://go.dev/ref/spec#Program_execution) settles this in its section on program execution: when `main` returns, the program exits, and it does not wait for other goroutines to complete. There is no handle to join and no flag to change that. A program that must wait counts its goroutines with a `sync.WaitGroup`: `wg.Go` adds one, starts the goroutine, and marks it done when the function returns. `wg.Go` arrived in Go 1.25; before it, the same program calls `wg.Add(1)` and defers `wg.Done()` itself. The Go library's [`main` does not wait ↗](https://masiarek.github.io/go-learning-library/01_Goroutines/main_does_not_wait/index.html) goes further: the deferred calls that never run in a goroutine cut off this way, and the four ways a Go program can end.

<details markdown="1">
<summary><code>who_waits_go.go</code></summary>

<!-- source:who_waits_go -->
*[`who_waits_go.go`](examples/who_waits_go.go) in full — pasted here by `tools/run_examples.py` from the file CI runs.*

```go
// Who waits when main returns? In Go, nothing waits for a goroutine: when main
// returns, the program exits. A sync.WaitGroup is a wait you write yourself.
//
//	go build who_waits_go.go && ./who_waits_go
package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var wg sync.WaitGroup
	wg.Go(func() { // Go 1.25: Add(1), start the goroutine, Done() when it returns
		time.Sleep(1 * time.Second)
		fmt.Println("goroutine in a WaitGroup:  finished")
	})
	wg.Wait()

	go func() {
		time.Sleep(3 * time.Second)
		fmt.Println("plain goroutine:           finished")
	}()

	fmt.Println("main:                      returning")
}
```
<!-- /source -->

</details>

## C

Two programs that differ only in their last line. The first returns from `main`:

<!-- output:who_waits_c -->
*Verified output of [`who_waits_c.c`](examples/who_waits_c.c) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
main:           returning
```
<!-- /output -->

The second calls `pthread_exit` instead:

<!-- output:who_waits_pthread_exit_c -->
*Verified output of [`who_waits_pthread_exit_c.c`](examples/who_waits_pthread_exit_c.c) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
main:           calling pthread_exit
worker thread:  finished
```
<!-- /output -->

Returning from `main` is [equivalent to calling `exit` ↗](https://en.cppreference.com/w/c/language/main_function) with the value returned, and `exit` ends the process with every thread in it. `pthread_exit` ends only the thread that calls it. Called at the end of `main`, it leaves the worker running, and [POSIX ↗](https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_exit.html) specifies what happens next: once the last thread has ended, the process exits with status 0, as if `exit(0)` had been called then.

<details markdown="1">
<summary><code>who_waits_c.c</code> and <code>who_waits_pthread_exit_c.c</code></summary>

<!-- source:who_waits_c -->
*[`who_waits_c.c`](examples/who_waits_c.c) in full — pasted here by `tools/run_examples.py` from the file CI runs.*

```c
/* Who waits when main returns? In C, nothing: returning from main is calling
 * exit(), and exit() ends the process with every thread in it.
 *
 *   cc -std=c17 -Wall -Wextra -pedantic -pthread who_waits_c.c -o who_waits_c && ./who_waits_c
 */
#define _POSIX_C_SOURCE 200809L

#include <pthread.h>
#include <stdio.h>
#include <unistd.h>

static void *worker(void *arg) {
    (void)arg;
    sleep(1);
    printf("worker thread:  finished\n");
    return NULL;
}

int main(void) {
    pthread_t t;
    pthread_create(&t, NULL, worker, NULL);
    printf("main:           returning\n");
    return 0;
}
```
<!-- /source -->

<!-- source:who_waits_pthread_exit_c -->
*[`who_waits_pthread_exit_c.c`](examples/who_waits_pthread_exit_c.c) in full — pasted here by `tools/run_examples.py` from the file CI runs.*

```c
/* The same program, except that main ends with pthread_exit instead of return.
 * pthread_exit ends the calling thread only; the process lives on until its
 * last thread has ended, and then exits as if exit(0) had been called.
 *
 *   cc -std=c17 -Wall -Wextra -pedantic -pthread who_waits_pthread_exit_c.c -o w && ./w
 */
#define _POSIX_C_SOURCE 200809L

#include <pthread.h>
#include <stdio.h>
#include <unistd.h>

static void *worker(void *arg) {
    (void)arg;
    sleep(1);
    printf("worker thread:  finished\n");
    return NULL;
}

int main(void) {
    pthread_t t;
    pthread_create(&t, NULL, worker, NULL);
    printf("main:           calling pthread_exit\n");
    pthread_exit(NULL);
}
```
<!-- /source -->

</details>

## C++

<!-- output:who_waits_cpp -->
*Verified output of [`who_waits_cpp.cpp`](examples/who_waits_cpp.cpp) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
std::jthread:          finished
main:                  returning
```
<!-- /output -->

A [`std::jthread` joins in its destructor ↗](https://en.cppreference.com/w/cpp/thread/jthread/~jthread), after asking its thread to stop, so the block around it did not end until the thread had printed. The `std::thread` was detached, and a detached thread ends with the process, as in Rust and Go.

The `detach()` is not optional. The program a C++ reader usually writes first — start a `std::thread`, then return — never reaches the question, because destroying a `std::thread` that was neither joined nor detached [calls `std::terminate` ↗](https://en.cppreference.com/w/cpp/thread/thread/~thread):

<!-- output:who_waits_unjoined_cpp_sh -->
*Verified output of [`who_waits_unjoined_cpp_sh.sh`](examples/who_waits_unjoined_cpp_sh.sh) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
$ c++ -std=c++20 -O2 -pthread unjoined.cpp -o unjoined
$ ./unjoined
main: returning without join() or detach()
exit status 134: killed by signal 6, SIGABRT
```
<!-- /output -->

Exit status 134 is 128 plus 6, and signal 6 is `SIGABRT` — the same arithmetic as the 141, 128 plus `SIGPIPE`'s 13, in the Linux library's [head closes the pipe early ↗](https://masiarek.github.io/linux-learning-library/01_Pipelines/head_closes_the_pipe_early/index.html): the [default terminate handler calls `std::abort` ↗](https://en.cppreference.com/w/cpp/error/terminate). libc++ and libstdc++ print different messages to stderr on the way down; the script drops them and keeps what the two agree on.

<details markdown="1">
<summary><code>who_waits_cpp.cpp</code> and <code>who_waits_unjoined_cpp_sh.sh</code></summary>

<!-- source:who_waits_cpp -->
*[`who_waits_cpp.cpp`](examples/who_waits_cpp.cpp) in full — pasted here by `tools/run_examples.py` from the file CI runs.*

```cpp
// Who waits when main returns? In C++ it depends on the class: a std::jthread
// joins in its destructor, and a detached std::thread is ended with the process.
//
//   c++ -std=c++20 -O2 -Wall -Wextra -Wpedantic -pthread who_waits_cpp.cpp -o who_waits_cpp && ./who_waits_cpp

#include <chrono>
#include <iostream>
#include <thread>

using namespace std::chrono_literals;

int main() {
    {
        std::jthread waited([] {
            std::this_thread::sleep_for(1s);
            std::cout << "std::jthread:          finished\n";
        });
    }  // ~jthread() asks the thread to stop, then joins it

    std::thread detached([] {
        std::this_thread::sleep_for(3s);
        std::cout << "detached std::thread:  finished\n";
    });
    detached.detach();  // without this, ~thread() would call std::terminate

    std::cout << "main:                  returning\n";
}
```
<!-- /source -->

<!-- source:who_waits_unjoined_cpp_sh -->
*[`who_waits_unjoined_cpp_sh.sh`](examples/who_waits_unjoined_cpp_sh.sh) in full — pasted here by `tools/run_examples.py` from the file CI runs.*

```bash
#!/usr/bin/env bash
# The C++ program a reader writes first: a std::thread that main neither joins
# nor detaches. Its destructor calls std::terminate, which aborts the process.
# The two standard libraries word the abort differently on stderr, so this
# script keeps what they agree on: main's line, and the exit status.
set -u

dir=$(mktemp -d)
trap 'rm -rf "$dir"' EXIT

cat >"$dir/unjoined.cpp" <<'CPP'
#include <iostream>
#include <thread>

int main() {
    std::thread worker([] {});
    std::cout << "main: returning without join() or detach()" << std::endl;
}
CPP

say() { printf '$ %s\n' "$*"; }

say 'c++ -std=c++20 -O2 -pthread unjoined.cpp -o unjoined'
"${CXX:-c++}" -std=c++20 -O2 -Wall -Wextra -Wpedantic -pthread "$dir/unjoined.cpp" -o "$dir/unjoined"

say './unjoined'
# `exit $?` keeps the subshell alive to reap the program, so bash's own
# "Aborted" report goes to the subshell's stderr, which is /dev/null.
(cd "$dir" && ./unjoined; exit $?) 2>/dev/null
status=$?
echo "exit status $status: killed by signal $((status - 128)), SIG$(kill -l $((status - 128)))"
```
<!-- /source -->

</details>

## Java

<!-- output:who_waits_java -->
*Verified output of [`who_waits_java.java`](examples/who_waits_java.java) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
platform thread is a daemon: false
virtual thread is a daemon:  true
main:             returning
platform thread:  finished
```
<!-- /output -->

The platform thread printed and the virtual thread did not. The [`Thread` documentation ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Thread.html) states both halves: the JVM's shutdown sequence begins when all started non-daemon threads have terminated, and virtual threads are daemon threads, so they do not hold it back. The two `isDaemon` lines show the defaults for threads started from `main`.

So moving work from platform threads to virtual threads changes what happens at exit: a task that used to keep the JVM running until it finished is now cut off when `main` returns.

<details markdown="1">
<summary><code>who_waits_java.java</code></summary>

<!-- source:who_waits_java -->
*[`who_waits_java.java`](examples/who_waits_java.java) in full — pasted here by `tools/run_examples.py` from the file CI runs.*

```java
// Who waits when main returns? In Java, the JVM does: it will not exit while a
// thread that is not a daemon is still running. A virtual thread is always a daemon.
//
//   java who_waits_java.java      (Java 25: a compact source file, no class declaration)

void main() {
    Thread platform = Thread.ofPlatform().start(() -> work("platform thread:", 1));
    Thread virtual = Thread.ofVirtual().start(() -> work("virtual thread: ", 3));

    IO.println("platform thread is a daemon: " + platform.isDaemon());
    IO.println("virtual thread is a daemon:  " + virtual.isDaemon());
    IO.println("main:             returning");
}

void work(String label, int seconds) {
    try {
        Thread.sleep(seconds * 1000L);
    } catch (InterruptedException e) {
        return;
    }
    IO.println(label + "  finished");
}
```
<!-- /source -->

</details>

## Python

<!-- output:who_waits_py -->
*Verified output of [`who_waits_py.py`](examples/who_waits_py.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
main:             end of the script
ordinary thread:  finished
```
<!-- /output -->

The end of the script is not the end of the program. The [`threading` documentation ↗](https://docs.python.org/3/library/threading.html) says a Python program exits when only daemon threads are left, so the interpreter waited a second for the ordinary thread, then ended the daemon thread while it was still asleep. The same page warns that daemon threads are stopped abruptly at shutdown, without releasing what they hold, and recommends an ordinary thread and a signal such as an `Event` for work that has to stop cleanly.

<details markdown="1">
<summary><code>who_waits_py.py</code></summary>

<!-- source:who_waits_py -->
*[`who_waits_py.py`](examples/who_waits_py.py) in full — pasted here by `tools/run_examples.py` from the file CI runs.*

```python
"""Who waits when main returns? In Python, the interpreter does: it will not exit
while a thread that is not a daemon is still running. A daemon thread is ended.

    python3 who_waits_py.py
"""

import threading
import time


def worker(label: str, seconds: int) -> None:
    time.sleep(seconds)
    print(f"{label}  finished", flush=True)


ordinary = threading.Thread(target=worker, args=("ordinary thread:", 1))
daemon = threading.Thread(target=worker, args=("daemon thread:  ", 3), daemon=True)
ordinary.start()
daemon.start()

print("main:             end of the script", flush=True)
```
<!-- /source -->

</details>

## What to do

- **Join what you start, or start it inside something that joins for you**: `thread::scope` in Rust, a `sync.WaitGroup` in Go, `pthread_join` in C, `std::jthread` in C++, and in Java and Python an executor that is closed at the end of a `try` or `with` block — the next lesson uses both.
- **Treat "daemon" and "detached" as a decision to lose work at exit**, and make that decision on purpose.
- **A last line that never appeared is a clue about the end of the program**, not about the thread. When a thread's output stops short, especially in the middle of a line, ask what was supposed to wait for it before asking what went wrong inside it.

## See also

- [Getting a result back](../getting_a_result_back/README.md) — the next lesson: a join is also how a thread's answer, and its failure, comes back.
- The Rust library's [Spawning a thread ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/spawning_a_thread/index.html) — `JoinHandle`, `move`, and `thread::scope` in depth.
- [*Rust Atomics and Locks*, chapter 1 ↗](https://marabos.nl/atomics/basics.html) — where the program at the top of this page comes from.
- The Rust library's [Standard error, and exit status ↗](https://masiarek.github.io/rust-learning-library/02_Errors/stderr_and_exit_status/index.html) and the Encodings library's [A pipe is not a terminal ↗](https://masiarek.github.io/encodings-learning-library/06_Terminal/pipe_is_not_a_terminal/index.html) — the other way output goes missing at exit: a buffer that nothing flushes.
- The Go library's [A panic ends the whole program ↗](https://masiarek.github.io/go-learning-library/01_Goroutines/a_panic_ends_the_whole_program/index.html) — the other way a Go program ends without waiting.
- Concepts: [Thread](../../11_Concepts/units_of_execution/thread/README.md) · [Daemon and detached threads](../../11_Concepts/units_of_execution/daemon_thread/README.md) · [Join](../../11_Concepts/async/join/README.md) · [Structured concurrency](../../11_Concepts/async/structured_concurrency/README.md) · [Nondeterminism](../../11_Concepts/foundations/nondeterminism/README.md) · [Process](../../11_Concepts/units_of_execution/process/README.md)
