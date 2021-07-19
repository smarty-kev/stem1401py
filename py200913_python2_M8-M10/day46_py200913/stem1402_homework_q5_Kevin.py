"""
5. Write a Python program to read a file line by line and store it into a list.
"""

try:
    f = open("text_q1_Kevin.txt", 'r')

    content = f.readlines()
    print(content)
except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)
finally:
    f.close()