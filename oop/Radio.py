from tkinter import *
root = Tk()

root.geometry("800x600")
root.title("Radio buttons")

def order():
    print(f"your order of {var.get()} is received. Thank u for ordering!")

var = StringVar()
var.set("radio")
Label(root, text = "What would you like to eat sir?", font = "lucida 20 bold").pack(anchor = "w")

radio = Radiobutton(root, text = "Dosa", variable = var, value = "Dosa").pack(anchor = "w")
radio = Radiobutton(root, text = "Idly", variable = var, value = "Idly").pack(anchor = "w")
radio = Radiobutton(root, text = "Paratha", variable = var, value = "Paratha").pack(anchor = "w")
radio = Radiobutton(root, text = "Samosa", variable = var, value = "Samosa").pack(anchor = "w")

Button(root, text = "Order Now", command = order).pack(anchor = "w", padx = "10", pady = 15)
root.mainloop()