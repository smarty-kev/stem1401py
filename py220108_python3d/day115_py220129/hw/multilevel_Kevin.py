"""
Inheritance type : multilevel inheritance
Description
Computer(cpu, gpu, ram, storage, power_supply, os, open(), close())
Laptop(keyboard, screen, trackpad, battery)
2in1_Laptop(touchscreen, rotate())
A 2-1 laptop is a laptop, and a laptop is a computer.
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


class TwoInOne(Laptop):
    def __init__(self, cpu, gpu, ram, storage, power_supply, os, keyboard, screen, trackpad, battery, touchscreen='yes'):
        super().__init__(cpu, gpu, ram, storage, power_supply, os, keyboard, screen, trackpad, battery)
        self.touchscreen = touchscreen

    def rotate(self):
        print("ROTATE")


new_laptop = TwoInOne('i7', 'integrated', '16gb', '500gb ssd', 'integrated', 'windows 11', 'standard - us',
                      '1920x1080', 'multi-touch', '60watts')
new_laptop.open()
new_laptop.rotate()
new_laptop.close()
