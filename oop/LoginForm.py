from tkinter import *
root = Tk()
root.geometry("800x600")
root.title("Login Form")

Label(root, text ="Welcome to my Login Form", font = "lucida 20 bold").grid(row = 0, column = 0)

f1 = Frame(root, bg="grey", borderwidth= 2, relief=SUNKEN).grid()

label1 = Label(f1, text = "Username :").grid(pady= 5)
label2 = Label(f1, text = "password :").grid(pady = 5)
E1 = Entry(f1, textvariable = "username").grid(pady = 5)
E2 = Entry(f1, textvariable = "password").pack(pady = 5)

Button(f1, text = "Login", font = "comicsansms 10 bold").pack(pady = 5)

root.mainloop()