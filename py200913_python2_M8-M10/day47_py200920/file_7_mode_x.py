"""

"""
# case 1. file does not exist
f = open("file_7_mode_x.txt", "x")

content = "This is the content of file_7_mode_x.txt"
charnum = f.write(content)
f.close()

print(f"charnum={charnum}")

# case 2. file already exist
try:
    f = open("file_7_mode_x.txt", "x")

    content = "This is the content of file_7_mode_x.txt"
    charnum = f.write(content)
    f.close()

    print(f"charnum={charnum}")
except Exception as e:
    print(e)
finally:
    f.close()
