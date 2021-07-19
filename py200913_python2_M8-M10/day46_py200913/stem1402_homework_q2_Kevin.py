"""
2. Write a Python program to read the first n lines of a file.
"""


try:
    lines = int(input("Enter how many lines you want to read: "))

    f = open("text_q1_Kevin.txt", 'r')
    for l in range(lines):
        print(f.readline())
except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)
finally:
    f.close()
