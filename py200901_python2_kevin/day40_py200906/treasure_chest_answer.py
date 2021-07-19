"""
Treasure chest example - Guang Zhu
"""
from random import randint
normal = 0
rare = 0
magic = 0
legendary = 0
ancient_legendary = 0
for i in range(10000):
    a = randint(1, 1001)
    if a < 639:
        print("You got a Normal")
        normal += 1
    elif a < 889:
        print("You got a Rare")
        rare += 1
    elif a < 989:
        print("You got a Magic")
        magic += 1
    elif a < 999:
        print("You got a Legendary")
        legendary += 1
    else:
        print("You got a Ancient legendary")
        ancient_legendary += 1
print("You got {} normals".format(normal))
print("You got {} rares".format(rare))
print("You got {} magics".format(magic))
print("You got {} legendary".format(legendary))
print("You got {} ancient legendarys".format(ancient_legendary))