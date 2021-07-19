"""
file mode 'r+'
"""

f = None
try:
    f = open("file_9_mode_plus.txt", "r+")

    for line in f:
        print(line, end="")

    content = "this is the new content"
    charnum = f.write(content)
    print(f"charnum={charnum}")
except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)
finally:
    f.close()

