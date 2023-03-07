from tkinter import *
from tkinter import messagebox

base = Tk()
base.geometry("500x500")
base.title("Sign Up form")
base.configure(bg='light blue')


def login():
    messagebox.showerror("Valid", "Sign in Successful")
    base.destroy()
    import log_in


lb1 = Label(base, text="Enter Name", bg="blue", fg="black", width=10, font=("roman", 12))
lb1.place(x=20, y=120)
en1 = Entry(base)
en1.place(x=200, y=120)
lb3 = Label(base, text="Enter Email", bg="blue", fg="black", width=10, font=("roman", 12))
lb3.place(x=19, y=160)
en3 = Entry(base)
en3.place(x=200, y=160)
lb4 = Label(base, text="Contact Number", bg="blue", fg="black", width=13, font=("roman", 12))
lb4.place(x=19, y=200)
en4 = Entry(base)

en4.place(x=200, y=200)

list_of_pay = ("Credit Card", "PayPal", "Amazon Pay", "Google Pay")
cv = StringVar()
drplist = OptionMenu(base, cv, *list_of_pay)
drplist.config(width=15)
cv.set("Credit Card")
lb2 = Label(base, text="Mode of Payment", bg="blue", fg="black", width=13, font=("roman", 12))
lb2.place(x=16, y=280)
drplist.place(x=200, y=275)
lb6 = Label(base, text="Enter Password", bg="blue", fg="black", width=13, font=("roman", 12))
lb6.place(x=19, y=320)
en6 = Entry(base, show='*')
en6.place(x=200, y=320)

lb7 = Label(base, text="Re-Enter Password", bg="blue", fg="black", width=15, font=("roman", 12))
lb7.place(x=21, y=360)
en7 = Entry(base, show='*')
en7.place(x=200, y=360)

Button(base, text="Sign Up", width=10, bg="grey", fg="white", command=login).place(x=200, y=400)
base.mainloop()




