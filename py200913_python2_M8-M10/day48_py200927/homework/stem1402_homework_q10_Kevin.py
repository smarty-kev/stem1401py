"""
10. Write a Python program to count the frequency of words in a file.
"""

file = open("text_hmw_Kevin.txt", "r")

word = input("Word to check (case sensitive): ")

word_count = 0

text = file.readlines()

text = str(text).split()
for w in text:
    if w == word:
        word_count += 1

print(f"The word \"{word}\" occurred {word_count} times in the file text_hmw_Kevin.txt")

file.close()
