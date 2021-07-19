"""
Tkinter
place a label widget
image label with .gif, .png
"""

from tkinter import *

root = Tk()
root.title('Python GUI - Label image')

# root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

# create a label with image in .png
bgimg2 = PhotoImage(file='./img/diona.png')

# bgimg2.zoom(2)
# bgimg2.subsample(2)
# label2 = Label(root, image=bgimg2, width=1600, height=900)

label2 = Label(root, image=bgimg2)
label2.pack()


root.mainloop()