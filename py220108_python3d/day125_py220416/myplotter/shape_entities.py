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


class Shape:
    def __init__(self, shape_type=None):
        self.shape_type = shape_type


class TwoDShape(Shape):
    def __init__(self, shape_type=None):
        super().__init__(shape_type)


class Rectangle(TwoDShape):
    def __init__(self, a=int, b=int, shape_type="Rectangle"):
        self.a = a
        self.b = b
        super().__init__(shape_type)


class Square(Rectangle):
    def __init__(self, a=int, shape_type="Square"):
        self.a = a
        super().__init__(shape_type=shape_type)


class Triangle(TwoDShape):
    def __init__(self, a=int, h=int, shape_type="Triangle"):
        self.a = a
        self.h = h
        super().__init__(shape_type)


class RightTriangle(Triangle):
    def __init__(self, a=int, b=int, c=int,  shape_type="Right Triangle"):
        self.a = a
        self.b = b
        self.c = c
        super().__init__(shape_type=shape_type)


class Circle(TwoDShape):
    def __init__(self, r=int, shape_type="Circle"):
        self.r = r
        super().__init__(shape_type)


class Oval(TwoDShape):
    def __init__(self, r1=int, r2=int,  shape_type="Oval"):
        self.r1 = r1
        self.r2 = r2
        super().__init__(shape_type=shape_type)


class Parallelogram(TwoDShape):
    def __init__(self, a=int, b=int,  shape_type="Parallelogram"):
        self.a = a
        self.b = b
        super().__init__(shape_type=shape_type)


class Rhombus(Parallelogram):
    def __init__(self, d1=int, d2=int, shape_type="Rhombus"):
        self.d1 = d1
        self.d2 = d2
        super().__init__(shape_type=shape_type)


class ThreeDShape(Shape):
    def __init__(self, shape_type=None):
        super().__init__(shape_type)


class Sphere(ThreeDShape):
    def __init__(self, r=int, shape_type="Sphere"):
        self.r = r
        super().__init__(shape_type)


class Cylinder(ThreeDShape):
    def __init__(self, r=int, h=int, shape_type="Cylinder"):
        self.r = r
        self.h = h
        super().__init__(shape_type)


class Cube(ThreeDShape):
    def __init__(self, a=int, shape_type="Square"):
        self.a = a
        super().__init__(shape_type)


class Pyramid(ThreeDShape):
    def __init__(self, h=int, base_shape=TwoDShape, shape_type="Pyramid"):
        self.h = h
        self.base_shape = base_shape
        super().__init__(shape_type)
