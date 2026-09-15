/* Splitting a sum across workers. Each thread adds its own run of values into a
 * variable no other thread can see, and the partial sums are then combined two
 * ways: one after another, and as a tree whose rounds add pairs at the same time.
 * Then the same split, with doubles.
 *
 * C has no generics, so every function comes twice: once for long, once for
 * double. Each thread's job is the same in both: add up `count` values,
 * starting at `from`.
 *
 *   cc -std=c17 -Wall -Wextra -pedantic -pthread split_sum_c.c -o split_sum_c && ./split_sum_c
 */
#define _POSIX_C_SOURCE 200809L

#include <pthread.h>
#include <stdio.h>

enum { COUNT = 24, WORKERS = 8 }; /* a power of two, so every round pairs everyone up */

static const long VALUES[COUNT] = {1, 4, 3, 9, 2, 8, 5, 1, 1, 6, 2, 7,
                                   2, 5, 0, 4, 1, 8, 6, 5, 1, 2, 3, 9};

struct long_job {
    const long *from;
    int count;
    long sum;
};

struct double_job {
    const double *from;
    int count;
    double sum;
};

static void *add_longs(void *arg) {
    struct long_job *job = arg;
    long my_sum = job->from[0];
    for (int i = 1; i < job->count; i++) {
        my_sum += job->from[i];
    }
    job->sum = my_sum;
    return NULL;
}

static void *add_doubles(void *arg) {
    struct double_job *job = arg;
    double my_sum = job->from[0];
    for (int i = 1; i < job->count; i++) {
        my_sum += job->from[i];
    }
    job->sum = my_sum;
    return NULL;
}

/* Run each of n jobs on its own thread, and wait for all of them. */
static void run_all(void *(*work)(void *), void *jobs, size_t job_size, int n) {
    pthread_t threads[COUNT];
    for (int i = 0; i < n; i++) {
        pthread_create(&threads[i], NULL, work, (char *)jobs + (size_t)i * job_size);
    }
    for (int i = 0; i < n; i++) {
        pthread_join(threads[i], NULL);
    }
}

/* Partial sums: one job per worker, each over an equal run of values. */
static void partial_longs(const long *values, long *sums) {
    struct long_job jobs[WORKERS];
    for (int w = 0; w < WORKERS; w++) {
        jobs[w] = (struct long_job){values + w * (COUNT / WORKERS), COUNT / WORKERS, 0};
    }
    run_all(add_longs, jobs, sizeof jobs[0], WORKERS);
    for (int w = 0; w < WORKERS; w++) {
        sums[w] = jobs[w].sum;
    }
}

static void partial_doubles(const double *values, double *sums) {
    struct double_job jobs[WORKERS];
    for (int w = 0; w < WORKERS; w++) {
        jobs[w] = (struct double_job){values + w * (COUNT / WORKERS), COUNT / WORKERS, 0};
    }
    run_all(add_doubles, jobs, sizeof jobs[0], WORKERS);
    for (int w = 0; w < WORKERS; w++) {
        sums[w] = jobs[w].sum;
    }
}

/* The tree: each round is one job per neighbouring pair, all at once. The
   results overwrite the front of `level`, so it shrinks by half every round. */
static long tree_longs(long *level, int *additions, int *rounds, int show_rounds) {
    *additions = *rounds = 0;
    for (int n = WORKERS; n > 1; n /= 2) {
        struct long_job jobs[WORKERS];
        for (int i = 0; i < n / 2; i++) {
            jobs[i] = (struct long_job){level + 2 * i, 2, 0};
        }
        run_all(add_longs, jobs, sizeof jobs[0], n / 2);
        for (int i = 0; i < n / 2; i++) {
            level[i] = jobs[i].sum;
        }
        *additions += n / 2;
        *rounds += 1;
        if (show_rounds) {
            printf("tree, round %d:", *rounds);
            for (int i = 0; i < n / 2; i++) {
                printf(" %ld", level[i]);
            }
            printf("\n");
        }
    }
    return level[0];
}

static double tree_doubles(double *level) {
    for (int n = WORKERS; n > 1; n /= 2) {
        struct double_job jobs[WORKERS];
        for (int i = 0; i < n / 2; i++) {
            jobs[i] = (struct double_job){level + 2 * i, 2, 0};
        }
        run_all(add_doubles, jobs, sizeof jobs[0], n / 2);
        for (int i = 0; i < n / 2; i++) {
            level[i] = jobs[i].sum;
        }
    }
    return level[0];
}

int main(void) {
    printf("%d values, %d to each of %d workers\n", COUNT, COUNT / WORKERS, WORKERS);
    long partials[WORKERS];
    partial_longs(VALUES, partials);
    printf("partial sums:");
    for (int w = 0; w < WORKERS; w++) {
        printf(" %ld", partials[w]);
    }
    printf("\n");

    long total = partials[0];
    for (int w = 1; w < WORKERS; w++) {
        total += partials[w];
    }
    printf("serial combine: %ld, after %d additions in %d rounds\n", total, WORKERS - 1, WORKERS - 1);
    int additions, rounds;
    total = tree_longs(partials, &additions, &rounds, 1);
    printf("tree combine: %ld, after %d additions in %d rounds\n", total, additions, rounds);

    double floats[COUNT];
    for (int i = 0; i < COUNT; i++) {
        floats[i] = (double)VALUES[i] + 0.2;
    }
    printf("\nthe same %d values plus 0.2 each, as double (on paper, 99.8)\n", COUNT);
    double loop_total = 0.0;
    for (int i = 0; i < COUNT; i++) {
        loop_total += floats[i];
    }
    printf("one loop over all %d: %.17g\n", COUNT, loop_total);
    double float_partials[WORKERS];
    partial_doubles(floats, float_partials);
    double serial_total = float_partials[0];
    for (int w = 1; w < WORKERS; w++) {
        serial_total += float_partials[w];
    }
    printf("partial sums, then serial: %.17g\n", serial_total);
    printf("partial sums, then tree: %.17g\n", tree_doubles(float_partials));
    return 0;
}
