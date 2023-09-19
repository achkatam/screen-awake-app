import ctypes as c
import time


def keep_awake():
    counter = 1

    while counter == 10:
        c.windll.kernel32.SetThreadExecutionState(0x80000002)
        time.sleep(600)  # 10 seconds
        counter += 1
