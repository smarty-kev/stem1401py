"""
Tkinter
place a label widget
display a jpg
"""

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Python GUI - Label image')
root.configure(bg='#ddddff')

# create a label with image in .jpg
img_obj = Image.open("./img/xiao.jpg")

bgimg = ImageTk.PhotoImage(img_obj)
label1 = Label(root, image=bgimg)
label1.pack()

root.mainloop()
