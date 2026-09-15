"""Keeping every update, two ways. Eight handlers each add the numbers 1 to
10,000 to one total: under a threading.Lock, and by putting every number on a
queue that one thread reads and adds up.

    python3 every_update_py.py
"""

import queue
import threading

HANDLERS = 8
LAST = 10_000


def run_handlers(handler) -> None:
    threads = [threading.Thread(target=handler) for _ in range(HANDLERS)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def with_a_lock() -> int:
    lock = threading.Lock()
    total = 0

    def handler() -> None:
        nonlocal total
        for n in range(1, LAST + 1):
            with lock:
                total += n  # load, add and store, all while holding the lock

    run_handlers(handler)
    return total


def with_one_owner() -> int:
    numbers: queue.Queue[int | None] = queue.Queue()
    result = []

    def owner() -> None:
        total = 0  # no other thread can reach this variable
        while (n := numbers.get()) is not None:
            total += n
        result.append(total)

    def handler() -> None:
        for n in range(1, LAST + 1):
            numbers.put(n)

    owning_thread = threading.Thread(target=owner)
    owning_thread.start()
    run_handlers(handler)
    numbers.put(None)  # every handler has finished: tell the owner to stop
    owning_thread.join()
    return result[0]


print(f"{HANDLERS} handlers each add 1 to {LAST}; the total should be {HANDLERS * LAST * (LAST + 1) // 2}")
print(f"with a threading.Lock: {with_a_lock()}")
print(f"with one owner:        {with_one_owner()}")
