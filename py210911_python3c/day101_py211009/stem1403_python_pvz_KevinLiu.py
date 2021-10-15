"""
[Homework]
Date: 2021-10-09
Due date: 2021-10-15
1. Design a game system in OO
Polish your design
double check and refine classes you found
Write a code framework for the game system you have.
Coding strictly according to your design (namely class diagram)
Submit your code along with your UPDATED class diagram (system design)
Hints:
At least 4 types of plant
At least 4 types of zombie
Search on the Internet for plant and zombie names
"""


class Entity:
    # Class variables
    hp = 0
    coordinate = (0, 0)

    # behaviours
    def __init__(self, hp, coord):
        self.hp = hp
        self.coordinate = coord


class Plant(Entity):
    # Class variables

    # behaviours
    def __init__(self, hp, coord, sun_cost):
        super().__init__(hp, coord)
        self.sun_cost = sun_cost


class Peashooter(Plant):
    sun_cost = 100


class SnowPea(Plant):
    sun_cost = 175


class Sunflower(Plant):
    sun_cost = 50


class WallNut(Plant):
    sun_cost = 50


class Zombie(Entity):
    # Class variables
    atk_dmg = 0

    # behaviours
    def __init__(self, hp, coord, atk_dmg):
        super().__init__(hp, coord)
        self.atk_dmg = atk_dmg


class NormalZombie(Zombie):
    pass


class PoleVaultingZombie(Zombie):
    pass


class ConeheadZombie(Zombie):
    pass


dude = Peashooter(50, (8 ,9), 80)
print(dude.hp, dude.coordinate, dude.sun_cost)
