"""
Button
command
"""

from tkinter import *


def changecolor(color):
    root.config(bg=color)


# main program
root = Tk()
root.title('Python GUI - Button and Lambda')
root.geometry('300x200+300+200')

color1 = input("enter a color: ")
# color1 = "yellow"
color2 = "blue"
btn1 = Button(root, text=color1, command=lambda: changecolor(color1))
btn2 = Button(root, text='Blue', command=lambda: changecolor(color2))
btn3 = Button(root, text='Exit', command=root.destroy)

btn3.pack(anchor=S, side=RIGHT)
btn2.pack(anchor=S, side=RIGHT)
btn1.pack(anchor=S, side=RIGHT)


root.mainloop()
