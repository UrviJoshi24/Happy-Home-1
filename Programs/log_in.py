from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)


def sign_in():
    root.destroy()
    import signin


def forget_password():
    import forget_password


def hide():
    openeye.config(file='C:\\Users\\ACER\\PycharmProjects\\Old Age Home\\Images\\closeeye.png')
    code.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='C:\\Users\\ACER\\PycharmProjects\\Old Age Home\\Images\\openeye.png')
    code.config(show='')
    eyeButton.config(command=hide)


def signin():
    username = user.get()
    password = code.get()
    if username == 'admin@gmail.com' and password == '1234':
        messagebox.showerror("Valid", "Login Successful!")
        root.destroy()
        import home_page
# ADDED NEW WINDOW NAMED HOME PAGE
    elif username == " " or password == " ":
        messagebox.showerror("Invalid", "All fields are required!")
    elif username != "admin@gmail.com" and password != '1234':
        messagebox.showerror("Invalid", "Invalid username and password")
    elif password != "1234":
        messagebox.showerror("Invalid", "Invalid password")


img = PhotoImage(file='C://Users//ACER//PycharmProjects//Old Age Home//Images//login_img.png')
Label(root, image=img, bg='white').place(x=0,y=0)


frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=260, y=70)
heading = Label(frame, text='LOGIN', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=120, y=30)


def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'EmailID')


user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'EmailID')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)


def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')


code = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

openeye = PhotoImage(file='C:\\Users\\ACER\\PycharmProjects\\Old Age Home\\Images\\openeye.png')
eyeButton = Button(frame, image=openeye, bd=0, bg='White', activebackground='white', cursor='hand2', command=hide)
eyeButton.place(x=275, y=145)

forgetPassword = Button(frame, text="Forgot Password?", fg="#57a1f8", bg='white', font=('Microsoft YaHei UI Light', 9),
                        bd=0, cursor='hand2', command=forget_password)
forgetPassword.place(x=35, y=245)

remember_me = Checkbutton(frame, text="Remember Me", fg="#57a1f8", bg='white', font=('Microsoft YaHei UI Light', 9),
                     bd=0, cursor='hand2')
remember_me.place(x=210, y=245)

accountnothave = Label(frame, text="Don't have an account?", fg="black", bg='white',font=('Microsoft YaHei UI Light',9))
accountnothave.place(x=75, y=270)

Button(frame, width=39, pady=7, text='Sign in', bg="#57a1f8", fg='white', border=0, command=signin).place(x=35, y=204)
sign_up = Button(frame, width=6, bd=0, text='Sign up', bg="white", cursor="hand2", fg="#57a1f8", command=sign_in)
sign_up.place(x=215, y=270)
root.mainloop()
