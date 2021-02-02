from tkinter import *

def yogesh(event):
    print("you clicked on the button")
root = Tk()
root.geometry("800x600")

widget = Button(root, text = "submit")
widget.pack()

widget.bind('<Button-1>', yogesh)
widget.bind('<Double-1>', quit)


root.mainloop()
