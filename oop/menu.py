from tkinter import *

def myfunc():
    print("This is my Menubar")

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

root.mainloop()