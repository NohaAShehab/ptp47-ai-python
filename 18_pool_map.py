"""Results come back, in input order. Half the code of 02_threads.py.  Run:  python3.14 18_pool_map.py"""
from concurrent.futures import ThreadPoolExecutor
import time

def download(name, seconds):
    time.sleep(seconds)
    return f"{name}: {int(seconds * 1000)} KB"

files = {"a.csv": 1.0, "b.csv": 0.6, "c.csv": 0.8}
start = time.perf_counter()
with ThreadPoolExecutor(max_workers=3) as pool:
    for line in pool.map(download, files, files.values()):
        print(line)
print(f"total: {time.perf_counter() - start:.1f} s")
