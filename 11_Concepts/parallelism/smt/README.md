# Simultaneous multithreading

**Category:** [Parallelism](../README.md) · **Status:** stub

**One line:** One physical core presenting two or more logical cores to the operating system, sharing its execution resources between them.

Also called: SMT, Hyper-Threading.

## In each language

| | |
|---|---|
| Go | [`runtime.NumCPU` ↗](https://pkg.go.dev/runtime#NumCPU) counts logical CPUs |
| Python | [`os.cpu_count` ↗](https://docs.python.org/3/library/os.html#os.cpu_count) returns logical CPUs |
| C# | [`Environment.ProcessorCount` ↗](https://learn.microsoft.com/en-us/dotnet/api/system.environment.processorcount) counts logical processors, capped by CPU affinity and CPU limits |
| JavaScript | [`navigator.hardwareConcurrency` ↗](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/hardwareConcurrency) counts logical processors |
| The operating system | [`sched_setaffinity(2)` ↗](https://man7.org/linux/man-pages/man2/sched_setaffinity.2.html) pins a thread to chosen logical CPUs |

## Where to read more

- **Notes:** [HW - CPUs - pipelines - caching - HT - memory bandwidth - latency ↗](https://docs.google.com/document/u/0/d/12TY3QDOenDFezomACTM7BV3rKpFnrADXMT5q8Yc653Q/edit)
- **Reference:** [Wikipedia: Simultaneous multithreading ↗](https://en.wikipedia.org/wiki/Simultaneous_multithreading)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
