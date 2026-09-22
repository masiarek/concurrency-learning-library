#!/usr/bin/env bash
# The C mirror of the Rust program that does not compile: a function starts a
# thread pointing at its own locals and returns the pthread_t, leaving the
# caller to join. By the time the thread reads, the frame it is reading has
# gone. Every warning this library builds with is on, and the compiler has
# nothing to say.
#
# The program is not run here. Reading a dead stack frame is undefined
# behaviour, so what it prints is not an answer key; demo/use_after_return.sh
# runs it under AddressSanitizer instead.
set -u

dir=$(mktemp -d)
trap 'rm -rf "$dir"' EXIT

cat >"$dir/dangling.c" <<'C'
#define _POSIX_C_SOURCE 200809L

#include <pthread.h>
#include <stdio.h>
#include <time.h>

struct half {
    const long *from;
    int n;
    long sum;
};

static void *sum_half(void *arg) {
    struct half *h = arg;
    /* A second's margin, so that the read below certainly happens after
       start_summing has returned. It is not synchronizing anything. */
    nanosleep(&(struct timespec){1, 0}, NULL);
    h->sum = 0;
    for (int i = 0; i < h->n; i++) {
        h->sum += h->from[i]; /* `from` points into a frame that is gone */
    }
    return NULL;
}

static pthread_t start_summing(void) {
    long samples[8] = {3, 1, 4, 1, 5, 9, 2, 6};
    struct half left = {samples, 4, 0};

    pthread_t a;
    pthread_create(&a, NULL, sum_half, &left);
    return a; /* `samples` and `left` die here; the thread still holds them */
}

int main(void) {
    pthread_t a = start_summing();
    pthread_join(a, NULL);
    printf("joined\n");
    return 0;
}
C

say() { printf '$ %s\n' "$*"; }

say 'cc -std=c17 -Wall -Wextra -pedantic -pthread dangling.c -o dangling'
(cd "$dir" && "${CC:-cc}" -std=c17 -Wall -Wextra -pedantic -pthread dangling.c -o dangling 2>diagnostic.txt)
status=$?
if [ -s "$dir/diagnostic.txt" ]; then
    echo "the compiler printed:"
    cat "$dir/diagnostic.txt"
else
    echo "the compiler printed nothing"
fi
echo "cc exit status $status"
if [ -x "$dir/dangling" ]; then
    echo "a binary was built, and this script does not run it"
fi
