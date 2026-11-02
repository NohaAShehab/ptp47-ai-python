"""Ten threads print at the same instant: lines can mix. logging writes whole lines and names the thread.
Run it a few times:  python3.14 08_print_vs_logging.py"""
import threading, logging

def shout(i):
    print("hello from thread", i)

ts = [threading.Thread(target=shout, args=(i,)) for i in range(10)]
for t in ts: t.start()
for t in ts: t.join()

print("--- with logging ---")
logging.basicConfig(level=logging.INFO, format="%(threadName)-10s %(message)s")

def tell(i):
    logging.info("hello from thread %d", i)

ts = [threading.Thread(target=tell, args=(i,), name=f"worker-{i}") for i in range(4)]
for t in ts: t.start()
for t in ts: t.join()
