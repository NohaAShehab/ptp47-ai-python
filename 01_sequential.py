"""Three downloads, one at a time: the total is the SUM of the waits.
Run:  python3.14 01_sequential.py"""
import time

def download(name, seconds):
    print("start", name)
    time.sleep(seconds)          # waiting for the network
    print("done ", name)

# seconds each download takes
files = {"a.csv": 1.0, "b.csv": 0.6, "c.csv": 0.8}
start = time.perf_counter()
print(start)
for name, seconds in files.items():
    download(name, seconds)
print(f"total: {time.perf_counter() - start:.1f} s")      # 2.4 s
