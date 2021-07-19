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

def printInfo1():
    print(txt.get())
def printInfo2():
    print(rdbtn2["text"])

root = Tk()
root.title("Python GUI - Radiobutton")
root.geometry("640x480+300+200")
root.config(bg="#ddddff")

# Radiobutton
txt = StringVar()
txt.set("Mage")
rdbtn = Radiobutton(root, command=printInfo1, textvariable=txt)
rdbtn.pack()

rdbtn2 = Radiobutton(root, text="Warrior", command=printInfo2)
rdbtn2.pack()


# list all options
# print(rdbtn.keys())
for i in rdbtn.keys():
    # print(i)
    pass

# main program
root.mainloop()
