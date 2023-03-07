from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('User Profile')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)


def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')


heading = Label(root, text='User Profile Details', fg='#57a1f8', bg='white',
                font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=345, y=30)

message = Label(root, text='Enter your EmailId to know your details',fg='#57a1f8',bg='white')
message.place(x=375,y=80)

code = Entry(root, width=25, fg="#57a1f8", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code.place(x=230, y=150)
code.insert(0, 'EmailID')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(root, width=295, height=2, bg='black').place(x=230, y=177)

enter_button = Button(root, width=20, height=2, text='Enter', cursor='hand2', bg='#57a1f8', fg='white', border=0)
enter_button.place(x=550, y=140)


root.mainloop()
