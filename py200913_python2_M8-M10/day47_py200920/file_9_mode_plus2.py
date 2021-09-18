"""
file mode 'w+'
"""

with open("file_9_mode_plus2.txt", "w+") as f:
    # note that f has now been truncated to 0 bytes, so you'll only
    # be able to read data that you write after this point
    f.write("This is the new text\n")
    f.seek(0) # Important : return to the top of the file before reading, otherwise you'll just read an empty string
    data = f.read() # Returns 'somedata\n'
    print(data)

