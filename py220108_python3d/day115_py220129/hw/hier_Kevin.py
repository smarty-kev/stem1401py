"""
Inheritance type : hierarchical inheritance
Description
Computer(cpu, gpu, ram, storage, power_supply, os, open(), close())
Laptop(keyboard, screen, trackpad, battery)
SmartPhone(touchscreen, camera, keyboard=optional, home_button=optional)
A laptop is a computer, a smartphone is a computer, but a phone is not a laptop.
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


class SmartPhone(Computer):
    def __init__(self, cpu, gpu, ram, storage, power_supply, os, touchscreen, battery, camera):
        super().__init__(cpu, gpu, ram, storage, power_supply, os)
        self.screen = touchscreen
        self.battery = battery
        self.camera = camera

    def take_photo(self):
        print("Take photo")


gaming_laptop = Laptop('i7', 'integrated', '16gb', '500gb ssd', 'integrated', 'windows 11', 'standard - us',
                       '1920x1080', 'multi touch', "60watts")
gaming_laptop.open()
gaming_laptop.close()

iphone_13 = SmartPhone('a15', 'integrated', '4gb', '128gb', 'integrated', 'iOS 15', 'multi_touch', '4000watts',
                       '3 camera setup')
iphone_13.take_photo()

