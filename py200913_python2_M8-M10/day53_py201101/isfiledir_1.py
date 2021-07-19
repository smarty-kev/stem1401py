"""
Test if a path is a file or dir
"""

import os

path = "filesize_1.py"
if os.path.isdir(path):
    print(f"{path} is a directory")
else:
    print(f"{path} is a normal file")

