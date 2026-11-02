"""join() always returns None. Give each thread its own slot to write to.
Run:  python3.14 05_results.py"""
import threading, time

def square(n):
    return n * n

t = threading.Thread(target=square, args=(4,))
t.start()
print("join returned:", t.join())                         # None: the 16 is lost

def square_into(n, results, i):
    time.sleep(0.1)
    results[i] = n * n           # each thread writes its own slot

numbers = [3, 5, 7]
results = [None] * len(numbers)
threads = [threading.Thread(target=square_into, args=(n, results, i)) for i, n in enumerate(numbers)]
for t in threads: t.start()
for t in threads: t.join()
print(results)                                             # [9, 25, 49]
