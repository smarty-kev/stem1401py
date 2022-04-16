"""
2D Shapes:
Circle
Rectangle
Square
Triangle
Right Triangle
Oval
Parallelogram
Rhombus

3D Shapes:
Sphere
Cube
Pyramid
Cylinder
"""


class TwoDShape:
    def __init__(self, measurements=None, shape=None, color=None):
        self.measurements = measurements
        self.color = color
        self.shape = shape


class Circle(TwoDShape):
    def __init__(self, radius=None, circumference=None):
        measurements = {
            "radius": radius,
            "circumference": circumference,
        }
        super().__init__(measurements, "circle")


class Rectangle(TwoDShape):
    def __init__(self, radius=None, circumference=None):
        self.radius = radius
        super().__init__(circumference)
