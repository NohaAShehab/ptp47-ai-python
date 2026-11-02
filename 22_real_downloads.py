"""Real network I/O (needs internet). Downloads the same pages one by one, then with a pool.
Run:  python3.14 22_real_downloads.py"""
import time, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

URLS = ["https://www.python.org", "https://docs.python.org/3/", "https://pypi.org",
        "https://peps.python.org", "https://www.wikipedia.org", "https://github.com"]

def fetch(url):
    with urllib.request.urlopen(url, timeout=10) as r:
        return len(r.read())

def sequential():
    for u in URLS:
        try:
            fetch(u)
        except OSError:
            pass

start = time.perf_counter()
sequential()
print(f"one at a time: {time.perf_counter() - start:.1f} s")

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=len(URLS)) as pool:
    futures = {pool.submit(fetch, u): u for u in URLS}
    for fut in as_completed(futures):
        try:
            print(f"{fut.result():>9,} bytes  {futures[fut]}")
        except OSError as e:
            print(f"   failed        {futures[fut]}  ({type(e).__name__})")
print(f"thread pool:   {time.perf_counter() - start:.1f} s")
