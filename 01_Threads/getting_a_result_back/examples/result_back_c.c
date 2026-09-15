/* Getting a result back. In C, a thread function returns a void *, and
 * pthread_join's second argument receives it. What it points to, and what
 * counts as failure, is a contract between the two functions.
 *
 *   cc -std=c17 -Wall -Wextra -pedantic -pthread result_back_c.c -o result_back_c && ./result_back_c
 */
#define _POSIX_C_SOURCE 200809L

#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

static void *sum_to_100(void *arg) {
    (void)arg;
    /* The result must outlive this thread's stack, so it lives on the heap
       and the joining thread frees it. */
    unsigned long *total = malloc(sizeof *total);
    if (total == NULL) {
        return NULL;
    }
    *total = 0;
    for (unsigned long i = 1; i <= 100; i++) {
        *total += i;
    }
    return total;
}

static void *no_total_today(void *arg) {
    (void)arg;
    return NULL; /* "failure", because this program says NULL means failure */
}

int main(void) {
    pthread_t t;
    pthread_create(&t, NULL, sum_to_100, NULL);

    void *returned;
    int rc = pthread_join(t, &returned);
    unsigned long *total = returned;
    printf("pthread_join returned %d, and handed back a pointer to %lu\n", rc, *total);
    free(total);

    pthread_create(&t, NULL, no_total_today, NULL);
    rc = pthread_join(t, &returned);
    printf("pthread_join returned %d, and handed back %s\n", rc,
           returned == NULL ? "NULL" : "a pointer");
    return 0;
}
