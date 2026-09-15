"""Who waits when main returns? In Python, the interpreter does: it will not exit
while a thread that is not a daemon is still running. A daemon thread is ended.

    python3 who_waits_py.py
"""

import threading
import time


def worker(label: str, seconds: int) -> None:
    time.sleep(seconds)
    print(f"{label}  finished", flush=True)


ordinary = threading.Thread(target=worker, args=("ordinary thread:", 1))
daemon = threading.Thread(target=worker, args=("daemon thread:  ", 3), daemon=True)
ordinary.start()
daemon.start()

print("main:             end of the script", flush=True)
