/* Who waits when main returns? In C, nothing: returning from main is calling
 * exit(), and exit() ends the process with every thread in it.
 *
 *   cc -std=c17 -Wall -Wextra -pedantic -pthread who_waits_c.c -o who_waits_c && ./who_waits_c
 */
#define _POSIX_C_SOURCE 200809L

#include <pthread.h>
#include <stdio.h>
#include <unistd.h>

static void *worker(void *arg) {
    (void)arg;
    sleep(1);
    printf("worker thread:  finished\n");
    return NULL;
}

int main(void) {
    pthread_t t;
    pthread_create(&t, NULL, worker, NULL);
    printf("main:           returning\n");
    return 0;
}
