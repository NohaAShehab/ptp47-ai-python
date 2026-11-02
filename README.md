# Day 06 lecture demos: threads and concurrency

One script per demo in the Day 06 deck, in slide order. Each script starts with a docstring that says what to show and how to run it.

## Setup

The demos are written for **Python 3.14**. Two of them compare it with the **free-threaded build, python3.14t** (no GIL):

- python.org installer (Windows, macOS): tick *Download free-threaded binaries* in the custom install options.
- uv: `uv python install 3.14 3.14t`
- Check what you are running: `python3.14 23_which_python.py` and `python3.14t 23_which_python.py`

Run from this folder, for example `python3.14 02_threads.py`. Nothing else needs installing.

## The demos

| Script | Slide | What it shows |
| --- | --- | --- |
| `00_uv_walkthrough.md` | Part one: packages | Commands to type live: pip, venv, uv, .env |
| `00_env_vars.py` | Reading environment variables in Python | os.environ, defaults, required keys (with `.env.example`) |
| `01_sequential.py` | The cost of waiting | Three downloads, one at a time |
| `02_threads.py` | Three downloads, three threads, one second | The same downloads in threads |
| `03_join.py` | join(): wait for a thread to finish | With and without join() |
| `04_thread_info.py` | Who am I? Naming and inspecting threads | Names, current_thread() and active_count() |
| `05_results.py` | Getting results back from a thread | A thread's return value is lost |
| `06_thread_subclass.py` | Day 5 again: a Thread subclass | Subclass Thread and override run() |
| `07_daemon.py` | Daemon threads: background helpers | A daemon heartbeat |
| `08_print_vs_logging.py` | Clean code for threaded programs | print() can mix lines; logging does not |
| `09_gil_cpu.py` | CPU work: two threads, no faster | Threads do not speed up pure-Python math (with the GIL) |
| `10_gil_hides_race.py` | The GIL is not a lock for your data | balance += 1 in four threads |
| `11_check_then_act.py` | Check, then act: the classic race | Two cash machines, one account |
| `12_lock_fix.py` | A Lock makes check-and-act one step | The same account with a Lock |
| `13_rlock.py` | RLock: a lock you may take twice | A method that waits for itself |
| `14_deadlock.py` | Deadlock: each holds what the other needs | Opposite lock order freezes; same order works |
| `15_event.py` | Event: one thread signals, many wake up | Ready, set, go |
| `16_semaphore.py` | Semaphore: at most N threads at a time | Six downloads, two at a time |
| `17_queue_workers.py` | Queue: hand work from one thread to another | Producer, queue, three workers |
| `18_pool_map.py` | pool.map: the threaded version of map() | ThreadPoolExecutor.map |
| `19_pool_submit.py` | submit() and as_completed() | Results as they finish, failures included |
| `20_thread_exceptions.py` | Where do a thread's exceptions go? | Plain Thread vs pool |
| `21_processes.py` | Same API, real parallelism: processes | ThreadPoolExecutor vs ProcessPoolExecutor |
| `22_real_downloads.py` | Looking ahead | Real web pages: sequential vs a thread pool |
| `23_which_python.py` | Python without the GIL | Which interpreter am I running? |

## Tips for the lecture

- Ask the class to **predict** before you run: the order of the done lines in `02`, the total in `10` with and without the GIL, the balance in `11`.
- Run `10_gil_hides_race.py` three times on each interpreter: the GIL run is always right, the free-threaded run changes every time.
- `13_rlock.py` and `14_deadlock.py` use daemon threads with a join timeout, so they report the problem instead of freezing the terminal.
- `21_processes.py` must run as a script: process pools import the main module.
- `22_real_downloads.py` needs internet; if the room has none, the time.sleep demos show the same idea.
- Timings were measured on a 2-core machine. Your numbers will differ; the pattern will not.
