# import threading, time
#
# class Downloader(threading.Thread):
#     def __init__(self, url):
#         super().__init__(name=f"dl-{url}")
#         self.url = url
#         self.size = None
#         print('Thread started')
#
#     def run(self):               # start() calls run() in the new thread
#         time.sleep(0.1)
#         self.size = len(self.url) * 100
#         print(f"--- is running  {self.url} ---")
#
# d = Downloader("ai-47")
# d.start()  # main and the d --> once finished
# print("---- hererrrrr")
# print(threading.active_count(), "downloader")
#
# print(d.name, d.size)
# ################################ dl-iti.gov.eg 1000
#                        # None: the 16 is lost
#
# def square_into(n, results, i):
#     time.sleep(0.1)
#     results[i] = n * n           # each thread writes its own slot
#
# numbers = [3, 5, 7]
# results = [None] * len(numbers)
# threads = [threading.Thread(target=square_into, args=(n, results, i)) for i, n in enumerate(numbers)]
# for t in threads:
#     t.start()
#     print(t.name)
# print(threading.active_count(), "square_into")
# print(results)


###
import threading, time, sys

def count(n):
    while n > 0:
        n -= 1                   # pure Python, pure CPU

N = 20_000_000
start = time.perf_counter()
count(N)
count(N)
print(f"sequential: {time.perf_counter() - start:.1f} s")

##################
start = time.perf_counter()
ts = [threading.Thread(target=count, args=(N,)) for _ in range(2)]
for t in ts: t.start()
for t in ts: t.join()
print(f"2 threads:  {time.perf_counter() - start:.1f} s")
print("GIL enabled:", sys._is_gil_enabled())