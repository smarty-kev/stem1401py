"""
Write a python program to find the longest words.
"""

try:
    f = open("text_q1_Kevin.txt")
    content = f.read()
    words = content.split()
    # print(words)
    long_word = []
    len_current_long_word = 0
    for w in words:
        if len(w) > len_current_long_word:
            long_word.append(w)
            len_current_long_word = len(w)
        elif len(w) == len_current_long_word:
            long_word.append(w)
    # print(len_current_long_word)
    for w in long_word:
        if len(w) < len_current_long_word:
            long_word = list(filter(lambda x : len(x) == len_current_long_word, long_word))
    print(long_word)
except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)
finally:
    f.close()

