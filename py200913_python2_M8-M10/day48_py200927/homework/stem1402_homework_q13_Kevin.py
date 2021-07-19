"""
13. Write a Python program to copy the contents of a file to another file.
"""

chosen_file = input("Please enter the file name you want to copy from (if leaved blank, will copy from text_hmw_Kevin.txt) : ")

if chosen_file == "":
    chosen_file = "text_hmw_Kevin.txt"

file = open(chosen_file, "r")

content = file.readlines()

file.close()

chosen_file = input("Please enter the file name you want to copy to (if leaved blank, will create a new file) : ")

if chosen_file == "":
    chosen_file = "new_file.txt"

new_file = open(chosen_file, "w")

new_file.writelines(content)

new_file.close()
