# CLAUDE.md — Concurrency learning library

Standing guidance for Claude working in this repo. Created 2026-09-14, when Adam asked for a concurrency library organized "by topics and within the topic different languages or links to other libraries".

## What this is

A learning library in the same format as its siblings (Rust, C, C++, Python, Java text, Linux, Perl, Ruby text, Encodings): one idea per page, every claim backed by a program whose output is an answer key checked in CI. What is new here is that a lesson is one question put to six languages — Rust, Go, C, C++, Java, Python — so its table and its sections carry a row and a program per language. Public repo `masiarek/concurrency-learning-library`, site <https://masiarek.github.io/concurrency-learning-library/>.

**The rules live in [CONTRIBUTING.md](CONTRIBUTING.md)** — above all "How the library is organized" and "Deterministic about nondeterminism". This file carries only the operational context.

## Toolchains on this Mac (measured 2026-09-14)

- `cc` / `c++` — Apple clang 21.0.0 with libc++, x86-64.
- `rustc` 1.98.0 from rustup, with the `rust-src` component: the standard library's source is under `$(rustc --print sysroot)/lib/rustlib/src/rust/library/std/src`, which is how the first lesson's explanation of cut-off lines was checked (`io/stdio.rs` `cleanup`, called from `rt.rs`).
- `go` 1.25.5 (Homebrew). `java` OpenJDK 25.0.4.1. `python3` 3.14.7. `/bin/bash` 3.2.57.
- Not installed: Erlang, Elixir, GHC. `dotnet` is 5.0, too old to use. `pdftotext` is at `/usr/local/bin/pdftotext`.
- Docker images for the Linux column: `gcc:14` (GCC 14.4, glibc 2.41, g++, python3; no Go, Java or Rust), `rust:1-slim`, `golang:1.25-alpine`, `python:3.1x-slim`. There is no JDK image yet, so the Linux Java column is CI's. Pass `--ulimit fsize=104857600` to every container probe.

## The books

The PDFs behind [Resources](10_Resources/README.md) are on this disk: `/Volumes/T7/Concurrent` (Williams, Breshears, and Adam's own notes `spawn and join.docx`, whose question — why a two-thread Rust program printed less than expected — became the first lesson), `/Volumes/T7/Go programming` (Cox-Buday, Cutajar, Serdar, Charpentier), `/Volumes/T7/C++` (Williams 2nd ed.), `/Volumes/T7/Haskell` (Marlow), `/Volumes/T7/C# C Sharp` (Terrell, Duffy), `/Volumes/T7/Elixir`, `/Volumes/T7/Erlang`, `/Volumes/T7/Linux Unix` (Love).

## Working with Adam

- **Be self-driven**: build, verify, commit, push, then report — flag only what is genuinely uncertain.
- Several sessions may share a checkout: run `git status` before numbering a chapter, gate with `tools/check_all.py --staged`, and stage only your own paths. If master has diverged from origin, work in a `git worktree add --detach <path> origin/master` and push from there.
- **Never `-m` a commit message that contains backticks** — the shell runs them. Write the message to a file and use `-F`.
- Markdown is not hard-wrapped.
