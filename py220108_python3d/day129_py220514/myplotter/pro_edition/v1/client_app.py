"""
client app
user interface = cml
"""

from plotter import *


# shape name
two_d_shapes = ["Circle", "Rectangle", "Square", "Triangle", "Right Triangle", "Oval", "Parallelogram", "Rhombus"]
three_d_shapes = ["Cube", "Sphere", "Cylinder", "Pyramid"]


# main menu:
main_menu = "\n===Main Menu===\n" \
            "Plot Shape : [1]\n" \
            "Color Shape: [2]\n" \
            "Exit       : [x]\n"


# plot shape menu
plot_shape_menu = "\n===Shape Menu===\n"
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
plot_shape_menu += "Return to main menu : [x]"


# color menu
color_main_menu = "\n===Coloring Menu===\n" \
                  "Default Colors : [1]\n" \
                  "Hex Colors     : [2]\n" \
                  "Return to main menu: [x]\n"

# default color menu
default_colors_menu = ""
default_colors = {
    1: "red",
    2: "green",
    3: "blue",
    4: "yellow",
    5: "orange",
    6: "purple",
    7: "white",
    8: "black",
}
for key in default_colors:
    default_colors_menu += "{:<7} : [{}]\n".format(default_colors[key].capitalize(), key)


def main():
    my_plotter = MyPlotter()
    while True:
        # 2d menu
        print(main_menu)
        main_menu_input = input("<<here>> : ")
        if main_menu_input == "x":
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
                    print("Right Triangle : a, b, hypotenuse")
                    right_triangle = RightTriangle(input("a : "),
                                                   input("b : "),
                                                   input("hypotenuse : "))

                    print("\n")
                    my_plotter.plotShape(right_triangle)

                if shape_menu_input == "6":
                    print("Oval : r1, r2")
                    oval = Oval(input("r1 : "),
                                input("r2 : "))

                    print("\n")
                    my_plotter.plotShape(oval)

                if shape_menu_input == "7":
                    print("Parallelogram : a, b")
                    parallelogram = Parallelogram(input("a : "),
                                                  input("b : "))

                    print("\n")
                    my_plotter.plotShape(parallelogram)

                if shape_menu_input == "8":
                    print("Rhombus : d1, d2, a")
                    rhombus = Rhombus(input("d1 : "),
                                      input("d2 : "),
                                      input("a : "))

                    print("\n")
                    my_plotter.plotShape(rhombus)

                if shape_menu_input == "9":
                    print("Cube : a")
                    cube = Cube(input("a : "))

                    print("\n")
                    my_plotter.plotShape(cube)

                if shape_menu_input == "10":
                    print("Sphere : r")
                    sphere = Sphere(input("r : "))

                    print("\n")
                    my_plotter.plotShape(sphere)

                if shape_menu_input == "11":
                    print("Cylinder : r, h")
                    cylinder = Cylinder(input("r : "),
                                        input("h : "))

                    print("\n")
                    my_plotter.plotShape(cylinder)

                if shape_menu_input == "12":
                    print("Pyramid : h, BASE_SHAPE")
                    h = input("h : ")
                    print("BASE_SHAPE - Rectangle : [1]")
                    print("BASE_SHAPE - Square or Rhombus : [2]")
                    base_shape_choice = input("Base Shape : ")
                    if base_shape_choice == "1":
                        rectangle = Rectangle(input("a : "),
                                              input("b : "))
                        pyramid = Pyramid(h, rectangle)
                    if base_shape_choice == "2":
                        square_or_rhombus = Square(input("a : "))
                        pyramid = Pyramid(h, square_or_rhombus)

                    print("\n")
                    my_plotter.plotShape(pyramid)

                if shape_menu_input == "x":
                    break
        if main_menu_input == "2":
            if my_plotter.myshapes is []:
                print("You have not plotted any shapes yet. :(")
                break

            print("My Shapes = ", end="")
            key = 1
            for shape in my_plotter.myshapes:
                print(f"{shape.shape_type} : [{key}], ", end="")
                key += 1
            print()
            target_shape = my_plotter.myshapes[int(input("Shape to be colored : "))-1]
            print()

            while True:
                print(color_main_menu)
                color_main_menu_input = input("<<here>> : ")
                if color_main_menu_input == "1":
                    print(default_colors_menu)
                    default_colors_menu_input = input("<<here>> : ")
                    if default_colors_menu_input == "1":
                        my_plotter.fillColor(target_shape, default_colors[1])
                    if default_colors_menu_input == "2":
                        my_plotter.fillColor(target_shape, default_colors[2])
                    if default_colors_menu_input == "3":
                        my_plotter.fillColor(target_shape, default_colors[3])
                    if default_colors_menu_input == "4":
                        my_plotter.fillColor(target_shape, default_colors[4])
                    if default_colors_menu_input == "5":
                        my_plotter.fillColor(target_shape, default_colors[5])
                    if default_colors_menu_input == "6":
                        my_plotter.fillColor(target_shape, default_colors[6])
                    if default_colors_menu_input == "7":
                        my_plotter.fillColor(target_shape, default_colors[7])
                    if default_colors_menu_input == "8":
                        my_plotter.fillColor(target_shape, default_colors[8])
                if color_main_menu_input == "2":
                    print("Please enter a valid hex input (ex: #7dd0d7")
                    hex_color = input("<<here>> : ")
                    my_plotter.fillColor(target_shape, hex_color)
                if color_main_menu_input == "x":
                    break


# main program
if __name__ == "__main__":
    main()
