"""
place()
https://www.geeksforgeeks.org/python-place-method-in-tkinter/
"""
# Importing tkinter module
from tkinter import *
from tkinter.ttk import *
# creating Tk window
root = Tk()
# setting geometry of tk window
root.geometry("200x200")
# button widget
b2 = Button(root, text="Button")
b2.pack(fill=X, expand=True, ipady=10)
# button widget
b1 = Button(root, text="Click me !")
# This is where b1 is placed inside b2 with in_ option
b1.place(in_=b2, relx=0.5, rely=0.5, anchor=CENTER)
# label widget
l = Label(root, text="I'm a Label")
l.place(anchor=NW)
# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
mainloop()