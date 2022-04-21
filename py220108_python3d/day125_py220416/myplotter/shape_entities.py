"""
2D Shapes:
Circle, Rectangle, Square, Triangle, Right Triangle, Oval, Parallelogram, Rhombus

3D Shapes:
Sphere, Cube, Pyramid, Cylinder
"""

import math

# the value of π (pi) will not be taken as absolute value
PI = 3.14159265358979


class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type


class TwoDShape(Shape):
    def __init__(self, shape_type):
        super().__init__(shape_type)

    def findPerimeter(self):
        pass

    def findArea(self):
        pass


class Rectangle(TwoDShape):
    def __init__(self, a=int, b=int, shape_type="Rectangle"):
        self.a = int(a)
        self.b = int(b)
        super().__init__(shape_type)

    def findPerimeter(self):
        perimeter = 2 * (self.a + self.b)
        return perimeter

    def findArea(self):
        area = self.a * self.b
        return area


class Square(TwoDShape):
    def __init__(self, a=int, shape_type="Square"):
        self.a = int(a)
        super().__init__(shape_type)

    def findPerimeter(self):
        perimeter = 4 * self.a
        return perimeter

    def findArea(self):
        area = self.a ** 2
        return area


class Triangle(TwoDShape):
    def __init__(self, base=int, h=int, side2=int, side3=int, shape_type="Triangle"):
        self.base = int(base)  # base = side1
        self.h = int(h)
        self.side2 = int(side2)
        self.side3 = int(side3)
        super().__init__(shape_type)

    def findPerimeter(self):
        perimeter = self.base + self.side2 + self.side3
        return perimeter

    def findArea(self):
        area = (self.base * self.h) / 2
        return area


class RightTriangle(TwoDShape):
    def __init__(self, a=int, b=int, hypotenuse=int,  shape_type="Right Triangle"):
        self.a = int(a)
        self.b = int(b)
        if hypotenuse != int:
            self.hypotenuse = int(hypotenuse)
        super().__init__(shape_type)

    def findPerimeter(self):
        perimeter = self.a + self.b + self.hypotenuse
        return perimeter

    def findArea(self):
        area = (self.a * self.b) / 2
        return area

    def findHypotenuse(self):
        self.hypotenuse = math.sqrt(self.a ** 2 + self.b ** 2)
        return self.hypotenuse


class Circle(TwoDShape):
    def __init__(self, r=int, shape_type="Circle"):
        self.r = int(r)
        super().__init__(shape_type)

    def findPerimeter(self):
        perimeter = 2 * self.r * PI
        return perimeter

    def findArea(self):
        area = PI * (self.r ** 2)
        return area


class Oval(TwoDShape):
    def __init__(self, r1=int, r2=int,  shape_type="Oval"):
        self.r1 = int(r1)  # major radius
        self.r2 = int(r2)  # minor radius
        super().__init__(shape_type)

    def findPerimeter(self):
        r1 = self.r1  # major radius
        r2 = self.r2  # minor radius
        h = (r1 - r2) ** 2 / (r1 - r2) ** 2
        perimeter = PI * (r1 + r2) * (1 + h * 0.25 + (h**2) * (1/64) + (h**3) * (1/256) + (h**4) * (25/16384) +
                                      (h**5) * (49/65536) + (h**6) * (441/1048576))
        return perimeter

    def findArea(self):
        area = PI * self.r1 * self.r2
        return area


class Parallelogram(TwoDShape):
    def __init__(self, a=int, b=int,  shape_type="Parallelogram"):
        self.a = int(a)
        self.b = int(b)
        super().__init__(shape_type)

    def findPerimeter(self):
        perimeter = 2 * (self.a + self.b)
        return perimeter

    def findArea(self):
        area = self.a * self.b
        return area


class Rhombus(TwoDShape):
    def __init__(self, d1=int, d2=int, side=int, shape_type="Rhombus"):
        self.d1 = int(d1)
        self.d2 = int(d2)
        self.side = int(side)
        super().__init__(shape_type)

    def findPerimeter(self):
        perimeter = 4 * self.side
        return perimeter

    def findArea(self):
        area = (self.d1 * self.d2) / 2
        return area


class ThreeDShape(Shape):
    def __init__(self, shape_type=None):
        super().__init__(shape_type)

    def findArea(self):
        pass

    def findVolume(self):
        pass


class Sphere(ThreeDShape):
    def __init__(self, r=int, shape_type="Sphere"):
        self.r = int(r)
        super().__init__(shape_type)

    def findArea(self):
        area = 4 * PI * (self.r ** 2)
        return area

    def findVolume(self):
        volume = (4 * PI * (self.r ** 3)) / 3
        return volume


class Cylinder(ThreeDShape):
    def __init__(self, r=int, h=int, shape_type="Cylinder"):
        self.r = int(r)
        self.h = int(h)
        super().__init__(shape_type)

    def findArea(self):
        area_rectangle = self.h * 2 * self.r * PI
        area_circle = PI * (self.r ** 2)
        area = 2 * area_circle + area_rectangle
        return area

    def findVolume(self):
        area_circle = PI * (self.r ** 2)
        area = area_circle * self.h
        return area


class Cube(ThreeDShape):
    def __init__(self, a=int, shape_type="Square"):
        self.a = int(a)
        super().__init__(shape_type)

    def findArea(self):
        area_square = self.a ** 2
        area = 6 * area_square
        return area

    def findVolume(self):
        volume = self.a ** 3
        return volume


class Pyramid(ThreeDShape):
    def __init__(self, h=int, base_obj=TwoDShape, shape_type="Pyramid"):
        self.h = int(h)
        self.base_shape = base_obj
        super().__init__(shape_type)

    def findArea(self):
        area_base = self.base_shape.findArea()

        if self.base_shape.shape_type == "Rectangle":
            # print("rectangle")
            apothem_side_a = 0
            triangles_area = 2 * (Triangle(self.base_shape.a, ).getArea()) + 2 * (Triangle(self.base_shape.b))

        if self.base_shape.shape_type == "Square":
            # print("square")
            pass

        if self.base_shape.shape_type == "Rhombus":
            # print("rhombus")
            pass


        area = 0
        return area

    def findVolume(self):
        pass

