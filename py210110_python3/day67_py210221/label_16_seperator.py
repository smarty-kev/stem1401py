"""

"""

from tkinter import *
from tkinter.ttk import Separator


# main program
root = Tk()
root.title('Python GUI - Clock')
root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

# create a label for title
mytitle = 'Tkinter Separator'
label1 = Label(root, text=mytitle,
               padx=30, pady=15,
               font="Helnetic 14",
               bg='#72EFAA', fg='black')
label1.pack(padx=10, pady=10)

# sep
sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X)

# create a label for content
mycontent = '''The tkinter package ('Tk interface') is the standard Python interface 
to the Tk GUI toolkit. Both Tk and tkinter are available on most Unix platforms, 
as well as on Windows systems. (Tk itself is not part of Python; 
it is maintained at ActiveState.)'''
label2 = Label(root, text=mycontent)
label2.pack(padx=10, pady=10)

root.mainloop()