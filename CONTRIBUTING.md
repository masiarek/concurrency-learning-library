# Conventions

House rules for writing a page here. Readers browsing lessons do not need this file; it is for whoever is about to add one.

## The rule that comes before the others

**A page never claims something a program has not printed — on both machines.** CI runs every example on `ubuntu-latest` and `macos-latest`, and an answer key is only what both agree on. A sentence that no program here backs — what a standard promises, how Erlang behaves — links its source, or the sibling library page that checks it, or ends with *(Not machine-checked here.)*

## How the library is organized

**Chapters are problems; languages live inside lessons.** A chapter is a thing that goes wrong or a thing you need — waiting for a thread, sharing a counter, a deadlock, a channel — and never a language. The language libraries already give each language its own tour. What only this library can do is put one question to several languages at once and show where their answers split.

**A lesson's languages are the ones with something to say.** The six checked here are Rust, Go, C, C++, Java and Python, **always in that order**, in tables and in sections. A lesson includes a language when its answer differs from the others', or when it is the answer the others are measured against. It leaves a language out rather than pad a row with "same as above".

**Link, do not repeat.** When a sibling library already has the deep page for one language — the Rust library's `Send` and `Sync`, say — the lesson here makes the cross-language point, shows the short program, and links there. [Resources](10_Resources/README.md) keeps the crosswalk from every topic to those pages; a new link on a lesson gets a row there too.

**Languages without a toolchain here** — Erlang, Elixir, Haskell, C# — appear as links, and as sentences ending *(Not machine-checked here.)*, until an example of theirs runs in CI.

## Deterministic about nondeterminism

Concurrency is where a recorded answer key is hardest to keep honest, because the interesting behaviour is so often the part that changes between runs. So:

- **A key records only what cannot vary.** Never the order two threads printed in, the count a race lost, a duration, a thread id or goroutine number the language does not promise, a pid, or an address.
- **Force the order you print in.** Do the work in the thread, hand the result back, and print on the joining side — or print from one thread only. When printing from the thread *is* the point, flush.
- **A sleep is a margin, never a synchronizer.** A lesson may sleep to show that something did *not* happen — a thread still asleep when the process exits — and then the competing events are at least two seconds apart: one second against three. Never sleep to make a race come out one way.
- **Show variation as variation.** What differs between runs goes in a fence whose title starts `Real runs —` and names the toolchain, the machine, the number of runs and the date. A script in the lesson's `demo/` folder, which the runner skips, produces it, and the page says how to run that script. [Who waits when main returns?](01_Threads/who_waits_when_main_returns/README.md) is the pattern.
- **An exit status or a signal is a result.** An example must itself exit 0, because the runner stops on anything else. A `.sh` driver runs the program that dies and prints how it died; [the unjoined `std::thread`](01_Threads/who_waits_when_main_returns/examples/who_waits_unjoined_cpp_sh.sh) is the pattern.

## The shape of a lesson

```
01_Threads/
  who_waits_when_main_returns/
    README.md                        the lesson
    examples/
      who_waits_rs.rs                one program per language
      who_waits_rs.out               its recorded output (generated — do not hand-edit)
      who_waits_go.go
      who_waits_go.out
      ...
      who_waits_unjoined_cpp_sh.sh   a driver, for an exit status
    demo/                            not run by CI: the scripts behind Real runs fences
```

One idea per folder. The folder name is the idea, in `lower_snake_case`, and it becomes a permanent URL — so name it for what it teaches, not where it sits in the reading order. A page names an example by its bare stem, so stems are unique across languages: the suffix is `_rs`, `_go`, `_c`, `_cpp`, `_java`, `_py` or `_sh`.

## The page

Open with the title, a `**Level:**` line (`101` / `201` / `301`, then `·`, then who it is for) and a `**One line:**` that states the claim rather than the topic. Then the table, with a row per language; then a `##` section per language in the fixed order, each with its output block, what the output shows, and its source folded inside `<details markdown="1">`; then **What to do** and **See also**. Do not hard-wrap paragraphs — one paragraph, one line.

## Output is generated, never typed

Mark the spot and let the tool fill it:

```markdown
<!-- output:who_waits_rs -->
<!-- /output -->
```

`tools/run_examples.py` runs the example and pastes what it actually printed, with a provenance line above the fence. Inside the markers is generated; outside is yours. A second kind, `<!-- source:stem -->`, pastes the program itself.

```bash
python3 tools/run_examples.py                      # verify + refill
python3 tools/run_examples.py --update --only X    # record X's output as its answer key
python3 tools/run_examples.py --check              # write nothing, fail on drift (CI)
python3 tools/check_all.py --staged                # every gate CI runs, on what you are about to commit
```

**Always pass `--only` with `--update`**, and read what it recorded before committing: `--update` accepts whatever the program printed, so it will happily enshrine a bug. For a concurrency example, run it several times before recording it — a key that is right four runs in five is a flaky test waiting for CI.

## The programs

**Rust: `rustc --edition 2024`, one file, no crates.** An async lesson that needs a runtime will have to teach the runner about Cargo first.

**Go: 1.25 or later, standard library only.** The runner does `go build -trimpath` on the one file, under `GOTOOLCHAIN=local`.

**C: C17 and POSIX threads**, built with `cc -std=c17 -Wall -Wextra -pedantic -pthread`, with `#define _POSIX_C_SOURCE 200809L` above the first `#include`. It must compile without warnings under both Apple clang and GCC.

**C++: C++20, standard library only**, built with `c++ -std=c++20 -O2 -Wall -Wextra -Wpedantic -pthread`. Without warnings, and the same output, under libc++ and libstdc++.

**Java: 25 or later, launched from source** as `java <stem>.java`. Prefer a compact source file — `void main()`, `IO.println`, no class declaration — which imports all of `java.base` by itself.

**Python: standard library, run as `python3 -I`**, and nothing newer than the Ubuntu runner's Python unless the lesson is about that version and says so.

**Shell: `bash`, in a `mktemp -d` directory, printing each command before running it** with a `say` helper, so a verified block reads like a terminal. On the Mac that is `/bin/bash` 3.2, so no `mapfile` and no `${var,,}`.

## Two machines, and a container

CI's *Show toolchain* step prints what each runner has. Add a row when CI finds a difference between them, with the date:

| | Ubuntu runner | macOS runner |
|---|---|---|
| CPU | x86-64 | arm64 |
| C and C++ | GCC, glibc, libstdc++ | Apple clang, libc++ |
| Go, Java | from `setup-go` and `setup-java` | from `setup-go` and `setup-java` |
| `bash` | 5.x | 3.2 |

The keys were recorded on 2026-09-14 on an x86-64 Mac with Apple clang 21.0.0, rustc 1.98.0, go1.25.5, OpenJDK 25.0.4.1, Python 3.14.7 and bash 3.2.57. Before the first push, the C and C++ examples were also run on Linux in the Docker image `gcc:14` (GCC 14.4, glibc 2.41) and printed the same keys.

## Links

- Link a folder by naming its `README.md` — `[label](some_folder/README.md)`, never `[label](some_folder/)`.
- **A link that leaves the library ends its label with ` ↗`**; an internal link never does. `python3 tools/check_link_style.py --fix` adds and removes them; CI runs it without `--fix`.
- A sibling library's page is linked as `https://masiarek.github.io/<library>/<chapter>/<lesson>/index.html`.

## Nav order

A new lesson folder gets a row in `NAV_ORDER` in `mkdocs_hooks.py`. Its sidebar label is its README's `# H1` with the backticks dropped; give it an entry in `LABEL_OVERRIDES` only when that H1 is too long for a sidebar. `tools/check_nav_chain.py` fails on a row naming a folder that does not exist, so commit the folder and its row together.
