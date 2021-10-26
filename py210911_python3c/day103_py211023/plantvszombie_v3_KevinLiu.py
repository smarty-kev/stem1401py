"""
[Homework]
Date: 2021-10-23
Due date: 2021-10-29
1. Write code for your game system in OO
Create at least 3 instances (objects) of plant
Create at least 3 instances (objects) of zombie
Note that more than one type for both plant and zombie instances are supposed to be created.
Describe the battle process between a peashooter and a zombie and write down as a comment
Write some trial code to implement that process in sequence.
Hints:
Coding strictly according to your design (the description of battle process)
Submit your code including your description of the battle process
"""

# the player's sun count
sun_stock = 0


class Entity:
    # Class variables
    def __init__(self, hp, coord, name):  # coord is a list
        self.hp = hp
        self.coordinate = coord
        self.name = name

    # behaviours
    def spawn(self, x, y):
        self.coordinate = [x, y]
        print(f"Spawned {self.name}, at x:{self.coordinate[0]}, y:{self.coordinate[1]}")

    def destroy(self):
        print("Destroy() was called.")


class Plant(Entity):

    # Class variables
    def __init__(self, hp, coord, sun_cost, name):
        super().__init__(hp, coord, name)
        self.sun_cost = sun_cost

    # behaviours
    def buy(self):
        global sun_stock
        sun_stock -= self.sun_cost


class Peashooter(Plant):
    # Class variables
    def __init__(self, hp, coord, sun_cost, atk_dmg, name):
        super().__init__(hp, coord, sun_cost, name)
        self.atk_dmg = atk_dmg

    # behaviours
    def attack(self, target):
        target.hp -= self.atk_dmg
        print(f"{self.name} dealt {self.atk_dmg} dmg to {target.name}!")
        if target.hp <= 0:
            target.destroy()
            print(f"{target.name} has succumbed!")


class SnowPea(Peashooter):
    # Class variables
    def __init__(self, hp, coord, sun_cost, atk_dmg, name, ability):
        super().__init__(hp, coord, sun_cost, atk_dmg, name)
        self.ability = ability


class Sunflower(Plant):
    # Class variables
    def __init__(self, hp, coord, sun_cost, capacity, name):  # capacity is the value of every sun it makes
        super().__init__(hp, coord, sun_cost, name)
        self.capacity = capacity

    # behaviours
    def make_sun(self):
        global sun_stock
        sun_stock += self.capacity


class WallNut(Plant):
    # Class variables
    def __init__(self, hp, coord, sun_cost, name):
        super().__init__(hp, coord, sun_cost, name)
        self.sun_cost = sun_cost


class Zombie(Entity):
    # Class variables
    def __init__(self, hp, coord, atk_dmg, name, target):
        super().__init__(hp, coord, name)
        self.atk_dmg = atk_dmg
        self.target = target

    # behaviours
    def move(self):
        if self.coordinate == self.target.coordinate:
            self.attack()
        else:
            self.coordinate[1] -= 1
            print(f"{self.name} moved to x:{self.coordinate[0]}, y:{self.coordinate[1]}")
        if self.coordinate[1] == -1:
            self.end_game()

    def attack(self):
        self.target.hp -= self.atk_dmg
        print(f"{self.name} dealt {self.atk_dmg} dmg to {self.target.name}!")
        if self.target.hp <= 0:
            self.target.destroy()
            print(f"{self.target.name} has succumbed!")

    def end_game(self):  # eat your brains
        print("The zombies have won!")


class NormalZombie(Zombie):
    def __init__(self, hp, coord, atk_dmg, name, target):
        super().__init__(hp, coord, atk_dmg, name, target)


class PoleVaultingZombie(Zombie):
    def __init__(self, hp, coord, atk_dmg, name, target, jumping_pole):
        super().__init__(hp, coord, atk_dmg, name, target)
        self.jumping_pole = jumping_pole  # True = still has ability, False = doesn't have ability anymore

    # behaviours
    def jump(self):
        if self.jumping_pole:  # if self.jumping_pole == True
            self.coordinate[1] -= 1


class ConeheadZombie(Zombie):
    def __init__(self, hp, coord, atk_dmg, name, target, hat_hp):
        super().__init__(hp, coord, atk_dmg, name, target)
        self.hat_hp = hat_hp

    # behaviours
    def lose_hat(self):
        self.hp += self.hat_hp


# main program


# plants
peashooter_1 = Peashooter(50, [2, 0], 100, 25, "Peashooter")
sunflower_1 = Sunflower(50, [3, 0], 50, 50, "Sunflower")
snow_pea_1 = SnowPea(50, [1, 0], 175, 25, "Snow Pea", "Freeze")


# zombies
zombie_1 = NormalZombie(270, [2, 6], 15, "Normal Zombie", peashooter_1)
pole_vaulting_zombie_1 = PoleVaultingZombie(500, [3, 4], 15, "Pole Vaulting Zombie", True, sunflower_1)
cone_head_zombie_1 = ConeheadZombie(270, [1, 3], 15, "Conehead Zombie", 370, snow_pea_1)


# spawning
peashooter_1.spawn(peashooter_1.coordinate[0], peashooter_1.coordinate[1])
zombie_1.spawn(zombie_1.coordinate[0], zombie_1.coordinate[1])
print("==================================")


# battle
peashooter_1.attack(zombie_1)  # Peashooter dealt 25 dmg to Normal Zombie!
zombie_1.move()                # Normal Zombie dealt 15 dmg to Peashooter!
print("===")

peashooter_1.attack(zombie_1)  # Peashooter dealt 25 dmg to Normal Zombie!
zombie_1.move()                # Normal Zombie dealt 15 dmg to Peashooter!
print("===")

peashooter_1.attack(zombie_1)  # Peashooter dealt 25 dmg to Normal Zombie!
zombie_1.move()                # Normal Zombie dealt 15 dmg to Peashooter!
print("===")

peashooter_1.attack(zombie_1)  # Peashooter dealt 25 dmg to Normal Zombie!
zombie_1.move()                # Normal Zombie dealt 15 dmg to Peashooter!
print("===")

peashooter_1.attack(zombie_1)  # Peashooter dealt 25 dmg to Normal Zombie!
zombie_1.move()                # Normal Zombie dealt 15 dmg to Peashooter!
print("===")

peashooter_1.attack(zombie_1)  # Peashooter dealt 25 dmg to Normal Zombie!
zombie_1.move()                # Normal Zombie dealt 15 dmg to Peashooter!
print("===")

peashooter_1.attack(zombie_1)  # Peashooter dealt 25 dmg to Normal Zombie!
zombie_1.move()                # Normal Zombie dealt 15 dmg to Peashooter!
print("===")

peashooter_1.attack(zombie_1)  # Peashooter dealt 25 dmg to Normal Zombie!
zombie_1.move()                # Normal Zombie dealt 15 dmg to Peashooter!
print("===")

peashooter_1.attack(zombie_1)  # Peashooter dealt 25 dmg to Normal Zombie!
zombie_1.move()                # Normal Zombie dealt 15 dmg to Peashooter!
print("===")

peashooter_1.attack(zombie_1)  # Peashooter dealt 25 dmg to Normal Zombie!
zombie_1.move()                # Normal Zombie dealt 15 dmg to Peashooter! Destroy() was called. Peashooter has succumbed!
del peashooter_1
print("===")

zombie_1.target.coordinate = [-1, -1]
zombie_1.move()  # Normal Zombie moved to x:2, y:-1 The zombies have won!
