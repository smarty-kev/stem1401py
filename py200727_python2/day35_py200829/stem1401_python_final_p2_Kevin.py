"""
Program : count the times each character occurs in a given sentence
Author : Kevin
Date : 2020-08-29
"""

"""
my ideas:
create a dictionary from a-z and start at 0 for each value
first we ask the input of user
then we make a for loop to pick up each char in sentence (except [space]) and add 1 to char
print dictionary
"""

# explanation
print("This program counts the number of time a letter is in your input")

# entire alphabet, start count = 0
alphabet = {
    "a" : 0,
    "b" : 0,
    "c" : 0,
    "d" : 0,
    "e" : 0,
    "f" : 0,
    "g" : 0,
    "h" : 0,
    "i" : 0,
    "j" : 0,
    "k" : 0,
    "l" : 0,
    "m" : 0,
    "n" : 0,
    "o" : 0,
    "p" : 0,
    "q" : 0,
    "r" : 0,
    "s" : 0,
    "t" : 0,
    "u" : 0,
    "v" : 0,
    "w" : 0,
    "x" : 0,
    "y" : 0,
    "z" : 0,
}

# user input
sentence = input("Please enter your sentence or a word (in all lowercase): ")

# counting process
for l in sentence:
    if l in alphabet:
        alphabet[l] += 1

# echo answer
for letter in alphabet:
    if alphabet[letter] > 0:
        print("{} = ".format(letter),end="")
        print(alphabet[letter])


# end
print("End, Goodbye!")
