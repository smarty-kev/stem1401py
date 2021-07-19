"""
to get an item from a list(sequence) randomly
"""

import random

items = ['gold','weapon','diamond','pet','armor','hp potion','mp potion']
for i in range(3):
    a = random.randrange(7)
    print("You got {}!".format(items[a]))
