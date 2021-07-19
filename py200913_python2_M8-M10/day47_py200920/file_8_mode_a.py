"""
file mode 'a'
"""

# case 1. create file and file does not exist
f = open("file_8_mode_a.txt", "a")

content = "This is the new content that is added into file_8_mode_a.txt\n"
charnum = f.write(content)
f.close()

print(f"charnum={charnum}")


