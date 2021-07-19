"""
list all subdirectories and files in a specific directory.

How to list all directories and files with subdirectories under specified directory?
"""

import os

sep = os.sep

def alldir(dirname, level=0):
    listdir = os.listdir(dirname)
    for name in listdir:
        print('    ' * level + name)
        if os.path.isdir(dirname+sep+name):
            level += 1
            alldir(dirname+sep+name, level)
            level -= 1


# start path
start_path = input("Please enter the full path of the directory: ")
alldir(start_path)

