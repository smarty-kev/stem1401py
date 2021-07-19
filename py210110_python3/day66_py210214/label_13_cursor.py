"""
Tkinter

Cursors

"arrow"
"circle"
"clock"
"cross"
"dotbox"
"exchange"
"fleur"
"heart"
"heart"
"man"
"mouse"
"pirate"
"plus"
"shuttle"
"sizing"
"spider"
"spraycan"
"star"
"target"
"tcross"
"trek"
"watch"
"""
from tkinter import *

root = Tk()
root.title('Python GUI - Cursors')
root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

# create a label widget
label1 = Label(root, text='Cursor exchange',
               padx=30, pady=15,
               font = "Helnetic 20",
               bg='#72EFAA', fg='black',
               cursor='exchange')
label1.pack()
# create a label widget
label2 = Label(root, text='Cursor circle',
               padx=30, pady=15,
               font = "Helnetic 20",
               bg='#72AAEF', fg='black',
               cursor='circle')
label2.pack()
# create a label widget
label3 = Label(root, text='Cursor watch',
               padx=30, pady=15,
               font = "Helnetic 20",
               bg='#72EFAA', fg='black',
               cursor='watch')
label3.pack()
# create a label widget
label4 = Label(root, text='Cursor heart',
               padx=30, pady=15,
               font = "Helnetic 20",
               bg='#72AAEF', fg='black',
               cursor='heart')
label4.pack()
# create a label widget
label5 = Label(root, text='Cursor plus',
               padx=30, pady=15,
               font = "Helnetic 20",
               bg='#72EFAA', fg='black',
               cursor='plus')
label5.pack()
# create a label widget
label6 = Label(root, text='Cursor cross',
               padx=30, pady=15,
               font = "Helnetic 20",
               bg='#72EFAA', fg='black',
               cursor='cross')
label6.pack()
root.mainloop()