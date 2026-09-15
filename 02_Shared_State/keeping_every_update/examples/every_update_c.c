/* Keeping every update, three ways. Eight handlers each add the numbers 1 to
 * 10,000 to one total: under a pthread mutex, with a C11 atomic add, and by
 * writing every number into a pipe that one thread reads and adds up.
 *
 *   cc -std=c17 -Wall -Wextra -pedantic -pthread every_update_c.c -o every_update_c && ./every_update_c
 */
#define _POSIX_C_SOURCE 200809L

#include <pthread.h>
#include <stdatomic.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

enum { HANDLERS = 8, LAST = 10000 };

static void run_handlers(void *(*handler)(void *), void *arg) {
    pthread_t threads[HANDLERS];
    for (int i = 0; i < HANDLERS; i++) {
        pthread_create(&threads[i], NULL, handler, arg);
    }
    for (int i = 0; i < HANDLERS; i++) {
        pthread_join(threads[i], NULL);
    }
}

/* --- with a mutex --- */

static pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
static long locked_total;

static void *add_under_the_lock(void *arg) {
    (void)arg;
    for (long n = 1; n <= LAST; n++) {
        pthread_mutex_lock(&lock);
        locked_total += n; /* load, add and store, all while holding the lock */
        pthread_mutex_unlock(&lock);
    }
    return NULL;
}

/* --- with an atomic add --- */

static atomic_long atomic_total;

static void *add_atomically(void *arg) {
    (void)arg;
    for (long n = 1; n <= LAST; n++) {
        atomic_fetch_add(&atomic_total, n); /* one indivisible operation */
    }
    return NULL;
}

/* --- with one owner, reading a pipe --- */

static void *send_numbers(void *arg) {
    int write_end = *(int *)arg;
    for (long n = 1; n <= LAST; n++) {
        /* A write of at most PIPE_BUF bytes is never interleaved with another. */
        if (write(write_end, &n, sizeof n) != sizeof n) {
            abort();
        }
    }
    return NULL;
}

static void *own_the_total(void *arg) {
    int read_end = *(int *)arg;
    long *total = malloc(sizeof *total); /* no other thread can reach this */
    *total = 0;
    long n;
    ssize_t got;
    /* Each write put a whole long into the pipe, so a read of one long gets a
       whole long, and 0 means every write end is closed. */
    while ((got = read(read_end, &n, sizeof n)) == sizeof n) {
        *total += n;
    }
    if (got != 0) {
        abort();
    }
    return total;
}

static long with_one_owner(void) {
    int ends[2];
    if (pipe(ends) != 0) {
        abort();
    }
    pthread_t owner;
    pthread_create(&owner, NULL, own_the_total, &ends[0]);
    run_handlers(send_numbers, &ends[1]);
    close(ends[1]); /* the owner's next read returns 0 */

    void *result;
    pthread_join(owner, &result);
    long total = *(long *)result;
    free(result);
    close(ends[0]);
    return total;
}

int main(void) {
    printf("%d handlers each add 1 to %d; the total should be %ld\n", HANDLERS, LAST,
           (long)HANDLERS * LAST * (LAST + 1) / 2);

    run_handlers(add_under_the_lock, NULL);
    printf("with a pthread mutex:  %ld\n", locked_total);

    run_handlers(add_atomically, NULL);
    printf("with atomic_fetch_add: %ld\n", atomic_load(&atomic_total));

    printf("with one owner:        %ld\n", with_one_owner());
    return 0;
}
