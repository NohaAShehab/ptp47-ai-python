"""One word changes. Processes each have their own GIL, so CPU work runs on several cores.
Run as a script (process pools need an importable module):  python3.14 21_processes.py"""
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def count(n):
    while n > 0:
        n -= 1

if __name__ == "__main__":       # required for processes
    for Pool in (ThreadPoolExecutor, ProcessPoolExecutor):
        start = time.perf_counter()
        with Pool(max_workers=2) as pool:
            list(pool.map(count, [40_000_000] * 2))
        print(f"{Pool.__name__:20} {time.perf_counter() - start:.1f} s")
