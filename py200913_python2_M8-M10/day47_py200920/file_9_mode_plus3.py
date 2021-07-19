"""
file mode 'a+'
"""

with open("file_9_mode_plus3.txt", "a+") as f:
    f.write("This is the new text\n")
    f.seek(0) # Important : return to the top of the file before reading, otherwise you'll just read an empty string
    data = f.read() # Returns 'somedata\n'
    print(data)
