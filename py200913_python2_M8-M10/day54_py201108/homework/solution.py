"""
solution for homework 1
"""
import string


def test_filename(filename, extension=".txt"):
    print(f"{filename}{extension}")

def create_file(filename, extension=".txt"):
    with open(f"{filename}{extension}", "x") as file:
        file.close()


for letter in string.ascii_uppercase:
    # print(letter)
    test_filename(letter, ".log")
    # create_file(letter)