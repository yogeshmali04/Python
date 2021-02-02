from tkinter import *
root = Tk()
root.geometry("600x400")
root.title("Status Bar")

def delay():
    status.set("busy...")
    sbar.update()
    import time
    time.sleep(2)
    status.set("Ready")
status = StringVar()
status.set("Ready")
sbar = Label(root, textvariable = status, relief = SUNKEN, anchor="w")
sbar.pack(side = "bottom", fill = X)

Button(root, text = "submit", command = delay).pack()

root.mainloop()