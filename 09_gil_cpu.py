"""Run it twice, on both interpreters:
    python3.14  09_gil_cpu.py     -> 2 threads take as long as sequential
    python3.14t 09_gil_cpu.py     -> 2 threads take about half (free-threaded, no GIL)"""
import threading, time, sys

def count(n):
    while n > 0:
        n -= 1                   # pure Python, pure CPU

N = 20_000_000
start = time.perf_counter()
count(N); count(N)
print(f"sequential: {time.perf_counter() - start:.1f} s")

start = time.perf_counter()
ts = [threading.Thread(target=count, args=(N,)) for _ in range(2)]
for t in ts: t.start()
for t in ts: t.join()
print(f"2 threads:  {time.perf_counter() - start:.1f} s")
print("GIL enabled:", sys._is_gil_enabled())
