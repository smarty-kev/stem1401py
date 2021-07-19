"""
change directory

chdir()
"""

import os

# before
current_path = os.getcwd()
print(current_path)

# after
os.chdir(r"/Users/jenn/PycharmProjects/stem1401py/py200913_python2_M8-M10/day50_py201011/homework")
changed_path = os.getcwd()
print(changed_path)

# relative path
os.chdir(r"..//..//..")
changed_path = os.getcwd()
print(changed_path)
