"""Inheritance from Day 5 in a real library. Then try: remove super().__init__(...)
-> RuntimeError: thread.__init__() not called.   Run:  python3.14 06_thread_subclass.py"""
import threading, time

class Downloader(threading.Thread):
    def __init__(self, url):
        super().__init__(name=f"dl-{url}")
        self.url = url
        self.size = None

    def run(self):               # start() calls run() in the new thread
        time.sleep(0.1)
        self.size = len(self.url) * 100

d = Downloader("iti.gov.eg")
d.start()
d.join()
print(d.name, d.size)                                      # dl-iti.gov.eg 1000
