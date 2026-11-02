"""Without join() the main thread reports 'done' too early.
Run:  python3.14 03_join.py         then change USE_JOIN to True and run again."""
import threading, time

USE_JOIN = False

def work():
    time.sleep(0.5)
    print("worker: finished")

t = threading.Thread(target=work)
t.start()
if USE_JOIN:
    t.join()
print("main: all done?")
