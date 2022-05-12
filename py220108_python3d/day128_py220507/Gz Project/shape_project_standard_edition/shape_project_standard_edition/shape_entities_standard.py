"""
standard edition shape entities
2D shapes : Rectangle, Square, Triangle, and Circle
3D shapes : Cube, Sphere
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

    def Perimeter(self):
        pass

    def Area(self):
        pass


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

    def Area(self):
        pass

    def Volume(self):
        pass


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
