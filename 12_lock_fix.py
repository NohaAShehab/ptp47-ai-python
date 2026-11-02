"""with lock: makes the check and the action one step.  Run:  python3.14 12_lock_fix.py"""
import threading, time

balance = 100
paid = []
lock = threading.Lock()

def withdraw(amount):
    global balance
    with lock:                   # one thread at a time
        if balance >= amount:
            time.sleep(0.01)
            balance -= amount
            paid.append(amount)

ts = [threading.Thread(target=withdraw, args=(80,)) for _ in range(2)]
for t in ts: t.start()
for t in ts: t.join()
print("paid out:", paid)         # [80]
print("balance:", balance)       # 20
