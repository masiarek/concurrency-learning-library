/* The same eight numbers on one function's stack, summed by two POSIX threads
 * that hold pointers into them. This program is correct, and every part of
 * saying so is the programmer's: the two pthread_join calls come before the
 * return, so the frame that `samples` lives in outlives both threads. Move
 * either join below the return and nothing here would say a word.
 *
 *   cc -std=c17 -Wall -Wextra -pedantic -pthread lend_local_c.c -o lend_local_c && ./lend_local_c
 */
#define _POSIX_C_SOURCE 200809L

#include <pthread.h>
#include <stdio.h>

struct half {
    const long *from;
    int n;
    long sum;
};

static void *sum_half(void *arg) {
    struct half *h = arg; /* the void * was a struct half *, because we say so */
    h->sum = 0;
    for (int i = 0; i < h->n; i++) {
        h->sum += h->from[i];
    }
    return NULL;
}

static long sum_on_two_threads(void) {
    long samples[8] = {3, 1, 4, 1, 5, 9, 2, 6}; /* on this function's stack */
    struct half left = {samples, 4, 0};
    struct half right = {samples + 4, 4, 0};

    pthread_t a, b;
    pthread_create(&a, NULL, sum_half, &left);
    pthread_create(&b, NULL, sum_half, &right);
    pthread_join(a, NULL); /* both joined before... */
    pthread_join(b, NULL);

    printf("left half %ld + right half %ld\n", left.sum, right.sum);
    return left.sum + right.sum; /* ...this frame goes away */
}

int main(void) {
    printf("the total is %ld\n", sum_on_two_threads());
    return 0;
}
