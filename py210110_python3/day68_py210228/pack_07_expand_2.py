"""
Layout manager:  pack()
option - expand
expand = True, False
"""
from tkinter import *
root = Tk()
root.title('Python GUI - pack fill')
root.geometry('640x480+0+0')
root.config(bg='#ddddff')
label1 = Label(root, text='Java 1', font=('Arial', 20), fg='red')
label2 = Label(root, text='Python 2',bg='yellow', font=('Arial', 20))
label3 = Label(root, text='Web 3', font=('Arial', 20), fg='white', bg='blue')
label1.pack(side = LEFT, fill = Y)
label2.pack(expand=True)
label3.pack(fill = X)
# label2.pack()
# label3.pack(fill = X, expand=True)
root.mainloop()