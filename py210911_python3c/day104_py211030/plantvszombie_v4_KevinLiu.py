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


class Resource():
    # Class variables
    def __init__(self, starting_value):
        self.sun_count = starting_value

    # behaviours
    def accumulate(self, received_sun_value):
        self.sun_count += received_sun_value

    def decrease(self, used_sun_value):
        self.sun_count -= used_sun_value


class Entity:
    # Class variables
    def __init__(self, hp, coord):  # coord is a list
        self.hp = hp
        self.coordinate = coord
        self.name = self.__class__.__name__

    # behaviours
    def spawn(self, coordinate):
        self.coordinate = coordinate  # coordinate is a list
        print(f"Spawned {self.name}, at x:{self.coordinate[0]}, y:{self.coordinate[1]}")

    def destroy(self):
        print("Destroy() was called.")


class Plant(Entity):

    # Class variables
    def __init__(self, hp, coord, sun_cost):
        super().__init__(hp, coord)
        self.sun_cost = sun_cost

    # behaviours
    def buy(self, Resource, coordinate):
        if self.sun_cost <= Resource.sun_count:
            Resource.decrease(self.sun_cost)
            self.spawn(coordinate)
        else:
            print(f"You do not have enough resources. You have {Resource.sun_count}. You need {self.sun_cost}")


class Peashooter(Plant):
    # Class variables
    def __init__(self, hp, coord, sun_cost, atk_dmg):
        super().__init__(hp, coord, sun_cost)
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
    def __init__(self, hp, coord, sun_cost, atk_dmg, ability):
        super().__init__(hp, coord, sun_cost, atk_dmg)
        self.ability = ability


class Sunflower(Plant):
    # Class variables
    def __init__(self, hp, coord, sun_cost, capacity):  # capacity is the value of every sun it makes
        super().__init__(hp, coord, sun_cost)
        self.capacity = capacity

    # behaviours
    def make_sun(self, Resource):
        Resource.accumulate(self.capacity)


class WallNut(Plant):
    # Class variables
    def __init__(self, hp, coord, sun_cost, name):
        super().__init__(hp, coord, sun_cost)
        self.sun_cost = sun_cost


class Zombie(Entity):
    # Class variables
    def __init__(self, hp, coord, atk_dmg, name, target):
        super().__init__(hp, coord)
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
    def __init__(self, hp, coord, atk_dmg, target):
        super().__init__(hp, coord, atk_dmg, target)


class PoleVaultingZombie(Zombie):
    def __init__(self, hp, coord, atk_dmg, target, jumping_pole):
        super().__init__(hp, coord, atk_dmg, target)
        self.jumping_pole = jumping_pole  # True = still has ability, False = doesn't have ability anymore

    # behaviours
    def jump(self):
        if self.jumping_pole:  # if self.jumping_pole == True
            self.coordinate[1] -= 1


class ConeheadZombie(Zombie):
    def __init__(self, hp, coord, atk_dmg, target, hat_hp):
        super().__init__(hp, coord, atk_dmg, target)
        self.hat_hp = hat_hp

    # behaviours
    def lose_hat(self):
        self.hp += self.hat_hp


# main program
resource = Resource(50)

sunflower1 = Sunflower(50, [2, 0], 50, 25)
sunflower1.buy(resource, sunflower1.coordinate)  # Spawned Sunflower, at x:2, y:0

sunflower2 = Sunflower(50, [3, 0], 50, 25)
sunflower2.buy(resource, sunflower2.coordinate)  # You do not have enough resources. You have 0. You need 50

sunflower1.make_sun(resource)                    # gained 25 sun
sunflower1.make_sun(resource)                    # gained 25 sun
sunflower1.make_sun(resource)                    # gained 25 sun

sunflower2.buy(resource, sunflower2.coordinate)  # Spawned Sunflower, at x:3, y:0
