"""
get file size
"""

import os

filename = "/Users/jenn/PycharmProjects/stem1401py/py200913_python2_M8-M10/day51_py201018/filedir_2_mkdir.py"
result = os.path.getsize(filename)

print(result, type(result))
