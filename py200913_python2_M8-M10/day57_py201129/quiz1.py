"""
Quiz
Write a program to rename multiple files in a specific directory
date : 2020-11-29
author : Kevin Liu
"""

import os


# instruction of program
print("This program allows you to change rename multiple files in a specific directory.")


#
specified_directory = input("Please enter the full path of the desired directory: ")


# rename file function
def rename_file(file, new_name):
    os.rename(file, new_name)


# all files in specified directory
all_files_directory = list()
dir_list = os.listdir(specified_directory)
print("These are the following files in the specified directory =")
for f in dir_list:
    print(f)

# counter
file_num = 0


# main program
while True:
    if not os.path.isdir(specified_directory+os.sep+dir_list[file_num]):
        print(f"Do you wish to change the name of file {dir_list[file_num]}, y/n")
        change = input()
        if change == "y":
            new_file_name = input("Please enter the new file name, with the extension desired: ")
            rename_file(specified_directory+os.sep+dir_list[file_num], new_file_name)
    file_num += 1
    if file_num == len(dir_list):
        break
