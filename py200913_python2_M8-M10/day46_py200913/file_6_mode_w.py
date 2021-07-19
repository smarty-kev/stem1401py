"""
file mode w -write
1. Open with a mode
2. R/W
3. Close

conclusion:
the mode of 'w' will create a new if file if it does not exist
will truncated the text if the file already exists
"""

# case 1.
try:
    f = open("file_6_mode_w", "w")

    content = """this is the new content
    to change. Idk what to write lol"""
    charnum  = f.write(content)
    print(f"{charnum} has been writing in file: file_6_mode_w")

except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)

finally:
    f.close()

# case 2.
try:
    f = open("file_6_mode_w2", "w")

    content = """this is the new content
    to change. Idk what to write lol"""
    charnum  = f.write(content)
    print(f"{charnum} has been writing in file: file_6_mode_w2")

except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)

finally:
    f.close()

# case 3.
# log.txt
try:
    f = open("log", "w")

    content = input("Enter what you want to add: ")
    charnum  = f.write(content)
    print(f"{charnum} has been writing in file: log")

except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)

finally:
    f.close()
