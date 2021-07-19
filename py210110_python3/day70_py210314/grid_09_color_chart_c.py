"""
grid layout
color chart
for loop
"""
from tkinter import *
root = Tk()
# root.geometry('640x480+200+200')
root.geometry('+400+300')
root.config(bg='#ddddff')
root.title('Python GUI - Grid')
COLORS = ("red", "orange", "yellow", "green","cyan", "blue", "purple")
for index in range(len(COLORS)):
    # create text label
    label_left = Label(root, text=COLORS[index], relief='groove', width=20, padx=20, pady=20)
    label_left.grid(row= index,  column= 0)
    # create color label
    label_right = Label(root, bg=COLORS[index], padx=80, pady=20)
    label_right.grid(row=index, column=1)
root.mainloop()