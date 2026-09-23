# Stress testing

**Category:** [Testing and tools](../README.md) · **Status:** stub · **Lessons:** [chapter 09, Testing and tools](../../../09_Testing_and_Tools/README.md)

**One line:** Running concurrent code many times, under load and with many threads, so that rare interleavings get a chance to show up.

Also called: jcstress.

## How it connects


- **See also:** [Nondeterminism](../../foundations/nondeterminism/README.md)

## In each language

| | |
|---|---|
| Go | [`go test -count n -cpu 1,2,4` ↗](https://pkg.go.dev/cmd/go#hdr-Testing_flags) repeats each test under several `GOMAXPROCS` values; [`stress` ↗](https://pkg.go.dev/golang.org/x/tools/cmd/stress) runs a process in parallel in a loop to catch sporadic failures |
| Java | [jcstress ↗](https://github.com/openjdk/jcstress), the OpenJDK harness and test suite for the correctness of concurrency support in the JVM, class libraries and hardware |
| Python | [`sys.setswitchinterval` ↗](https://docs.python.org/3/library/sys.html#sys.setswitchinterval) sets how often the interpreter switches between threads |
| Kotlin | [Lincheck ↗](https://kotlinlang.org/docs/lincheck-guide.html) offers stress testing beside its model checking strategy |

## Where to read more

- **In this library:** [How do you write a test that provokes the race?](../../../09_Testing_and_Tools/a_stress_test_that_actually_races/README.md)
- **In this library:** [How does a test wait an hour in a millisecond?](../../../09_Testing_and_Tools/virtual_time_in_tests/README.md)
- **In the books:** [*Distributed Systems with Node.js*](../../../10_Resources/books_javascript/README.md#hunter_distributed_systems_with_nodejs), Thomas Hunter II — ch. 8, 'Resilience' → 'Resilience Testing'

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
