"""
mkdir
"""

import os
import time


try:
    path = "mydir3"
    print(f"creating path {path}...")
    time.sleep(2)
    os.mkdir(path)

    print(f"{os.getcwd() + os.sep+path} is created.")
except OSError as oe:
    print(oe)
except RuntimeError as re:
    print(re)
except Exception as e:
    print(e)
