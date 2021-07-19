"""
1. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
"""

import string


def create_file(letter):
    with open(f"{letter}.txt", "x") as file:
        file.close()


for letter in string.ascii_uppercase:
    create_file(letter)