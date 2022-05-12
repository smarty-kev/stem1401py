"""
client app for standard edition
"""

from plotter_standard import *
from shape_entities_standard import *

menu = ("Please enter the shape that you want the parameters:\n"
        "2D shapes\n"
        "[1] Rectangle\n"
        "[2] Square\n"
        "[3] Triangle\n"
        "[4] Circle\n"
        "3D shapes\n"
        "[5] Cube\n"
        "[6] Sphere\n"
        "Enter 'Exit' to quit")


def main():
    while True:
        print(menu)
        menu_input = input('Now, enter the choice:')
        if menu_input == '1':
            rectangle = Rectangle(int(input('Please enter the width of the rectangle:')),
                                  int(input('Please enter the height of the rectangle:')))
            Plotter.plotShapes(Rectangle, rectangle)

        if menu_input == '2':
            square = Square(int(input('Please enter one side of the square:')))
            Plotter.plotShapes(Square, square)

        if menu_input == '3':
            triangle = Triangle(int(input('Please enter the base of the triangle:')),
                                int(input('Please enter one of the sides of the triangle:')),
                                int(input('Please enter the other side of the triangle:')),
                                int(input('Please enter the height of the triangle:')))
            Plotter.plotShapes(Triangle, triangle)

        if menu_input == '4':
            circle = Circle(int(input('Please enter the radius of the circle:')))
            Plotter.plotShapes(Circle, circle)

        if menu_input == '5':
            cube = Cube(int(input('Please enter one side of the cube:')))
            Plotter.plotShapes(Cube, cube)

        if menu_input == '6':
            sphere = Sphere(int(input('Please enter the radius of the sphere:')))
            Plotter.plotShapes(Sphere, sphere)

        if menu_input == 'Exit' or menu_input == 'exit':
            break
main()
