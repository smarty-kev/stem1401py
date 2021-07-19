"""
[Homework]
Date: 2021-04-10
Design and write program for a login form
Requirements:
A GUI interface
Preset the username is 'admin' and the password is '123456'
User may input username
User may input password, and the password should show mask char ('*') instead
If the user's input matches the presetting, then the program shows a text message (info) box with the words 'login successfully!'
otherwise, the program shows a text message (error) box with the words 'wrong username or password!'
Due date: by the end of next Friday
"""

# tkinter module
from tkinter import *
from tkinter.ttk import Separator
from tkinter import messagebox as msg

# username & password
username = "admin"
password = "123456"


# login function
def login():
    user_input_username = accountE.get()
    user_input_password = passwordE.get()
    if username == user_input_username and password == user_input_password:
        msg.showinfo("Successful Login", "Welcome Back!")
    else:
        msg.showerror("Unsuccessful Login", "Wrong Credentials!")


# widget specifications
root = Tk()
root.title("Kevin L. | Login Form V2")
root.geometry("375x245+200+200")
root.config(bg="gray85")
root.resizable(1, 1)


# title label
title = Label(text="Login Form", font=("Helvetica", 24), bg="gray85")
title.grid(columnspan=2, pady=(8, 0))

# sep 1
sep1 = Separator(root, orient=HORIZONTAL)
sep1.grid(sticky=N, pady=5)

# username
accountL = Label(root, text="Account ")
accountL.grid(row=2,padx=(50,5), sticky='e')
accountE = Entry(root)
accountE.grid(row=2, column=1, padx=(5, 50))

# password
passwordL = Label(root, text="Password ")
passwordL.grid(row=3,padx=(50,5), sticky='e')
passwordE = Entry(root, show='*')
passwordE.grid(row=3, column=1, padx=(5, 50))

# login button
loginBtn = Button(text="Login", command=login)
loginBtn.grid(padx=5, sticky='e')

# sep 2
sep2 = Separator(root, orient=HORIZONTAL)
sep2.grid(sticky=N, pady=5)

# exit button
exitBtn = Button(text="Quit", command=root.destroy)
exitBtn.grid(row=4, column=1, padx=5, pady=5, sticky='w')

# footnote
footnoteL = Label(root, text="Kevin L. 17 April 2021", font=("Helvetica", 16), bg="gray85")
footnoteL.grid(columnspan=2, pady=(8, 0))

# mainloop
root.mainloop()
