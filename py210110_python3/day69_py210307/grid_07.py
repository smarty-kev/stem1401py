"""
Tkinter
using grid layout
grid()
without sticky, similar to anchor
"""

from tkinter import *


root = Tk()
root.geometry('640x480+200+200')
# root.geometry('+400+300')
root.title('Python GUI - sticky')
root.config(bg='#ddddff')


# Label(root,text="The First",bg="green",fg='white').grid(row=0,column=0,rowspan=2,columnspan=2,sticky="se")
# Label(root,text="The Second",bg="blue",fg='white').grid(row=0,column=2,columnspan=2,sticky="e")

# compare with
Label(root,text="The First",bg="green",fg='white').grid(row=0,column=0,rowspan=2,columnspan=2)
Label(root,text="The Second",bg="blue",fg='white').grid(row=0,column=0,columnspan=2)

Label(root,text="(1,2)").grid(row=1,column=2)
Label(root,text="(1,3)").grid(row=1,column=3)
Label(root,text="(2,0)").grid(row=2,column=0)
Label(root,text="(2,1)").grid(row=2,column=1)
Label(root,text="(2,2)").grid(row=2,column=2)
Label(root,text="(2,3)").grid(row=2,column=3)
root.mainloop()
