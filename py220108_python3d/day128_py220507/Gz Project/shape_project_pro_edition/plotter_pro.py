"""
plotter for standard edition of the project
"""

from shape_entities_pro import *


class Plotter:
    def __init__(self):
        print('Pro Edition Plotter')

    def plotShapes(self, shape):
        print('Drawing the shape...')
        if shape.shape_type == 'Rectangle' or shape.shape_type == 'Triangle' or shape.shape_type == 'Square' or shape.shape_type == 'Circle'\
                or shape.shape_type == 'Parallelogram' or shape.shape_type == 'RightTriangle' or shape.shape_type == 'Rhombus' \
                or shape.shape_type == 'Oval':
            perimeter = shape.Perimeter()
            area = shape.Area()
            print(f'The perimeter of the {shape.shape_type} is {perimeter}')
            print(f'The area of the {shape.shape_type} is {area}')

        if shape.shape_type == 'Cube' or shape.shape_type == 'Sphere' or shape.shape_type == 'Cylinder' or shape.shape_type == 'Pyramid':
            area = shape.Area()
            volume = shape.Volume()
            print(f'The area of the {shape.shape_type} is {area}')
            print(f'The volume of the {shape.shape_type} is {volume}')
