"""Getting a result back. In Python, Thread.join() returns None and the target's
return value is thrown away. A Future from an executor carries the value back --
and re-raises the exception if the call raised one.

    python3 result_back_py.py
"""

import threading
from concurrent.futures import ThreadPoolExecutor


def sum_to_100() -> int:
    return sum(range(1, 101))


def no_total_today() -> int:
    raise ValueError("no total today")


thread = threading.Thread(target=sum_to_100)
thread.start()
print("Thread.join() returned", thread.join())

with ThreadPoolExecutor() as pool:
    future = pool.submit(sum_to_100)
    print("Future.result() returned", future.result())

    failing = pool.submit(no_total_today)
    try:
        failing.result()
    except ValueError as e:
        print(f"Future.result() re-raised {e!r}")
