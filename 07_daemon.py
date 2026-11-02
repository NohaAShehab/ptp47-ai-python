"""A daemon thread does not keep the program alive. Then try daemon=False: the program never ends
(stop it with Ctrl+C).   Run:  python3.14 07_daemon.py"""
import threading, time

def heartbeat():
    while True:                  # never ends
        print("beat")
        time.sleep(0.3)

t = threading.Thread(target=heartbeat, daemon=True)
t.start()
time.sleep(1)
print("main: exiting")
print(threading.active_count())
print("----Test, test  ....")
print(4+5)


