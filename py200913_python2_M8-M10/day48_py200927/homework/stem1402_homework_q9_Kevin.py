"""
9. Write a Python program to count the number of lines in a text file.
"""

file = open("text_hmw_Kevin.txt", "r")

line_count = 0

for line in file.readlines()[:]:
    line_count += 1

print(f"there are {line_count} lines in the file text_hmw_Kevin.txt")

file.close()
