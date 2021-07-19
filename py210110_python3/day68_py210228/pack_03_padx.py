"""

"""


from tkinter import *

root = Tk()
# root.geometry('640x480+0+0')
root.config(bg='#ddddff')

label1 = Label(root, text='Python')
label2 = Label(root, text='Java',bg='yellow', font=(40))
label3 = Label(root, text='Web')
label4 = Label(root, text='Database',bg='yellow', font=(40))


label1.pack(side=LEFT, padx=20, pady=40)
label2.pack(side=LEFT, padx=20, pady=40)
label3.pack(side=LEFT, padx=20, pady=40)
label4.pack(side=LEFT, padx=20, pady=40)

root.mainloop()
