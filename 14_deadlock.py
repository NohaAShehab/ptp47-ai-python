"""Two threads take two locks in opposite orders: deadlock. (Daemon + timeout so the demo can report it.)
Run:  python3.14 14_deadlock.py          -> deadlock: True
      python3.14 14_deadlock.py fixed    -> both finish"""
import sys, threading, time

FIXED = "fixed" in sys.argv
lock_a, lock_b = threading.Lock(), threading.Lock()

def transfer(first, second, name):
    with first:
        time.sleep(0.1)
        with second:             # waits for the other thread
            print(name, "done")

t1 = threading.Thread(target=transfer, daemon=True, args=(lock_a, lock_b, "A->B"))
t2 = threading.Thread(target=transfer, daemon=True,
                      args=(lock_a, lock_b, "B->A") if FIXED else (lock_b, lock_a, "B->A"))
t1.start(); t2.start()
t1.join(timeout=1); t2.join(timeout=1)
print("deadlock:", t1.is_alive() and t2.is_alive())
