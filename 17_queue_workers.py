"""Producer-consumer: no shared variable, no lock to write. None tells a worker to stop.
Run:  python3.14 17_queue_workers.py"""
import threading, queue, time

jobs = queue.Queue()
results = queue.Queue()

def worker():
    while True:
        n = jobs.get()             # waits for an item
        if n is None:              # sentinel: stop
            break
        time.sleep(0.1)            # do the work
        results.put((n, n * n, threading.current_thread().name))

workers = [threading.Thread(target=worker, name=f"worker-{i}") for i in range(3)]
for w in workers: w.start()
for n in range(1, 7):              # the producer
    jobs.put(n)
for _ in workers:
    jobs.put(None)                 # one stop signal each
for w in workers: w.join()
for n, sq, who in sorted(results.queue):
    print(f"{n} -> {sq:2}  by {who}")
