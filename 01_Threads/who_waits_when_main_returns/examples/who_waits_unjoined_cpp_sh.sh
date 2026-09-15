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
