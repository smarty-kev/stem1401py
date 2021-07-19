"""
Work out assuming 3
renaming files in a batch in a certain specified directory
"""

# instruction of program
print("This program allows you to rename multiple files in a specific directory.")

# import the os module -> used in this case to rename files with os.rename()
import os

# user interface to specify chosen directory
print("Please enter the full path of directory:")
specified_directory = input()

# all files in specified directory
all_in_directory = os.listdir(specified_directory)
all_f_in_directory = list()
for f in all_in_directory:
    if not os.path.isdir(f):
        all_f_in_directory.append(f)

num_files_directory = len(all_f_in_directory)
if len(all_f_in_directory) == 0:
    num_files_directory = "no"  # if there are no files in specified directory

# echo the number of file in specified directory
print(f"There are {num_files_directory} files in specified directory.")

# full path of files
full_path_f_list = list()
for f in all_f_in_directory:
    full_path_f_list.append(specified_directory+os.sep+f)


# main program
new_names = list()

print('Anything other than "y" will be considered as no')
for f in all_f_in_directory:
    print(f"Do you wish to rename file {f} ,y/no:")
    y_or_n = input()
    new_name = f
    if y_or_n == "y":
        new_name = input("What do you wish to rename file to, including the desired extension: ")
    new_names.append(new_name)

for f in full_path_f_list:
    n = new_names[full_path_f_list.index(f)]
    os.rename(f, n)

print("All files successfully renamed. :)")
