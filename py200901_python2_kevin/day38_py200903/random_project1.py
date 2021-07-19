"""
Random Project : Version 1
Author : Kevin
Treasure Chest
Design and write a program for a treasure chest in an MMORPG game.
The item rank it may drop from the chest includes:
	normal						0.638
	magic				1/4		0.25
	rare				1/10	0.1
	legendary			1/100	0.01
	ancient legendary	1/500	0.002

Please write some test code to simulate opening chest for certain times like 100 times,
500 times, 1000 times or more
Analyze the result with your settings of probability of items dropping from the chests.
"""
# import random
import random

# list of every drop
probability = []

# add 638 Normal to list
for i in range(638):
    probability.append("Normal")

# add 250 Magical to list
for i in range(250):
    probability.append("Magical")
# add 100 Rare to list
for i in range(100):
    probability.append("Rare")
# add 10 legendary to list
for i in range(10):
    probability.append("Legendary")
# add 2 Ancient Legendary to list
for i in range(2):
    probability.append("Ancient Legendary")

# number of drops dictionary
num_of_drops = {
    "Normal" : 0,
    "Magical" : 0,
    "Rare" : 0,
    "Legendary" : 0,
    "Ancient Legendary" : 0
}

# number of draws
draws = 100000

# random individual drop
for i in range(draws):
    random.shuffle(probability)
    num_of_drops[probability[0]] += 1
else:
    print("In {} draws, you got:".format(draws))

# print out answer
for rarity in num_of_drops:
    print("{} = {}".format(rarity,num_of_drops[rarity]))
