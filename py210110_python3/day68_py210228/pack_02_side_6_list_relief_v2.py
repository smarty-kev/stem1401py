"""
"flat", "groove", "raised","ridge", "solid", "sunken"
"""

from tkinter import *

root = Tk()
# root.geometry('640x480+0+0')
root.config(bg='#ddddff')


reliefs = ["flat", "groove", "raised","ridge", "solid", "sunken"]
"""
label1 = Label(root, text='flat', relief='flat')
label2 = Label(root, text='groove', relief='groove')
label3 = Label(root, text='raised', relief='raised')
label4 = Label(root, text='ridge', relief='ridge')
label5 = Label(root, text='solid', relief='solid')
label6 = Label(root, text='sunken', relief='sunken')


label1.pack(side=LEFT, padx=10)
label2.pack(side=LEFT, padx=10)
label3.pack(side=LEFT, padx=10)
label4.pack(side=LEFT, padx=10)
label5.pack(side=LEFT, padx=10)
label6.pack(side=LEFT, padx=10)
"""

for relief in reliefs:
    Label(root, text=relief, relief=relief).pack(side=LEFT, padx=5, ipadx=10)

root.mainloop()