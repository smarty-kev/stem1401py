"""
python module

modules refers to a file containing Python statements and definitions

module name is the python file name

conventions:
not start with a number
not start with an underscore
"""

# to create a module in python: just create a python file


import py200727_python2.day33_py200824.myfunc as myfunc
import py200727_python2.day33_py200824.myconst as myconst


result = myfunc.add(1, 2)
print(result)

result = myfunc.sub(1, 2)
print(result)

result = myconst.G
print(result)
