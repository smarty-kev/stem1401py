"""
Part 1 Questions 60 points
"""

# question 1
"""
Exception Handling is the process of trying to "catch" the exception. This means finding the problem and making the
program not crash

syntax:
try:
    code
except  Error:
    code
except  Error2:
    code
finally:
    code
"""

# question 2
"""
A built in Exception are exception that are predefined in the Python language
"""

# q3
"""
user-defined exceptions are when you custom make an exception
"""

# q4
"""
An exception can occur when something unexpected appears in the flow of the program
The programmer can raise an error by using: except Error:
                                                   print(Error)
"""

# q5
"""
File output is when you read the file
File input is when you write in the file
"""

# q6
"""
r   read only
r+  read and write
w   write only
w+  write and read
a   append, cannot read
a+  append and read
x   create only
"""

# q7
"""
we can open it with the correct/appropriate character encoding (ex: UTF-8, US-ASCII, UTF-16, etc)
"""

# q8
"""
we can reset the cursor location in the file and read again
use : seek()
"""

# q9
"""
read in chunks, because it uses less system memory
ex:
file.read(n)
n is number of bytes
"""

# q10
"""
For a 'Log' document, it is better to use append mode (a/a+) because you do not want to erase what was previously written
if you would have used write mode (w/w+), it would essentially delete everything and restart
"""

# q11
"""
write() writes without \ns
writelines() writes with \ns
"""

# q12
"""
a tree structure is like a tree, it has branches and leaves. Both start at the root, which then separates into branches
which then can separate into more branches or leaves.
"""

# q13
"""
os.getcwd() - gets current directory
os.chdir()  - changes current directory
os.listdir() - lists all files and directories under specified directory
os.mkdir()  - creates a directory
os.rename() - renames file or directory
os.remove() - removes file or directory, thought the latter must be empty
shutil.rmdir()  - removes directories
os.path.getsize() - gets size of specified file
shutil.copyfile() - copies file from one to another
os.path.isdir() - returns true if is dir
os.path.exists() - returns true if path exists
"""

# q14
"""
relative path is inside your current directory
absolute path/full path is the entire path (to its root)
"""

# q15
"""
datetime.datetime.now()
datetime.date.today()
datetime.date()
datetime.date.fromtimestamp()
datetime.datetime.strptime()

from what ive learned, 5 ways
"""

# q16
"""
import datetime
now = datetime.datetime.now()           - current date and time
current_time = f"{now.hour}:{now.minute}    {now.second}sec(s)"            - current time
time = now.strftime("%Y-%m-%d %H:%M:%S")            - specified format
time2 = now.strftime("%I:%M %p")                    - specified format
"""
