"""Splitting a sum across workers. Each thread adds its own run of values into a
variable no other thread can see, and the partial sums are then combined two
ways: one after another, and as a tree whose rounds add pairs at the same time.
Then the same split, with floats.

With the global interpreter lock, these threads take turns rather than running
at once; the grouping of the additions, which is what this program prints, is
the same either way.

    python3 split_sum_py.py
"""

import math
import threading

WORKERS = 8  # a power of two, so every round of the tree pairs everyone up
VALUES = [1, 4, 3, 9, 2, 8, 5, 1, 1, 6, 2, 7, 2, 5, 0, 4, 1, 8, 6, 5, 1, 2, 3, 9]


def run_all(n, job):
    """Run job(0) ... job(n - 1), each on its own thread, and wait for all of them."""
    threads = [threading.Thread(target=job, args=(i,)) for i in range(n)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def partial_sums(values, workers):
    """Each worker adds its own run, left to right, into its own my_sum, and
    stores the result in its own slot of sums."""
    width = len(values) // workers
    sums = [None] * workers

    def worker(w):
        run = values[w * width : (w + 1) * width]
        my_sum = run[0]
        for x in run[1:]:
            my_sum += x
        sums[w] = my_sum

    run_all(workers, worker)
    return sums


def serial_combine(sums):
    """The master adds every partial sum into its own, one at a time."""
    total = sums[0]
    for s in sums[1:]:
        total += s
    return total, len(sums) - 1


def tree_combine(sums, show_rounds):
    """Each round adds neighbouring pairs, every pair on its own thread, until
    one value is left. Returns the total, the additions and the rounds."""
    level, additions, rounds = sums, 0, 0
    while len(level) > 1:
        current, following = level, [None] * (len(level) // 2)

        def add_pair(i):
            following[i] = current[2 * i] + current[2 * i + 1]

        run_all(len(following), add_pair)
        additions += len(following)
        rounds += 1
        level = following
        if show_rounds:
            print(f"tree, round {rounds}:", *level)
    return level[0], additions, rounds


print(f"{len(VALUES)} values, {len(VALUES) // WORKERS} to each of {WORKERS} workers")
partials = partial_sums(VALUES, WORKERS)
print("partial sums:", *partials)
total, additions = serial_combine(partials)
print(f"serial combine: {total}, after {additions} additions in {additions} rounds")
total, additions, rounds = tree_combine(partials, show_rounds=True)
print(f"tree combine: {total}, after {additions} additions in {rounds} rounds")

floats = [v + 0.2 for v in VALUES]
print()
print(f"the same {len(floats)} values plus 0.2 each, as float (on paper, 99.8)")
loop_total = 0.0
for x in floats:
    loop_total += x
print(f"one loop over all {len(floats)}: {loop_total}")
float_partials = partial_sums(floats, WORKERS)
print("partial sums, then serial:", serial_combine(float_partials)[0])
print("partial sums, then tree:", tree_combine(float_partials, show_rounds=False)[0])
print("sum():", sum(floats))
print("math.fsum():", math.fsum(floats))
