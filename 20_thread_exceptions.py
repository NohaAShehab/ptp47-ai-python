"""A plain thread's exception is printed and lost; a future keeps it for you.
Run:  python3.14 20_thread_exceptions.py"""
import threading
from concurrent.futures import ThreadPoolExecutor

def task():
    raise ValueError("bad data")

t = threading.Thread(target=task)
t.start()
t.join()
print("main: carried on, and cannot catch it")

with ThreadPoolExecutor() as pool:
    fut = pool.submit(task)
try:
    fut.result()
except ValueError as e:
    print("main caught:", e)
