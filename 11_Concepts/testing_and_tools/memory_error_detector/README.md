# Memory error detector

**Category:** [Testing and tools](../README.md) · **Status:** stub · **Lessons:** chapter 09, Testing and tools *(planned)*

**One line:** A tool that instruments allocations and stack frames so that reading or writing storage whose lifetime has ended is reported at run time — AddressSanitizer, Valgrind's Memcheck.

Also called: AddressSanitizer, ASan, Valgrind, Memcheck.

## How it connects


- **See also:** [Dangling pointer](../../hazards/dangling_pointer/README.md), [Debugging concurrent programs](../concurrency_debugging/README.md), [Race detector](../race_detector/README.md)

## In each language

| | |
|---|---|
| Rust | [Miri ↗](https://github.com/rust-lang/miri) interprets MIR and reports undefined behaviour in `unsafe` code, including dangling references |
| C | [`-fsanitize=address` ↗](https://clang.llvm.org/docs/AddressSanitizer.html) in Clang and GCC alike; `ASAN_OPTIONS=detect_stack_use_after_return=1` adds the frames a function has already returned from |
| C++ | The same flag, plus [`-fsanitize=undefined` ↗](https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html) for the checks that are not about memory |

## Where to read more

- **In this library:** [Can a thread borrow a local variable?](../../../01_Threads/lending_a_local_to_a_thread/README.md)
- **Reference:** [AddressSanitizer ↗](https://clang.llvm.org/docs/AddressSanitizer.html)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
