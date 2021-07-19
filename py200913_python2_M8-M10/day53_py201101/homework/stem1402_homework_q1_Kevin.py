"""
move a file(s)
move a directory

____________________
move = copy + delete/remove
copy, cp
remove()
"""

import shutil
import sys
import os


# file or directory
file_or_directory = input("Do you want to move a file or a directory (f/d)? :")


# move a file
def move_file():
    source = input("Enter the source file with full path: ")
    target = input("Enter the target file with full path: ")

    # adding exception handling
    try:
        shutil.copyfile(source, target)
    except IOError as e:
        print("Unable to copy file. %s" % e)
        exit(1)
    except:
        print("Unexpected Error: ", sys.exc_info())
        exit(1)

    # delete original file
    os.remove(source)
    print("\nFile Copy Done!\n")


# move a directory
def move_dir():
    source = input("Enter the source directory with full path: ")
    target = input("Enter the target directory with full path: ")

    try:
        shutil.copytree(source, target)
    except IOError as e:
        print("Unable to copy file. %s" % e)
        exit(1)
    except:
        print("Unexpected Error: ", sys.exc_info())
        exit(1)

    # delete original dir
    shutil.rmtree(source)
    print("\nFile Copy Done!\n")

while True:
    if file_or_directory == 'f':
        move_file()
        break
    elif file_or_directory == 'd':
        move_dir()
        break
    else:
        file_or_directory = input("Do you want to move a file or a directory (f/d)? : ")
