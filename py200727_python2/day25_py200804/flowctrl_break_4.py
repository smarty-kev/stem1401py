"""
project:

user can input a word
if the word contains the letter of i
please do not show the letter of i
otherwise show every letter of that word

input >> apple
apple
input >> string
str
"""

word = list(input("Please input a word: "))

for letter in range(len(word)):
    if "i" in word[letter]:
        break
    print(word[letter],end="")
