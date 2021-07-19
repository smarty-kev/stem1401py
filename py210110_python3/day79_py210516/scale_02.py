"""
Scale
basic usage of Scale
get value via Scale object
"""
from tkinter import *


def changeNum(source):
    print("change value to", var1.get())


def get_Num():
    print("get scale", var1.get())


def set_Num():
    var1.set(5) # hard code
    print("set scale", var1.get())


# main program
root = Tk()
root.title("Python GUI - Scale")
root.geometry("640x480")
# label
label = Label(root, text="Scale binding a variable", bg="lightyellow", width=30)
label.pack()


var1 = IntVar()
scale1 = Scale(root, from_=0, to=10, orient=HORIZONTAL, variable=var1, command=changeNum)
scale1.pack()


Button(root, text="Get Value", width=20, command=set_Num).pack()
Button(root, text="Set Value", width=20, command=set_Num()).pack()
root.mainloop()
