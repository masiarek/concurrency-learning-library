"""When does the order of arrival change a sum? Every check here tries every
order in which the same requests could reach a server that adds them up, one
at a time, on one thread -- so no update can be lost -- and counts the distinct
totals those orders produce.

    python3 order_py.py
"""

import math
from itertools import permutations


def totals(values, apply, start=0):
    """Every distinct final total, over every order of `values`."""
    results = set()
    for order in permutations(values):
        total = start
        for v in order:
            total = apply(total, v)
        results.add(total)
    return sorted(results)


def report(title, values, results):
    orders = len(list(permutations(values)))
    print(f"{title}: {orders} orders -> {len(results)} distinct total(s): {results}")


def add(total, v):
    return total + v


ints = [5, 10, 20, 40, 80]
report("integers 5, 10, 20, 40, 80", ints, totals(ints, add))

floats = [0.1, 0.2, 0.3]
report("floats 0.1, 0.2, 0.3", floats, totals(floats, add, start=0.0))
print(f"  (0.1 + 0.2) + 0.3 = {(0.1 + 0.2) + 0.3!r}")
print(f"  0.1 + (0.2 + 0.3) = {0.1 + (0.2 + 0.3)!r}")
report("the same floats, summed with math.fsum", floats,
       sorted({math.fsum(order) for order in permutations(floats)}))


def withdraw_only_if_covered(balance, v):
    """A negative request is a withdrawal, refused if it would overdraw."""
    return balance + v if balance + v >= 0 else balance


money = [50, -30, -40]
report("a balance that refuses to go below 0, requests +50, -30, -40", money,
       totals(money, withdraw_only_if_covered))

print()
print("one request, +5, delivered twice because the client retried after a lost reply:")
deliveries = [("req-1", 5), ("req-2", 10), ("req-1", 5)]

total = 0
for _, amount in deliveries:
    total += amount
print(f"  adding every delivery: {total}")

total, seen = 0, set()
for request_id, amount in deliveries:
    if request_id in seen:
        continue  # a retry of a request already applied
    seen.add(request_id)
    total += amount
print(f"  adding each request id once: {total}")
