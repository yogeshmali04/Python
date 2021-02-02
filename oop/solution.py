from tkinter import *
root = Tk()

root.geometry("300x200")
root.title("Solution")

def windowsize():
    print("Updating GUI size")
    root.geometry(f"{width.get()}x{height.get()}")

width = StringVar()
height = StringVar()

Label(root, text = "Windows Resizer").grid(column = 1, pady = 20)

label1 = Label(root, text = "Enter Width : ").grid(row = 1)
label2 = Label(root, text = "Enter height : ").grid(row = 2)

Entry(root, textvariable = width).grid(row = 1, column = 1, pady = 5)
Entry(root, textvariable = height).grid(row = 2, column = 1, pady = 5)

Button(root, text = "Apply", command = windowsize).grid(row = 3, column = 1, pady = 10)

root.mainloop()