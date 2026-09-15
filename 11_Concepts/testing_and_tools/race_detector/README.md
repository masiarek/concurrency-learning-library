# Race detector

**Category:** [Testing and tools](../README.md) · **Status:** stub · **Lessons:** chapter 09, Testing and tools *(planned)*

**One line:** A tool that instruments memory accesses as the program runs and reports the data races that actually happened in that run — ThreadSanitizer, Go's `-race`.

Also called: ThreadSanitizer, TSan, go -race, Helgrind.

## How it connects


- **See also:** [Data race](../../hazards/data_race/README.md), [Heisenbug](../../hazards/heisenbug/README.md)

## In each language

| | |
|---|---|
| Rust | Unstable [`-Zsanitizer=thread` ↗](https://doc.rust-lang.org/unstable-book/compiler-flags/sanitizer.html#threadsanitizer) on supported targets, usually with `-Zbuild-std` |
| Go | [`go test -race` ↗](https://go.dev/doc/articles/race_detector): needs cgo, and typically costs 5-10x memory and 2-20x time |
| C | [ThreadSanitizer ↗](https://clang.llvm.org/docs/ThreadSanitizer.html): compile and link with `-fsanitize=thread` in Clang or [GCC ↗](https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html); typical slowdown 5x-15x |
| C++ | The same [ThreadSanitizer ↗](https://clang.llvm.org/docs/ThreadSanitizer.html) `-fsanitize=thread`, which also reports lock-order inversions |
| Python | CPython itself can be built with [`--with-thread-sanitizer` ↗](https://docs.python.org/3/using/configure.html#cmdoption-with-thread-sanitizer) (added in 3.13) |
| Elsewhere | Valgrind's [Helgrind ↗](https://valgrind.org/docs/manual/hg-manual.html) finds data races, lock-ordering problems and misuses of the pthreads API |

## Where to read more

- **In this library:** [Is total += n safe on two threads?](../../../02_Shared_State/the_lost_update/README.md)
- **In a sibling library:** [Rust: Data races — ThreadSanitizer on a C counter ↗](https://masiarek.github.io/rust-learning-library/31_C_and_Cpp/data_races/index.html)
- **In a sibling library:** [Go: The race detector ↗](https://masiarek.github.io/go-learning-library/07_Testing_Concurrent_Code/the_race_detector/index.html)
- **In the books:** [*Async Rust*](../../../10_Resources/books_rust/README.md#flitton_morton_async_rust), Maxwell Flitton, Caroline Morton — ch. 11, 'Testing' → 'Testing for Race Conditions'
- **In the books:** [*The Go Programming Language*](../../../10_Resources/books_go/README.md#donovan_kernighan_go_programming_language), Alan A. A. Donovan, Brian W. Kernighan — ch. 9, 'Concurrency with Shared Variables' → 'The Race Detector'
- **In the books:** [*Go Systems Programming*](../../../10_Resources/books_go/README.md#tsoukalos_go_systems_programming), Mihalis Tsoukalos — ch. 10, 'Goroutines — Advanced Features' → 'Detecting race conditions'
- **In the books:** [*Concurrency in Go*](../../../10_Resources/books_go/README.md#cox_buday_concurrency_in_go), Katherine Cox-Buday — ch. A, 'Appendix' → 'Race Detection'
- **Reference:** [ThreadSanitizer manual ↗](https://github.com/google/sanitizers/wiki/ThreadSanitizerCppManual)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
