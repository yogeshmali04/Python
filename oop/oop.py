from tkinter import *
from PIL import Image, ImageTk
root = Tk()

# GUI logic here

# width x height
root.geometry("444x222")
root.title("My GUI with Yogesh")

# Important label options
# text = add the text
# bd = background
# fg = foreground
# font = sets the font
# padx = x padding
# pady = y padding
# relief = border styling = SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text = '''Abdul Rashid Salim Salman Khan (pronounced [səlˈmaːn xaːn] ( listen); 27 December 1965) \n is an Indian film actor, producer, occasional singer and television personality who works in Hindi films.''',
                    bg="red", fg="white", padx=25, pady=50, font=("comicsansms", 19, "bold"), borderwidth=3, relief=SUNKEN)

# important pack options
# anchor = nw
# side =TOP, BOTTOM,LEFT,RIGHT
# fill
# padx
# pady


title_label.pack(side = BOTTOM, anchor="ne", fill=Y, padx = 25, pady = 25)


# width, height
# root.minsize(100, 100)

# width, height
# root.maxsize(1200, 700)

# abc = Label(text="My name is yogesh")
# abc.pack()

# For displaying image
image = Image.open("1.png")
photo = ImageTk.PhotoImage(image)
xyz = Label(image=photo)
xyz.pack(side = BOTTOM, anchor="sw")


root.mainloop()