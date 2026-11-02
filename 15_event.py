"""Runners block on go.wait() until the main thread calls go.set().  Run:  python3.14 15_event.py"""
import threading, time

go = threading.Event()             # starts "not set"

def runner(name, delay):
    print(name, "ready")
    go.wait()                      # block until set()
    time.sleep(delay)
    print(name, "running")

for i, name in enumerate(["A", "B", "C"]):
    threading.Thread(target=runner, args=(name, 0.1 * (i + 1))).start()
    time.sleep(0.05)
print("main: ready, set...")
time.sleep(0.5)
print("main: go!")
go.set()                           # wakes every waiting thread
