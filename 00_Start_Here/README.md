# 00 — Start here

**Level:** 101 · read this first

This library is for someone who writes one of six languages — Rust, Go, C, C++, Java, Python — and has met, or is about to meet, more than one thing happening at once: a thread whose output never appeared, a counter that comes out wrong one run in ten, a program that hangs only under load, an `async` function that stalls everything around it.

## What it assumes

One of the six languages well enough to read short programs in the others. No example is longer than a screen, and a page says what a construct does the first time it uses one.

## How a page is laid out

- **One line** — the claim, stated plainly enough that it could be wrong.
- **A table** with a row per language — the answer in brief.
- **A section per language**, always in the order Rust, Go, C, C++, Java, Python: the verified output first, then what it shows, then the program itself, folded away.
- **What to do**, and **See also** — including the sibling library that has the deep page for one of the languages.

## What "verified" means when threads are involved

An output block on a page is what the program printed on both CI machines — Ubuntu and macOS — and on the Mac where it was recorded. For a concurrency library that is a hard constraint, because the interesting behaviour is often exactly the part that changes from one run to the next. So the programs are written to print only what cannot vary: a value handed back by a join, a line that did or did not appear, an exit status.

What does vary is shown as variation, in a fence titled **Real runs**, with the machine, the toolchain, the number of runs and the date. That fence is not an answer key, and your machine will count differently. Beside it, the lesson's `demo/` folder holds the script that produced it, so you can count for yourself.

## Read in this order

1. [**Who waits when main returns?**](../01_Threads/who_waits_when_main_returns/README.md) — the question a first threaded program raises, and why the six languages answer it differently.
2. [**Getting a result back**](../01_Threads/getting_a_result_back/README.md) — where a thread's answer goes, and where its failure goes.

Then keep [**the concept map**](../11_Concepts/README.md) open beside the lessons: every term a lesson uses has a page there, with its name in each language and links to where it is taught — here, in the [Go library ↗](https://masiarek.github.io/go-learning-library/), the [Rust library ↗](https://masiarek.github.io/rust-learning-library/), and the books.

## The toolchains

| Language | Keys recorded with | In CI |
|---|---|---|
| Rust | rustc 1.98.0 | the runner image's `rustc` |
| Go | go1.25.5 | Go 1.25, from `actions/setup-go` |
| C | Apple clang 21.0.0 | GCC on Ubuntu, Apple clang on macOS |
| C++ | Apple clang 21.0.0 with libc++ | GCC with libstdc++ on Ubuntu, Apple clang with libc++ on macOS |
| Java | OpenJDK 25.0.4.1 | Temurin 25, from `actions/setup-java` |
| Python | Python 3.14.7 | the runner image's `python3` |

The Mac that recorded the keys is an x86-64 machine. [CONTRIBUTING.md](../CONTRIBUTING.md) has the rules for each language's programs.
