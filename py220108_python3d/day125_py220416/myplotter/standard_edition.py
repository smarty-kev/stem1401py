"""
standard edition

Requirements of Standard Edition:
An end-user may input a name of shape from their keyboard.
The application then draws a shape that the user desires.
The basic parameter(s) of a shape should print on the console, which determines possible measurements of a shape.
i.e. perimeter, area, surface area, volume, etc.
The perimeter of a 2D shape should print on the console.
The area of a 2D shape should print on the console.
The volume of a 3D shape should print on the console.
The surface area of a 3D shape should print on the console.
"""


from shape_entities import *


class PerimeterFinder:
    def getPerimeter(self, shape_obj):
        pass

    def getMultiplePerimeter(self, *shape_obj):
        pass


class AreaFinder:
    def getArea(self, shape_obj):
        pass

    def getMultipleArea(self, *shape_obj):
        pass


class VolumeFinder:
    def getVolume(self, shape_obj):
        pass

    def getMultipleVolume(self, *shape_obj):
        pass


class MyPlotter(PerimeterFinder, AreaFinder, VolumeFinder):
    def __init__(self, *shapes):
        self.__shapes = shapes

    def drawShape(self):
        pass
