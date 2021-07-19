"""
Check if path exists
"""

import os

# directory
path = os.getcwd()
os.path.exists(path)

# file
path = ".."+os.getcwd()
os.path.exists(path)

path = "xxxx.xxx"
if os.path.exists(path):
    print("Already Exists")
else:
    file = open(path, "x")
    file.close()
