"""A bug the GIL hides. Run on both interpreters, three times each:
    python3.14  10_gil_hides_race.py    -> 4000000 (luck: the interpreter happens not to switch mid-statement)
    python3.14t 10_gil_hides_race.py    -> a different, smaller number every run"""
import threading

balance = 0

def deposit(times):
    global balance
    for _ in range(times):
        balance += 1             # read, add, write

ts = [threading.Thread(target=deposit, args=(1_000_000,)) for _ in range(4)]
for t in ts: t.start()
for t in ts: t.join()
print(balance)                   # expected 4000000
