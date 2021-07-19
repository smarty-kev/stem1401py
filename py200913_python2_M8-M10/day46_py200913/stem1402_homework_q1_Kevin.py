"""
1. Write a Python program to read an entire text file.
"""

try:
    f = open("text_q1_Kevin.txt", "r")
    content = f.read()
    print(content)
except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)
finally:
    f.close()
