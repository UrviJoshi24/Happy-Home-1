from tkinter import *

root1 = Tk()
root1.title('RESET PAGE')
root1.geometry('925x500+300+200')
root1.configure(bg="#fff")
root1.resizable(False, False)

frame = Frame(root1, width=350, height=350, bg="white")
frame.place(x=200, y=70)
heading = Label(frame, text='RESET PASSWORD', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=45, y=10)


# email id
def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'EMAIL ID')


user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'EMAIL ID')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)


# new password field
def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'NEW PASSWORD')


code = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'NEW PASSWORD')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)


#  confirm password field
def on_enter(e):
    code1.delete(0, 'end')


def on_leave(e):
    name = code1.get()
    if name == '':
        code1.insert(0, 'CONFIRM PASSWORD')


code1 = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code1.place(x=30, y=220)
code1.insert(0, 'CONFIRM PASSWORD')
code1.bind('<FocusIn>', on_enter)
code1.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

# creating update and reset button
Button(frame, width=15, pady=7, text='UPDATE', bg="#57a1f8", fg='white', border=0).place(x=35, y=304)

Button(frame, width=15, pady=7, text='RESET', bg="#57a1f8", fg='white', border=0).place(x=180, y=304)


root1.mainloop()
