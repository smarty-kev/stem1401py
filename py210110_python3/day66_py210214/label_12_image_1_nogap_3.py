"""
Tkinter
place a label widget
image label with .gif, .png
does not support .jpg
_tkinter.TclError: couldn't recognize data in image file "./xiao.jpg"
"""
from tkinter import *
root = Tk()
root.title('Python GUI - Label image')
# root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')
# create a label with image in .jpg
bgimg3 = PhotoImage(file='./img/xiao.jpg')
label3 = Label(root, image=bgimg3)
label3.pack()
root.mainloop()