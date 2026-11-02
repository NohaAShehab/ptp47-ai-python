"""deposit_twice holds the lock and calls deposit, which asks for it again.
A Lock waits for itself forever; an RLock lets its owner in. (Daemon + timeout so the demo ends.)
Run:  python3.14 13_rlock.py"""
import threading

class Account:
    def __init__(self, lock):
        self.balance = 0
        self.lock = lock
    def deposit(self, x):
        with self.lock:
            self.balance += x
    def deposit_twice(self, x):
        with self.lock:          # holds the lock...
            self.deposit(x)      # ...and asks for it again
            self.deposit(x)

for name, lock in (("Lock", threading.Lock()), ("RLock", threading.RLock())):
    a = Account(lock)
    t = threading.Thread(target=a.deposit_twice, args=(10,), daemon=True)
    t.start(); t.join(timeout=1)
    print(name, "stuck:", t.is_alive(), "balance:", a.balance)
