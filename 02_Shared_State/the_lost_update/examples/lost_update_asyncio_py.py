"""The lost update with no second thread. An asyncio program runs every handler
on one thread, and a handler is never interrupted between two lines -- only at
an `await`. So a handler that loads, adds and stores with no `await` in between
keeps every update, and one that awaits between its load and its store loses
them, exactly as the threads did.

`asyncio.sleep(0)` waits for no time at all. It is the plainest possible
`await`, and it stands in for the database call or the log write that sits
between a load and a store in a real handler.

    python3 lost_update_asyncio_py.py
"""

import asyncio

HANDLERS = 10

total = 0


async def add_without_await() -> None:
    global total
    seen = total  # 1. load
    total = seen + 1  # 2. add, 3. store


async def add_with_await_between() -> None:
    global total
    seen = total  # 1. load
    await asyncio.sleep(0)  # the event loop runs the other handlers here
    total = seen + 1  # 2. add, 3. store


async def main() -> None:
    global total
    for handler in (add_without_await, add_with_await_between):
        total = 0
        await asyncio.gather(*(handler() for _ in range(HANDLERS)))
        print(f"{HANDLERS} handlers, {handler.__name__}: the total is {total}")


asyncio.run(main())
