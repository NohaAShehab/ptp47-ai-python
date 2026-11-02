"""Run with both:  python3.14 23_which_python.py   and   python3.14t 23_which_python.py"""
import sys, sysconfig

ft = sysconfig.get_config_var("Py_GIL_DISABLED")
print(sys.version.split()[0])
print("free-threaded build:", bool(ft))
print("GIL enabled now:", sys._is_gil_enabled())
