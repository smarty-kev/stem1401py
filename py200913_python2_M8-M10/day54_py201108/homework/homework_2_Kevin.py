"""
2. Calculate the size of a directory
"""

import os

sep = os.sep

sizes = []

def alldir(dirname):
    listdir = os.listdir(dirname)
    for name in listdir:
        if os.path.isdir(dirname+sep+name):
            alldir(dirname+sep+name)
        else:
            sizes.append(os.path.getsize(dirname))


# start path
start_path = input("Please enter the full path of the directory: ")
alldir(start_path)

total_size = 0

for size in sizes:
    total_size += size

print(f'The total size of directory "{start_path}" is {total_size} bytes.')
