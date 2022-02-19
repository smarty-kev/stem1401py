"""
hybrid inheritance
"""


class Car:
    def accelerate(self):
        print("VROOM")

    def brake(self):
        print("slow down")

    def turn(self):
        print("wheels turn")


class ElectricCar(Car):
    def recharge(self):
        print("Battery is recharged")


class FuelCar(Car):
    def refill(self):
        print("Fuel is refilled")


class HybridCar(ElectricCar, FuelCar):
    def switchMode(self):
        print("Switch Mode")
