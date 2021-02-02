from tkinter import *

root = Tk()

scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)

text = Text(root, yscrollcommand = scrollbar.set)
text.pack(fill = BOTH)

scrollbar.config(command = text.yview)



root.mainloop()
