from tkinter import *

root = Tk()

root.geometry("655x455")
root.title("Login Page")

def getvals():
    print(f"{uservalue.get(),passvalue.get()}")
    # print(passvalue.get())

user = Label(root, text = "Username :").grid()
password = Label(root, text = "Password :").grid(row = 1)

# user.grid()
# password.grid(row = 1)

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable = uservalue)
passentry = Entry(root, textvariable = passvalue)

userentry.grid(row=0, column = 1)
passentry.grid(row=1, column=1)

Button(text="Submit", command = getvals).grid()


root.mainloop()