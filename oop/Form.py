from tkinter import *

root = Tk()

root.geometry("655x544")
root.title("Form")

def getvals():
    print(f"{namevalue.get(), phonevalue.get(), destinationvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n")
    # print(f"{uservalue.get(), passvalue.get()}")

    with open("records.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), destinationvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n")

    # with open("records.txt", "a") as f:
    #     f.write(f"{namevalue.get(),phonevalue.get(),destinationvalue.get(),paymentmodevalue.get(),foodservicevalue}")

Label(text = "Welcome to my Travel Agency").grid(row = 0, column = 2)

name = Label(root, text = "Name")
phone = Label(root, text = "Phone")
destination = Label(root, text = "Destination")
paymentmode = Label(root, text = "Payment Mode")


name.grid(row = 1, column = 2)
phone.grid(row = 2, column = 2)
destination.grid(row = 3, column = 2)
paymentmode.grid(row = 4, column = 2)

namevalue = StringVar()
phonevalue = StringVar()
destinationvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

nameentry = Entry(root, textvariable = namevalue)
phoneentry = Entry(root, textvariable = phonevalue)
destinationentry = Entry(root, textvariable = destinationvalue)
paymentmodeentry = Entry(root, textvariable = paymentmodevalue)


nameentry.grid(row = 1, column = 3)
phoneentry.grid(row = 2, column = 3)
destinationentry.grid(row = 3, column = 3)
paymentmodeentry.grid(row = 4, column = 3)

foodservice = Checkbutton(text="You want a Premeal service?", variable=foodservicevalue)
foodservice.grid(row = 5, column = 3)

Button(text = "Submit", command = getvals).grid(row = 6, column = 3)

root.mainloop()
