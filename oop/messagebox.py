from tkinter import *
import tkinter.messagebox as tmsg

def myfunc():
    print("This is my Menubar")

def help():
    print("i will help you")
    tmsg.showinfo("help", "yogesh will help you")

def rate():
    print("rate us")
    tmsg.askquestion("About us", "was your experience good?")

root = Tk()
root.geometry("800x600")

mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff = 0)
m1.add_command(label = "Save", command = myfunc)
m1.add_command(label = "save as", command = myfunc)
m1.add_separator()
m1.add_command(label = "New", command = myfunc)
m1.add_command(label = "New Project", command = myfunc)
root.config(menu = mainmenu)

mainmenu.add_cascade(label = "File", menu = m1)


m2 = Menu(mainmenu, tearoff = 0)
m2.add_command(label = "cut", command = myfunc)
m2.add_command(label = "copy", command = myfunc)
# m2.add_separator()
m2.add_command(label = "paste", command = myfunc)
m2.add_command(label = "delete", command = myfunc)
root.config(menu = mainmenu)

mainmenu.add_cascade(label = "Edit", menu = m2)


m3 = Menu(mainmenu, tearoff = 0)
m3.add_command(label = "help", command = help)
m3.add_command(label = "Rate us", command = rate)
root.config(menu = mainmenu)

mainmenu.add_cascade(label = "Run", menu = m3)

root.mainloop()