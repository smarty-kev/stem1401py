from tkinter import *
import random
from tkinter import messagebox as msg


def verify():

    randomNumber = random.randint(10000, 99999)

    verifyWindow = Tk()
    verifyWindow.title("Verification")

    numberLabel = Label(verifyWindow, text=randomNumber)
    numberLabel.pack()

    number = IntVar()

    numberE = Entry(verifyWindow, textvariable=number)
    numberE.pack()

    confirm = Button(verifyWindow, text="Confirm", command=lambda : confirmVerification(verifyWindow, number.get(), randomNumber))
    confirm.pack()


def confirmVerification(window, num, randomNum):
    if int(num) == randomNum:
        global verified
        verified = True
        window.destroy()
    else:
        msg.showerror("Error", "Number does not match")


def register():
    if verified == True:
        if password.get() == passwordconfirm.get():
            msg.showinfo("Success", "Login Success!")
        else:
            msg.showerror("Error", "Passwords do not match!")
    else:
        msg.showerror("Error", "Please verify you are human")


def reset():
    username.set("")
    password.set("")
    passwordconfirm.set("")



root = Tk()
root.title("Registration")
root.geometry("640x480")

verified = False

label = Label(root, text="File Transfer\nAccount registration", font=("Roman", 40))
label.grid(row=0, columnspan=3)

usernameL = Label(root, text="Username:")
usernameL.grid(row=1, columnspan=2)

username = StringVar()
usernameE = Entry(root, textvariable=StringVar)
usernameE.grid(row=1, column=2)

passwordL = Label(root, text="Password:")
passwordL.grid(row=2, columnspan=2)

password = StringVar()
passwordE = Entry(root, textvariable=StringVar, show="*")
passwordE.grid(row=2, column=2)

passwordConfirmationL = Label(root, text="Please confirm your password:")
passwordConfirmationL.grid(row=3, columnspan=2)

passwordconfirm = StringVar()
passwordConfirmationE = Entry(root, textvariable=StringVar, show="*")
passwordConfirmationE.grid(row=3, column=2)

verificationLabel = Label(root, text="Please verify you are a human below")
verificationLabel.grid(row=4, columnspan=3)

verificationButton = Button(root, text="Verify", command=verify)
verificationButton.grid(row=5, columnspan=3)

confirmationButton = Button(root, text="Register", command=register)
confirmationButton.grid(row=6, column=0)

resetButton = Button(root, text="Clear all", command=reset)
resetButton.grid(row=6, column=1)

exitButton = Button(root, text="Exit", command=root.destroy)
exitButton.grid(row=6, column=2)

root.mainloop()