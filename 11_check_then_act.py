"""Both threads pass the check before either acts. Every run ends at -60.
Run:  python3.14 11_check_then_act.py"""
import threading, time

balance = 100
paid = []

def withdraw(amount):
    global balance
    if balance >= amount:        # 1. check
        time.sleep(0.01)         #    talk to the bank
        balance -= amount        # 2. act
        paid.append(amount)

ts = [threading.Thread(target=withdraw, args=(80,)) for _ in range(2)]
for t in ts: t.start()
for t in ts: t.join()
print("paid out:", paid)         # [80, 80]
print("balance:", balance)       # -60
