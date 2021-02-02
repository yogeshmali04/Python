from tkinter import *

root = Tk()

root.geometry("700x500")
root.title("Pycharm IDE")

username = StringVar()
password = StringVar()

def myfunc():
    print("This is menu")

mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff = 0)
m1.add_command(label = "Save", command = myfunc)
m1.add_command(label = "save as", command = myfunc)
m1.add_separator()
m1.add_command(label = "New", command = myfunc)
m1.add_command(label = "New Project", command = myfunc)
root.config(menu = mainmenu)

mainmenu.add_cascade(label = "File", menu = m1)

# mainmenu = Menu(root)
m2 = Menu(mainmenu, tearoff = 0)
m2.add_command(label = "cut", command = myfunc)
m2.add_command(label = "copy", command = myfunc)
# m2.add_separator()
m2.add_command(label = "paste", command = myfunc)
m2.add_command(label = "delete", command = myfunc)
root.config(menu = mainmenu)

mainmenu.add_cascade(label = "Edit", menu = m2)

# mainmenu = Menu(root)
m3 = Menu(mainmenu, tearoff = 0)
m3.add_command(label = "Run frame", command = myfunc)
m3.add_command(label = "Debug frame", command = myfunc)
m3.add_separator()
m3.add_command(label = "Run", command = myfunc)
m3.add_command(label = "Debug", command = myfunc)
root.config(menu = mainmenu)

mainmenu.add_cascade(label = "Run", menu = m3)


f1 = Frame(root, bg="grey", borderwidth= 2, relief=SUNKEN)
f1.grid(side=LEFT, fill="y")
f2 = Frame(root, bg = "grey", borderwidth = 3, relief = SUNKEN)
f2.grid(side = TOP, fill = "x")

l1 = Label(f1, text="Project Tkinter - Pycharm", bg = "grey")
l1.grid(pady = 20)
l2 = Label(f2, text = "Welcome to Pycharm IDE", font = "comicsansms 20 bold", bg = "grey")
l2.grid(pady = 15)


def login():
    pass

b1 = Button(f1, fg = "red", padx = 20, borderwidth = 4, text = "Login", command = login)
b1.grid()



# f3 = Frame(root, bg = "grey", borderwidth = 3, relief = SUNKEN)
# f3.pack(side = BOTTOM, fill = "x")

# label1 = Label(root, text = "Username :").pack(pady= 5)
# label2 = Label(root, text = "password :").pack(pady = 5)
# E1 = Entry(root, textvariable = "username").pack(pady = 5)
# E2 = Entry(root, textvariable = "password").pack(pady = 5)
#
# Button(root, text = "Login", font = "comicsansms 10 bold").pack(pady = 5)

root.mainloop()