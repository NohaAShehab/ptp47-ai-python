"""as_completed gives futures in finishing order; fut.result() re-raises the task's exception.
Run:  python3.14 19_pool_submit.py"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def download(name, seconds):
    time.sleep(seconds)
    if name.endswith(".exe"):
        raise ValueError(f"refusing {name}")
    return f"{name}: {int(seconds * 1000)} KB"

files = {"a.csv": 1.0, "b.csv": 0.6, "virus.exe": 0.2, "c.csv": 0.8}
with ThreadPoolExecutor(max_workers=4) as pool:
    futures = {pool.submit(download, f, s): f for f, s in files.items()}
    for fut in as_completed(futures):     # in finishing order
        try:
            print(fut.result())
        except ValueError as e:
            print("failed:", e)
