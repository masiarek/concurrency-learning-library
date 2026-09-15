/* Four threads, a million additions each, to a plain long with nothing guarding
 * it. Prints how many additions were lost. This is a data race, which makes the
 * program's behaviour undefined: the count is what one build happened to do. */
#define _POSIX_C_SOURCE 200809L

#include <pthread.h>
#include <stdio.h>

enum { THREADS = 4, EACH = 1000000 };

static long total;

static void *add(void *arg) {
    (void)arg;
    for (int i = 0; i < EACH; i++) {
        total += 1;
    }
    return NULL;
}

int main(void) {
    pthread_t threads[THREADS];
    for (int i = 0; i < THREADS; i++) {
        pthread_create(&threads[i], NULL, add, NULL);
    }
    for (int i = 0; i < THREADS; i++) {
        pthread_join(threads[i], NULL);
    }
    printf("%ld\n", (long)THREADS * EACH - total);
    return 0;
}
