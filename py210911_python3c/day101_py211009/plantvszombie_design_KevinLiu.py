"""
game design (OO) : PvZ
author : Kevin Liu
"""


class Entity:
    # variables
    hp = 0
    coordinate = [0, 0]

    # behaviours
    def spawn(self, x, y):
        self.coordinate = [x, y]

    def destroy(self):
        pass


class Plant(Entity):
    # variables
    sun_cost = 0


class Peashooter(Plant):
    # variables
    hp = 50
    sun_cost = 100
    dmg = 10

    # behaviours
    def atk(self):
        pass


class SnowPea(Peashooter):
    ability = 'FREEZE'
    sun_cost = 175


class Sunflower(Plant):
    # variables
    hp = 50
    sun_cost = 50

    # behaviours
    def make_sun(self):
        pass


class WallNut(Plant):
    # variables
    hp = 150
    sun_cost = 50


class Zombie(Entity):
    # variables
    atk_dmg = 0

    # behaviours
    def move(self):
        pass

    def end_game(self):  # eat your brains
        pass


class NormalZombie(Zombie):
    # variables
    hp = 270
    atk_dmg = 15


class ConeheadZombie(Zombie):
    # variables
    hp = 640  # 370 - cone + 270 zombie
    atk_dmg = 15


class BucketheadZombie(Zombie):
    # variables
    hp = 1370  # 1100 - bucket + 270 zombie
    atk_dmg = 15


class PoleVaultingZombie(Zombie):
    # variables
    hp = 500
    atk_dmg = 15
    jumping_pole = "Yes"  # yes : still has jump power, if no : cannot jump

    # behaviours
    def jump(self):
        if self.jumping_pole == "Yes":
            self.coordinate[1] -= 1
        self.jumping_pole = "No"
