from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Fund Donation")
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

frame = Frame(root, bg='white',width=920, height=480)
frame.place(x=0, y=0)

intro = Label(frame, text='Choose any one of the Payment Gateway', fg='#57a1f8', bg='white',
              font=('Microsoft YaHei UI Light', 21, 'bold'))
intro.place(x=160, y=30)

credit_button = Button(root, width=30, height=3, text='Credit Card', cursor='hand2', bg='#57a1f8', fg='white',
                       border=0)
credit_button.place(x=370,y=140)

gpay_button = Button(root, width=30, height=3, text='Google Pay', cursor='hand2', bg='#57a1f8', fg='white', border=0)
gpay_button.place(x=370,y=240)

debit_button = Button(root, width=30, height=3, text='Debit Card', cursor='hand2', bg='#57a1f8', fg='white', border=0)
debit_button.place(x=370,y=340)


root.mainloop()