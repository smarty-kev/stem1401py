from shape_entities import *


square = Square(5)
# print(square.shape_type)
# print(square.findArea())
# print(square.findPerimeter())
# print()


rectangle = Rectangle(4, 5)
# print(rectangle.shape_type)
# print(rectangle.findArea())
# print(rectangle.findPerimeter())
# print()


# print("Square Pyramid")
pyramid = Pyramid(5, square)
# print(pyramid.findArea())
# print(pyramid.findVolume())
# print()

# print("Rectangle Pyramid")
pyramid = Pyramid(5, rectangle)
# print(pyramid.findArea())
# print(pyramid.findVolume())
# print()
