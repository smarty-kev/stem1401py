"""
Do research on how to update the content of a specified line

I found a solution from someone on https://exceptionshub.com/editing-specific-line-in-text-file-in-python.html
"""

# for exception handling
import io

# default file (if user leaves blank
default_file = "test_txt_file_Kevin.txt"

# user inputs the file they want to update, if leaved blank, will default to file "test_txt_file_Kevin"
print(f"Please enter name of the file you want to edit, if leaved blank, will default to file {default_file}:")  # prompt
file_to_update = input()

# if leaved blank, will default to file "test_txt_file_Kevin"
if file_to_update == "":
    file_to_update = default_file
    print("There are 10 lines in the default_file")

# line to update
print("Please enter the line (int) you want to update in the file: ")
while True:
    specific_line = input()
    if specific_line.isdecimal():
        specific_line = int(specific_line)
        break

# main program
try:
    file = open(f"{file_to_update}", "r")  # initial file
    content = file.readlines()  # content of initial file
    print(f'{content[specific_line-1]}This is the content of selected line')  # echo the selected line
    print("What would you like to change this line with?")
    new_content = input() + "\n"  # user inputs what they want to change the specified line with
    content[specific_line-1] = new_content  # changing specified line
    file.close()
    new_file = open(f"{file_to_update}", "w")  # reopening the file in "write" mode
    new_file.writelines(content)  # updating the file
    new_file.close()
    print("Successfully Changed!")
except IOError as io:
    print(io)
except Exception as e:
    print(e)

