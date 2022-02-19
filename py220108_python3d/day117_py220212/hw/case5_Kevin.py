"""
case 5. defining __init__ method in child class
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
    def __init__(self, cpu, gpu, ram, storage, power_supply, os, keyboard, screen, trackpad, battery):
        super().__init__(cpu, gpu, ram, storage, power_supply, os)
        self.keyboard = keyboard
        self.screen = screen
        self.trackpad = trackpad
        self.battery = battery

    def carry(self):
        print("put in bag")

    def recharge(self):
        print("battery % : 100")


laptop1 = Laptop("i7", "rtx 2060", "8gbx2", "500ssd", "500w", "windows 11", "standard - us", "4k - touch", "multi-touch", "100w")

laptop1.open()  # Open \n Turn display on
print(laptop1.cpu)  # i7

# attribute defined in the __init__ function of child class
print(laptop1.keyboard)  # standard - us
print(laptop1.screen)  # 4k - touch
print(laptop1.keyboard)  # standard - us
print(laptop1.battery)  # 100w


print(laptop1.os)  # windows 11
laptop1.close()  # Shut down \n Turn display off
