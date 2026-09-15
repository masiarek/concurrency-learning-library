/* The lost update, forced. `total += 1` is three steps -- load, add, store --
 * and nothing stops ten threads from all loading the same old total. A gate
 * made of a mutex and a condition variable holds every thread between its load
 * and its store, so every load happens before any store, on every run.
 *
 * `total` is an atomic_long, so each load and each store is one indivisible
 * operation and the program has no data race: its behaviour is defined. The
 * pair of operations is still not atomic.
 *
 *   cc -std=c17 -Wall -Wextra -pedantic -pthread lost_update_c.c -o lost_update_c && ./lost_update_c
 */
#define _POSIX_C_SOURCE 200809L

#include <pthread.h>
#include <stdatomic.h>
#include <stdio.h>

enum { HANDLERS = 10 };

static atomic_long total;

static pthread_mutex_t gate_lock = PTHREAD_MUTEX_INITIALIZER;
static pthread_cond_t gate_opened = PTHREAD_COND_INITIALIZER;
static int loaded_so_far;

/* Return only once all HANDLERS threads have called this: a hand-made barrier. */
static void wait_until_all_have_loaded(void) {
    pthread_mutex_lock(&gate_lock);
    loaded_so_far++;
    if (loaded_so_far == HANDLERS) {
        pthread_cond_broadcast(&gate_opened);
    }
    while (loaded_so_far < HANDLERS) {
        pthread_cond_wait(&gate_opened, &gate_lock);
    }
    pthread_mutex_unlock(&gate_lock);
}

static void *handle(void *arg) {
    long *seen = arg;
    *seen = atomic_load(&total);     /* 1. load */
    wait_until_all_have_loaded();    /* every handler has loaded */
    atomic_store(&total, *seen + 1); /* 2. add, 3. store */
    return NULL;
}

int main(void) {
    pthread_t threads[HANDLERS];
    long loaded[HANDLERS];
    for (int i = 0; i < HANDLERS; i++) {
        pthread_create(&threads[i], NULL, handle, &loaded[i]);
    }
    for (int i = 0; i < HANDLERS; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("%d handlers each added 1 to a total that started at 0\n", HANDLERS);
    printf("the totals they loaded:");
    for (int i = 0; i < HANDLERS; i++) {
        printf(" %ld", loaded[i]);
    }
    printf("\nthe total is %ld, not %d\n", atomic_load(&total), HANDLERS);
    return 0;
}
