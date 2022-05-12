"""
client app for standard edition
"""

from plotter_pro import *
from shape_entities_pro import *

menu = ("Please enter the shape that you want the parameters:\n"
        "=======2D shapes=======\n"
        "[1] Rectangle\n"
        "[2] Square\n"
        "[3] Triangle\n"
        "[4] Circle\n"
        "[5] Parallelogram\n"
        "[6] Oval\n"
        "[7] Rhombus\n"
        "[8] Right Triangle\n"
        "=======3D shapes=======\n"
        "[9] Cube\n"
        "[10] Sphere\n"
        "[11] Pyramid\n"
        "[12] Cylinder\n"
        "=======Fill Color========\n"
        "[13] Fill the shape with a color\n"
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
            parallelogram = Parallelogram(int(input('Please enter one side of the parallelogram:')),
                                          int(input('Please enter the base of the parallelogram:')))
            Plotter.plotShapes(Parallelogram, parallelogram)

        if menu_input == '6':
            oval = Oval(int(input('Please enter the minor radius of the oval:')),
                        int(input('Please enter the major radius of the oval:')))
            Plotter.plotShapes(Oval, oval)

        if menu_input == '7':
            rhombus = Rhombus(int(input('Please enter the short diagonal of the rhombus:')),
                              int(input('Please enter the long diagonal of the rhombus:')),
                              int(input('Please enter one side of the rhombus:')))
            Plotter.plotShapes(Rhombus, rhombus)

        if menu_input == '8':
            right_triangle = RightTriangle(int(input('Please enter one leg of the right triangle:')),
                                           int(input('Please enter the other leg of the right triangle:')),
                                           int(input('Please enter the hypotenuse of the right triangle:')))
            Plotter.plotShapes(RightTriangle, right_triangle)

        if menu_input == '9':
            cube = Cube(int(input('Please enter one side of the cube:')))
            Plotter.plotShapes(Cube, cube)

        if menu_input == '10':
            sphere = Sphere(int(input('Please enter the radius of the sphere:')))
            Plotter.plotShapes(Sphere, sphere)

        if menu_input == '11':
            pyramid = Pyramid(int(input('Please enter the base area of the pyramid:')),
                              int(input('Please enter the base perimeter of the pyramid:')),
                              int(input('Please enter the apothem of the pyramid:')),
                              int(input('Please enter the height of the pyramid:')))
            Plotter.plotShapes(Pyramid, pyramid)

        if menu_input == '12':
            cylinder = Cylinder(int(input('Please enter the radius of the cylinder:')),
                                int(input('Please enter the height of the cylinder:')))
            Plotter.plotShapes(Cylinder, cylinder)

        if menu_input == '13':
            shape_color = Color
            shape_color.fill(shape_color)
            print(f'The shape is now of color {shape_color.color}')
        if menu_input == 'Exit' or menu_input == 'exit':
            break


main()
