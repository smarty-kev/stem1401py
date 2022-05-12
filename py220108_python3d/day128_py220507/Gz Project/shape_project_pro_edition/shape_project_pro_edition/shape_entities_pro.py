"""
Pro edition shape entities
2D shapes : Rectangle, Square, Triangle, Circle, Parallelogram, Oval, Rhombus, and Right Triangle
3D shapes : Cube, Sphere, Cylinder, and Pyramid
"""

PI = 3.1415926


class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type


class StandardEdition(Shape):
    pass


class TwoDShapeStandard(StandardEdition):
    def __init__(self, shape_type):
        super().__init__(shape_type)


class Rectangle(TwoDShapeStandard):
    def __init__(self, length, width, shape_type="Rectangle"):
        self.length = length
        self.width = width
        super().__init__(shape_type)

    def Perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter

    def Area(self):
        area = self.length * self.width
        return area


class Square(TwoDShapeStandard):
    def __init__(self, side, shape_type="Square"):
        self.side = side
        super().__init__(shape_type)

    def Perimeter(self):
        perimeter = 4 * self.side
        return perimeter

    def Area(self):
        area = self.side ** 2
        return area


class Triangle(TwoDShapeStandard):
    def __init__(self, base, side, side2, height, shape_type="Triangle"):
        self.base = base
        self.side = side
        self.side2 = side2
        self.height = height
        super().__init__(shape_type)

    def Perimeter(self):
        perimeter = self.base + self.side + self.side2
        return perimeter

    def Area(self):
        area = self.base * self.height / 2
        return area


class Circle(TwoDShapeStandard):
    def __init__(self, radius, shape_type="Circle"):
        super().__init__(shape_type)
        self.radius = radius

    def Perimeter(self):
        perimeter = 2 * self.radius * PI
        return perimeter

    def Area(self):
        area = PI * self.radius ** 2
        return area


class ThreeDShapeStandard(StandardEdition):
    def __init__(self, shape_type):
        super().__init__(shape_type)


class Cube(ThreeDShapeStandard):
    def __init__(self, side, shape_type="Cube"):
        self.side = side
        super().__init__(shape_type)

    def Area(self):
        area = 6 * self.side ** 2
        return area

    def Volume(self):
        volume = self.side ** 3
        return volume


class Sphere(ThreeDShapeStandard):
    def __init__(self, radius, shape_type="Sphere"):
        self.radius = radius
        super().__init__(shape_type)

    def Area(self):
        area = 4 * PI * self.radius ** 2
        return area

    def Volume(self):
        volume = (4 * PI * self.radius ** 3) / 3
        return volume


class ProEdition(Shape):
    pass


class TwoDShapePro(ProEdition):
    def __init__(self, shape_type):
        super().__init__(shape_type)


class Parallelogram(TwoDShapePro):
    def __init__(self, base, side, shape_type="Parallelogram"):
        self.base = base
        self.side = side
        super().__init__(shape_type)

    def Perimeter(self):
        perimeter = 2 * (self.base + self.side)
        return perimeter

    def Area(self):
        area = self.base * self.side
        return area


class Oval(TwoDShapePro):
    def __init__(self, major_radius, minor_radius, shape_type="Oval"):
        self.major_radius = major_radius
        self.minor_radius = minor_radius
        super().__init__(shape_type)

    def Perimeter(self):
        h = (self.major_radius - self.minor_radius) ** 2 / (self.major_radius + self.minor_radius) ** 2
        perimeter = PI * (self.major_radius + self.minor_radius) * (
                1 + h * 0.25 + (h ** 2) * (1 / 64) + (h ** 3) * (1 / 256) + (h ** 4)
                * (25 / 16384) + (h ** 5) * (49 / 65536) + (h ** 6) * (441 / 1048576))
        return perimeter

    def Area(self):
        area = PI * self.major_radius * self.minor_radius
        return area


class Rhombus(TwoDShapePro):
    def __init__(self, short_diagonal, long_diagonal, side, shape_type="Rhombus"):
        self.short_diagonal = short_diagonal
        self.long_diagonal = long_diagonal
        self.side = side
        super().__init__(shape_type)

    def Perimeter(self):
        perimeter = 4 * self.side
        return perimeter

    def Area(self):
        area = (self.short_diagonal * self.long_diagonal) / 2
        return area


class RightTriangle(TwoDShapePro):
    def __init__(self, leg, leg2, hypotenuse, shape_type="RightTriangle"):
        self.leg = leg
        self.leg2 = leg2
        self.hypotenuse = hypotenuse
        super().__init__(shape_type)
    def Perimeter(self):
        perimeter = self.leg + self.leg2 + self.hypotenuse
        return perimeter

    def Area(self):
        area = (self.leg * self.leg2) / 2
        return area


class ThreeDShapePro(ProEdition):
    def __init__(self, shape_type):
        super().__init__(shape_type)


class Pyramid(ThreeDShapePro):
    def __init__(self, base_area, base_perimeter, apothem, height, shape_type="Pyramid"):
        self.base_area = base_area
        self.base_perimeter = base_perimeter
        self.apothem = apothem
        self.height = height
        super().__init__(shape_type)

    def Area(self):
        area = self.base_area + (1 / 2) * self.base_perimeter * self.apothem
        return area

    def Volume(self):
        volume = (self.base_area * self.height) / 3
        return volume


class Cylinder(ThreeDShapePro):
    def __init__(self, radius, height, shape_type="Cylinder"):
        self.radius = radius
        self.height = height
        super().__init__(shape_type)

    def Area(self):
        area = 2 * (self.radius ** 2 * PI) + self.radius * 2 * PI * self.height
        return area

    def Volume(self):
        volume = (self.radius ** 2 * PI) * self.height
        return volume


class Color:
    def __init__(self, color):
        self.color = color

    def fill(self):
        while True:
            input_color = input("Which color do you want to fill the shape with (Enter the number beside the color):\n"
                            "[1] red\n"
                            "[2] blue\n"
                            "[3] yellow\n"
                            "[4] green\n"
                            "[5] white\n"
                            "[6] black\n")

            if input_color == '1':
                self.color = 'red'
                return self.color
            elif input_color == '2':
                self.color = 'blue'
                return self.color
            elif input_color == '3':
                self.color = 'yellow'
                return self.color
            elif input_color == '4':
                self.color = 'green'
                return self.color
            elif input_color == '5':
                self.color = 'white'
                return self.color
            elif input_color == '6':
                self.color = 'black'
                return self.color
