"""
radiobutton widget

Class 1. styling
activebackground
activeforeground
background
bd
bg
borderwidth
disabledforeground
fg
font
foreground
height
highlightbackground
highlightcolor
highlightthickness
offrelief
overrelief
relief
selectcolor
underline
width
wraplength


Class 2. layout
anchor
justify
padx
pady

Class 3. features (functionality)
text
textvariable
bitmap (context)
compound
command
cursor
image
selectimage
state
takefocus
tristateimage
tristatevalue
value
variable


Class 4. other/misc
indicatoron
"""

from tkinter import *


def printOption():
    print(var.get())
    txt.set(var.get())


root = Tk()
root.title("Python GUI - Radiobutton")
root.geometry("640x480+300+200")
root.config(bg="#ddddff")

# Radiobutton
# var = StringVar()
var = IntVar()
# var.set(None)
var.set(2)
rdbtn = Radiobutton(root, text="Mage", command=printOption, variable=var, value=1)
rdbtn.pack()

rdbtn2 = Radiobutton(root, text="Warrior", command=printOption, variable=var, value=2)
rdbtn2.pack()

rdbtn3 = Radiobutton(root, text="Archer", command=printOption, variable=var, value=3)
rdbtn3.pack()

# use selected option
txt = StringVar()
txt.set("Please choose a role.")
label1 = Label(root, textvariable=txt, font=(None, 20))
label1.pack()

# main program
root.mainloop()
