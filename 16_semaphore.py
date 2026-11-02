"""Semaphore(2): the downloads finish in waves of two.  Change 2 to 3 and run again.
Run:  python3.14 16_semaphore.py"""
import threading, time

slots = threading.Semaphore(2)     # at most 2 at once
finished = []

def download():
    with slots:                    # take a slot, or wait for one
        time.sleep(0.2)
        finished.append(round(time.perf_counter() - start, 1))

start = time.perf_counter()
ts = [threading.Thread(target=download) for _ in range(6)]
for t in ts: t.start()
for t in ts: t.join()
print("finish times:", sorted(finished))    # [0.2, 0.2, 0.4, 0.4, 0.6, 0.6]
