"""
case 1. directly accessing properties and methods of parent class
"""


class Computer:
    def __init__(self, cpu, gpu, ram, storage, power_supply, os):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.storage = storage
        self.power_supply = power_supply
        self.os = os

        self.state = "off"

    def open(self):
        print("Open")
        self.state = "on"

    def close(self):
        print("Shut down")
        self.state = "off"


class Laptop(Computer):
    pass
    # only properties and methods of parent class


laptop1 = Laptop("i7", "rtx 2060", "8gbx2", "500ssd", "500w", "windows 11")

laptop1.open()  # Open
print(laptop1.cpu)  # i7
print(laptop1.os)  # windows 11
laptop1.close()  # Shut down
