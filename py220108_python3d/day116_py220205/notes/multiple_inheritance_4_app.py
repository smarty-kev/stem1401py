"""
multiple inheritance

application
RPG (Character, Doll)
Level, occupation, rank

Rank I
Occupation (Warrior I, Magician I)

Rank II
Warrior I -> Magical Warrior
melee(), holy_shield()

Magician I -> Warrior Magician
fireball(), melee()
"""


class Magician:
    def fireball(self):
        print("fireball")


class Warrior:
    def melee(self):
        print("melee")


class MagicalWarrior(Warrior, Magician):
    def holy_shield(self):
        print("holy shield")


class WarriorMagician(Magician, Warrior):
    pass
