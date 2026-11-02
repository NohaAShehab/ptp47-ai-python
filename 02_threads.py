"""The same downloads in threads: the total is the SLOWEST wait, not the sum.
Ask first: which file finishes first?  Run:  python3.14 02_threads.py"""
import threading, time

def download(name, seconds):
    time.sleep(seconds)
    print("done ", name)

files = {"a.csv": 1.0, "b.csv": 0.6, "c.csv": 0.8}
start = time.perf_counter()
threads = []
for name, secs in files.items():
    t = threading.Thread(target=download, args=(name, secs))
    t.start()                    # runs download() in a new thread
    print("start", name)
    threads.append(t)
for t in threads:
    t.join()                     # wait until t has finished
print(f"total: {time.perf_counter() - start:.1f} s")      # 1.0 s, b then c then a
