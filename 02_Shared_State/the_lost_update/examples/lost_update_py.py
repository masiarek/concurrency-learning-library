"""The lost update, forced. `total += 1` is three steps -- load, add, store --
and nothing stops ten threads from all loading the same old total. A Barrier
holds every thread between its load and its store, so every load happens before
any store, on every run.

    python3 lost_update_py.py
"""

import threading

HANDLERS = 10

total = 0
all_loaded = threading.Barrier(HANDLERS)
loaded = [None] * HANDLERS


def handle(slot: int) -> None:
    global total
    seen = total  # 1. load
    loaded[slot] = seen
    all_loaded.wait()  # every handler has loaded
    total = seen + 1  # 2. add, 3. store


threads = [threading.Thread(target=handle, args=(i,)) for i in range(HANDLERS)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"{HANDLERS} handlers each added 1 to a total that started at 0")
print("the totals they loaded:", loaded)
print(f"the total is {total}, not {HANDLERS}")
