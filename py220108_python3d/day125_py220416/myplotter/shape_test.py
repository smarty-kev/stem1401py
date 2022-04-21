from shape_entities import *

square = Square(5)
print(square.findArea())
print(square.findPerimeter())
print(square.shape_type)


pyramid = Pyramid(5, square)
pyramid.findArea()