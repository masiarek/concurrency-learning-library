#!/usr/bin/env bash
# The same program in C. It has the same data race as the Go one and the same
# invariant answer, and the compiler -- with every warning this library builds
# with turned on -- says nothing at all. The program is not run here: a data
# race in C is undefined behaviour, so what it prints is not an answer key.
set -u

dir=$(mktemp -d)
trap 'rm -rf "$dir"' EXIT

cat >"$dir/same_value.c" <<'C'
#define _POSIX_C_SOURCE 200809L

#include <pthread.h>
#include <stdio.h>

static int shared;

static void *write_one(void *arg) {
    (void)arg;
    shared = 1; /* both threads write the same 1 */
    return NULL;
}

int main(void) {
    pthread_t writers[2];
    for (int i = 0; i < 2; i++) {
        pthread_create(&writers[i], NULL, write_one, NULL);
    }
    for (int i = 0; i < 2; i++) {
        pthread_join(writers[i], NULL);
    }
    printf("shared is %d\n", shared);
    return 0;
}
C

say() { printf '$ %s\n' "$*"; }

say 'cc -std=c17 -Wall -Wextra -pedantic -pthread same_value.c -o same_value'
(cd "$dir" && "${CC:-cc}" -std=c17 -Wall -Wextra -pedantic -pthread same_value.c -o same_value 2>diagnostic.txt)
status=$?
if [ -s "$dir/diagnostic.txt" ]; then
    echo "the compiler printed:"
    cat "$dir/diagnostic.txt"
else
    echo "the compiler printed nothing"
fi
echo "cc exit status $status"
if [ -x "$dir/same_value" ]; then
    echo "a binary was built"
fi
