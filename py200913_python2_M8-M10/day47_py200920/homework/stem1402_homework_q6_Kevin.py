"""
6. Write a Python program to read a file line by line store it into a variable.
"""

try:
    f = open("text_Kevin.txt", "r")

    content = f.readlines()
    print(content, type(content))
except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)

finally:
    f.close()
