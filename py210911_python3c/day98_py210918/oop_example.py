"""
example of Object-Oriented Programming
"""


class Bicycle:

    # Class variables
    gear = 1
    speed = 0

    # behaviours
    def __init__(self, gear, speed):
        self.gear = gear
        self.speed = speed

    def speed_up(self, increase):
        self.speed += increase

    def change_gear(self, new_gear):
        self.gear = new_gear

    def brake(self, decrease):
        self.speed -= decrease


my_bicycle = Bicycle(10, 5)
print(my_bicycle.speed)
