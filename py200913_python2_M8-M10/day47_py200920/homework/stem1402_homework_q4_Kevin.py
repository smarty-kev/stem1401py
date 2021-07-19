"""
4. Write a Python program to read last n lines of a file.
"""

try:
    f = open("text_Kevin.txt", "r")

    last_n_lines = int(input("Last number of lines you want to read: "))

    for l in (f.readlines()[-last_n_lines:]):
        print(l)

except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)

finally:
    f.close()
