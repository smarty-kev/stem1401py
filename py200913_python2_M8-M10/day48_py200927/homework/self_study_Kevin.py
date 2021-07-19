"""
1. write code to self-study truncate() /seek(),tell() [and seekable() -> optional]
"""

# truncate(size:Optional[int]...)

# case 1. no argument
print("===Truncate(size:Optional[int]...)===")
f = open("txt_study.txt", "w+")
result = f.truncate()
print("case 1. no argument")
print("f.truncate()")
print(result, type(result))
f.write('''This is the content of this file''')
# truncates the whole text of a file
print("conclusion : Truncate() function truncates (deletes) all the text in a file\n")

# case 2. with argument
result = f.truncate(5)
print("case 2. with [size]")
print("f.truncate(5)")
print(result, type(result))
# truncates till [size=int] characters is left in the file
print("conclusion : truncates till [size=int] characters is left in the file\n")

# answer from internet
print("answer from internet, https://www.tutorialspoint.com/python/file_truncate.htm")
print("""Python file method truncate() truncates the file's size. If the optional size argument is present, the file is truncated to (at most) that size.
The size defaults to the current position. The current file position is not changed. Note that if a specified size exceeds the file's current size, the result is platform-dependent.
Note − This method would not work in case file is opened in read-only mode.""")
print("This method does not return any value.")
print("size − If this optional argument is present, the file is truncated to (at most) that size.\n")

f.write('''This is the content of this file''')

# seek()
print("===seek(offset:int, whence:int...)===")

# case 1. no argument
print("case 1. no argument")
print("f.seek()")
# result = f.seek() -> TypeError: seek expected at least 1 argument, got 0
# error must have at least 1 argument
print("conclusion : error - seek() must have at least one argument\n")

# case 2. with one argument
print("case 2. with one argument")
result = f.seek(3)
print("f.seek(1)")
print(result, type(result))
# truncates until [argument] size is left
print("conclusion : sets the current position of the file\n")

# case 3. with two arguments
print("case 3. with two arguments")
# f.seek(3, 5)
print("f.seek(3, 5)")
# ValueError: invalid whence (5, should be 0, 1 or 2)
print("error - must be 0, 1, 2")
# f.seek(3, 2)
print("f.seek(3, 1)")
# io.UnsupportedOperation: can't do nonzero end-relative seeks
print("error - io.UnsupportedOperation")
print("conclusion : ?\n")

# answer from internet
print("answer from internet, https://www.w3schools.com/python/ref_file_seek.asp")
print("The seek() method sets the current file position in a file stream. The seek() method also returns the new position.\n")


# tell()
print("===tell()===")

# case 1.
print("case 1.")
print("f.tell()")
result = f.tell()
print(result, type(result))
# tell() tells you the current position of the file
print("conclusion : tell() tells you the current position of the file")


# answer form internet
print("answer from internet, https://www.w3schools.com/python/ref_file_tell.asp")
print("The tell() method returns the current file position in a file stream.")

f.close()
