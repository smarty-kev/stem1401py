"""
Program : list all combinations of a set of characters
Author : Kevin
Date : 2020-08-29
"""

"""
my ideas:
ask user input and convert it into a list
probably use recursive functions to find answer
"""

# my attempt
# it doesnt work
"""
word = input("Please enter a word: ")
word = list(word)

a = len(word)

while a < a**a:
    for pos in range(0,len(word)+1):
        if pos == 0:
            word[pos] = word[pos+1]
        else:
            word[pos] = word[pos-1]
        for i in word:
            print(i, end="")
        print()
    a += 1
"""
