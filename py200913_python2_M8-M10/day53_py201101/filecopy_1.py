"""

"""

from shutil import copyfile
import sys

source = input("Enter the source file with full path")
target = input("Enter the target file with full path")

# adding exception handling
try:
    copyfile(source, target)
except IOError as e:
    print("Unable to copy file. %s" % e)
    exit(1)
except:
    print("Unexpected Error: ", sys.exc_info())
    exit(1)

print("\nFile Copy Done!\n")

while True:
    print("Do you like to print the file ? (y/n)")
    check = input()
    if check == "n":
        break
    elif check == "y":
        with open(target, "r") as file:
            print("\nHere follows the file content\n")
            print(file.read())
            file.close()
            print()
        break
    else:
        continue

