/* The same program, except that main ends with pthread_exit instead of return.
 * pthread_exit ends the calling thread only; the process lives on until its
 * last thread has ended, and then exits as if exit(0) had been called.
 *
 *   cc -std=c17 -Wall -Wextra -pedantic -pthread who_waits_pthread_exit_c.c -o w && ./w
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
    printf("main:           calling pthread_exit\n");
    pthread_exit(NULL);
}
