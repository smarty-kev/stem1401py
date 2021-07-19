"""
directory and file management


"""


# get current directory
# MS_DOS/Power Shell        C:\>
# Linux/Mac OS              # pwd
#                           $ pwd


# MS-DOS                    dir
# Linux/Mac OS              ls


# get current directory

import os

result = os.getcwd()
print(result, type(result))

"""
/Users/jenn/PycharmProjects/stem1401py/py200913_python2_M8-M10/day50_py201011 <class 'str'>
"""


result1 = os.getcwdb()
print(result1, type(result1))

"""
b'/Users/jenn/PycharmProjects/stem1401py/py200913_python2_M8-M10/day50_py201011' <class 'bytes'>
"""
