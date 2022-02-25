"""
Shapes are as follows:
(a) circle
(b) square
(c) equilateral triangle
Hints:
Design a parent class such as Shape
Design a method (i.e. method name could be getArea ) to calculate the area in the Shape class
Design classes for every shape
Design a method for each to calculate the area
Those methods must override the method (i.e. getArea )
Those methods have the same signature
Each method accepts one parameter of double type
Be noted that the formula can be taken as a function of x, where x is the parameter as input.
Formulas:
The area of circle:        f(r) = Pi * r * r   (where r is radius as input)
The area of square:     f(a) = a * a    (where a is side of square as input)
The area of equilateral triangle:   Heron's formula (refer to the link below)
"""

import math
PI = math.pi


class Shape:
    def getArea(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        area = PI * self.radius ** 2
        return area


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def getArea(self):
        area = self.side ** 2
        return area


class EquilateralTriangle(Shape):
    def __init__(self, side):
        self.side = side

    def getArea(self):
        s = (self.side * 3) / 2
        area = math.sqrt(s * (s-self.side) ** 3)
        return area


# main program
circle = Circle(3)
square = Square(2)
equilateral_triangle = EquilateralTriangle(5)

print(circle.getArea())                # 28.274333882308138
print(square.getArea())                # 4
print(equilateral_triangle.getArea())  # 10.825317547305483
