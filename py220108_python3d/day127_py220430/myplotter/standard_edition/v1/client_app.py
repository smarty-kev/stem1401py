"""
client app
user interface = cml
"""

from plotter import *


# shape name
two_d_shapes = ["Circle", "Rectangle", "Square", "Triangle", "Right Triangle", "Oval", "Parallelogram", "Rhombus"]
three_d_shapes = ["Cube", "Sphere", "Cylinder", "Pyramid"]


# main menu:
main_menu = "Main Menu\n" \
            "Plot Shape : [1]\n" \
            "Color Shape: [2]\n" \
            "Exit       : [exit]\n"


# plot shape menu
plot_shape_menu = "Shape Menu\n"
plot_shape_menu += "2D Shapes:\n"
key = 1
for shape in two_d_shapes:
    plot_shape_menu += "{:<14} : ".format(shape)  # 14 is longest length of a shape name (Right Triangle)
    plot_shape_menu += f"[{key}]\n"
    key += 1
plot_shape_menu += "3D Shapes:\n"
for shape in three_d_shapes:
    plot_shape_menu += "{:<14} : ".format(shape)
    plot_shape_menu += f"[{key}]\n"
    key += 1
plot_shape_menu += "Return to main menu : [exit]"


# color menu
color_main_menu = None


def main():
    my_plotter = MyPlotter()
    while True:
        # 2d menu
        print(main_menu)
        main_menu_input = input("<<here>> : ")
        if main_menu_input == "exit":
            print("Exiting Plotter...")
            break
        if main_menu_input == "1":
            while True:
                print(plot_shape_menu)
                shape_menu_input = input("<<here>> : ")
                if shape_menu_input == "1":
                    print("Circle Parameters : radius")
                    circle = Circle(input("radius : "))

                    print("\n")
                    my_plotter.plotShape(circle)

                if shape_menu_input == "2":
                    print("Rectangle Parameters : a, b")
                    rectangle = Rectangle(input("a : "),
                                          input("b : "))

                    print("\n")
                    my_plotter.plotShape(rectangle)

                if shape_menu_input == "3":
                    print("Square Parameters : a")
                    square = Square(input("a : "))

                    print("\n")
                    my_plotter.plotShape(square)

                if shape_menu_input == "4":
                    print("Triangle Parameters : base, h, a, b")
                    triangle = Triangle(input("base : "),
                                        input("h : "),
                                        input("a : "),
                                        input("b : "))

                    print("\n")
                    my_plotter.plotShape(triangle)

                if shape_menu_input == "5":
                    print("Cube Parameters : a")
                    cube = Cube(input("a : "))

                    print("\n")
                    my_plotter.plotShape(cube)

                if shape_menu_input == "6":
                    print("Sphere Parameters : radius")
                    sphere = Sphere(input("radius : "))

                    print("\n")
                    my_plotter.plotShape(sphere)

                if shape_menu_input == "exit":
                    break
        if main_menu_input == "2":
            pass


# main program
if __name__ == "__main__":
    main()
