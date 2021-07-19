"""
Tkinter
using grid layout
columnconfig()
"""
from tkinter import *
root = Tk()
root.geometry('+200+200')
# root.geometry('640x480+200+200')
root.title('Python GUI - grid')
root.config(bg='#ddddff')
Label(root,text="(0,0)",padx=20, pady=15).grid(row=0,column=0)
Label(root,text="(0,1)",padx=20, pady=15, bg='yellow').grid(row=0,column=1)
Label(root,text="(1,2)",padx=20, pady=15).grid(row=1,column=2)
Label(root,text="(1,3)",padx=20, pady=15, bg='yellow').grid(row=1,column=3)
Label(root,text="(2,0)",padx=20, pady=15, bg='yellow').grid(row=2,column=0,ipadx=30)
Label(root,text="(2,1)",padx=20, pady=15).grid(row=2,column=1)
Label(root,text="(2,2)",padx=20, pady=15, bg='yellow').grid(row=2,column=2)
Label(root,text="(2,3)",padx=20, pady=15).grid(row=2,column=3)
# pay attention to the object
# columnconfigure is the method of a container
root.columnconfigure(0, weight=1)
root.columnconfigure(2, weight=2)
# distribution of space width for columns by weight
# i.e 1/(1+2),  2/(1+2)
root.mainloop()