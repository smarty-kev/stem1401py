from tkinter import *


def msg_show():
    label["text"] = "Button Widget"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"


def msg_clear():
    label["text"] = ""
    print(root.cget('bg'))
    label['bg'] = 'SystemButtonFace'


root = Tk()
root.geometry("800x450+200+200")
root.configure(bg="#ddddff")

# labels
label = Label(root)

# buttons
btn1 = Button(root, text="show msg", command=msg_show)
btn2 = Button(root, text="exit", command=root.destroy)
btn3 = Button(root, text="clear message", command=msg_clear)

# grid
label.grid(row=0, column=0, columnspan=2)
btn1.grid(row=1, column=0)
btn1.grid(row=1, column=2)
btn1.grid(row=1, column=1)

root.mainloop()

# """
# button
# clear button
# """
# from tkinter import *
# root = Tk()
# root.geometry('640x480+200+200')
# root.title('Python GUI - grid')
# root.config(bg='#ddddff')
# def msgshow():
#     label['text'] = 'button widget'
#     label['bg'] = 'lightyellow'
#     label['fg'] = 'blue'
# def msgclear():
#     label['text'] = ''
# #create a button
# label = Label(root)
# btn1 = Button(root,text='show msg', command=msgshow)
# btn2 = Button(root,text='close', command=root.destroy)
# btn3 = Button(root,text='clear msg', command=msgclear)
# label.grid(row=0, column=0)
# btn1.grid(row=0, column=1)
# btn2.grid(row=0, column=2)
# btn3.grid(row=0, column=3)
# root.mainloop()