"""
cursor


read()
read(n)        n bytes
readline()     n line
readlines()

tell()
seek()


question 1.
    1 byte =? 1 char
    read(n)  n -> 1 char

encoding = ascii
"""

print("===Start===")
with open("textfile1.txt", encoding="utf-8") as file:
    print("current position =", file.tell())

    content = file.read(1)
    print(content, end="")
    print("current position =", file.tell())


    content = file.read(1)
    print(content, end="")
    print("current position =", file.tell())


    content = file.read(1)
    print(content, end="")
    print("current position =", file.tell())
    print()

    # move cursor to 0, the very beginning
    file.seek(0)
    content = file.read(1)
    print(content, end="")
    print("current position =", file.tell())

    content = file.read(1)
    print(content, end="")
    print("current position =", file.tell())

    content = file.read(1)
    print(content, end="")
    print("current position =", file.tell())
    print()

    # move cursor to specified position
    file.seek(3)
    content = file.read(1)
    print(content, end="")
    print("current position =", file.tell())

    content = file.read(1)
    print(content, end="")
    print("current position =", file.tell())

    content = file.read(1)
    print(content, end="")
    print("current position =", file.tell())
    print()

    # move cursor to invalid position
    file.seek(2)

    try:
        content = file.read(1)
        print(content, end="")
        print("current position =", file.tell())
        print()
    except UnicodeDecodeError as ue:
        print("Invalid Position")
    except Exception as e:
        print("Error")


print("====End====")
