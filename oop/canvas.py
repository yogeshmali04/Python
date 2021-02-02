from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 600
root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Canvas")

can_widget = Canvas(root, width = canvas_width, height = canvas_height)
can_widget.pack()

can_widget.create_line(0, 0, 800, 600, fill = "red")
can_widget.create_line(0, 600, 800, 0, fill = "red")

can_widget.create_rectangle(100 , 100, 700, 500, fill = "blue")

can_widget.create_oval(200, 200, 500, 400, fill = "red")

can_widget.create_text(300, 300, text = "CANVAS")

root.mainloop()