import ctypes as c
import time


def keep_awake():
    while True:
        c.windll.kernel32.SetThreadExecutionState(0x80000002)
        time.sleep(10)
