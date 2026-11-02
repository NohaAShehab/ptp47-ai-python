"""Every program starts with MainThread. Name your threads: logs become readable.
Run:  python3.14 04_thread_info.py"""
import threading, time

def task():
    me = threading.current_thread()
    print(f"{me.name} running")
    time.sleep(0.2)
    print(f"Done {me.name} ")

print(threading.current_thread().name)
workers = [threading.Thread(target=task, name=f"worker-{i}") for i in range(3)]
print(workers)
for w in workers:
    w.start()
    time.sleep(0.01)
print("alive:", threading.active_count())                 # 4: main + 3 workers
for w in workers:
    w.join()
print("alive:", threading.active_count(), workers[0].is_alive())
