"""
place_02.py
layout manager
place

width, height
"""

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Python GUI - place')
root.geometry('640x480+300+300')
root.config(bg='#ddddff')

dog = ImageTk.PhotoImage(Image.open("img/dog.jpg"))
dog2 = ImageTk.PhotoImage(Image.open("img/dog2.jpg"))

p1 = Label(root, image = dog)
p2 = Label(root, image =dog2)

p1.place(x=20, y=20, width = 200, height = 200)
p2.place(x=300, y=200, width = 150, height = 150)

root.mainloop()
