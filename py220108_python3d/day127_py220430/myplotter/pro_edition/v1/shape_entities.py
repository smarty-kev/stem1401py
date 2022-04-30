"""
2D Shapes:
Circle, Rectangle, Square, Triangle  # standard
Right Triangle, Oval, Parallelogram, Rhombus  # pro

3D Shapes:
Sphere, Cube  # standard
Pyramid, Cylinder  # pro
"""

import math

# the value of π (pi) will not be taken as absolute value
PI = 3.14159265358979


class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type


class TwoDShape(Shape):
    def __init__(self, shape_type):
        self.dimension = "TwoD"
        super().__init__(shape_type)

    def findPerimeter(self):
        pass

    def findArea(self):
        pass


class Rectangle(TwoDShape):
    def __init__(self, a, b, shape_type="Rectangle"):
        self.a = float(a)
        self.b = float(b)
        super().__init__(shape_type)

    def findPerimeter(self):
        perimeter = 2 * (self.a + self.b)
        return perimeter

    def findArea(self):
        area = self.a * self.b
        return area


class Square(TwoDShape):
    def __init__(self, a, shape_type="Square"):
        self.a = float(a)
        super().__init__(shape_type)

    def findPerimeter(self):
        perimeter = 4 * self.a
        return perimeter

    def findArea(self):
        area = self.a ** 2
        return area


class Triangle(TwoDShape):
    def __init__(self, base, h, side2, side3, shape_type="Triangle"):
        self.base = float(base)  # base = side1
        self.h = float(h)
        self.side2 = float(side2)
        self.side3 = float(side3)
        super().__init__(shape_type)

    def findPerimeter(self):
        perimeter = self.base + self.side2 + self.side3
        return perimeter

    def findArea(self):
        area = (self.base * self.h) / 2
        return area


class RightTriangle(TwoDShape):
    def __init__(self, a, b, hypotenuse=None,  shape_type="Right Triangle"):
        self.a = float(a)
        self.b = float(b)
        self.hypotenuse = float(hypotenuse)
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
    def __init__(self, r, shape_type="Circle"):
        self.r = float(r)
        super().__init__(shape_type)

    def findPerimeter(self):
        perimeter = 2 * self.r * PI
        return perimeter

    def findArea(self):
        area = PI * (self.r ** 2)
        return area


class Oval(TwoDShape):
    def __init__(self, r1, r2,  shape_type="Oval"):
        self.r1 = float(r1)  # major radius
        self.r2 = float(r2)  # minor radius
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
    def __init__(self, a, b,  shape_type="Parallelogram"):
        self.a = float(a)
        self.b = float(b)
        super().__init__(shape_type)

    def findPerimeter(self):
        perimeter = 2 * (self.a + self.b)
        return perimeter

    def findArea(self):
        area = self.a * self.b
        return area


class Rhombus(TwoDShape):
    def __init__(self, d1, d2, a, shape_type="Rhombus"):
        self.d1 = float(d1)
        self.d2 = float(d2)
        self.a = float(a)
        super().__init__(shape_type)

    def findPerimeter(self):
        perimeter = 4 * self.a
        return perimeter

    def findArea(self):
        area = (self.d1 * self.d2) / 2
        return area


class ThreeDShape(Shape):
    def __init__(self, shape_type=None):
        self.dimension = "ThreeD"
        super().__init__(shape_type)

    def findArea(self):
        pass

    def findVolume(self):
        pass


class Sphere(ThreeDShape):
    def __init__(self, r, shape_type="Sphere"):
        self.r = float(r)
        super().__init__(shape_type)

    def findArea(self):
        area = 4 * PI * (self.r ** 2)
        return area

    def findVolume(self):
        volume = (4 * PI * (self.r ** 3)) / 3
        return volume


class Cylinder(ThreeDShape):
    def __init__(self, r, h, shape_type="Cylinder"):
        self.r = float(r)
        self.h = float(h)
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
    def __init__(self, a, shape_type="Cube"):
        self.a = float(a)
        super().__init__(shape_type)

    def findArea(self):
        area_square = self.a ** 2
        area = 6 * area_square
        return area

    def findVolume(self):
        volume = self.a ** 3
        return volume


class Pyramid(ThreeDShape):
    def __init__(self, h, base_obj=TwoDShape, shape_type="Pyramid"):
        self.h = float(h)
        self.base_shape = base_obj
        super().__init__(shape_type)

    def findArea(self):
        area_base = self.base_shape.findArea()

        if self.base_shape.shape_type == "Rectangle":

            # print("rectangle")

            apothem_side_a = RightTriangle(self.base_shape.b/2, self.h, 0).findHypotenuse()
            apothem_side_b = RightTriangle(self.base_shape.a/2, self.h, 0).findHypotenuse()
            triangles_area = 2 * (Triangle(self.base_shape.a, apothem_side_a, 0, 0).findArea()) + \
                             2 * (Triangle(self.base_shape.b, apothem_side_b, 0, 0).findArea())

        if self.base_shape.shape_type == "Square" or "Rhombus":

            # print("square")

            apothem_side = RightTriangle(self.base_shape.a/2, self.h, 0).findHypotenuse()
            triangles_area = 4 * (Triangle(self.base_shape.a, apothem_side, 0, 0).findArea())

        area = area_base + triangles_area
        return area

    def findVolume(self):
        area_base = self.base_shape.findArea()
        volume = (area_base * self.h) / 3
        return volume
