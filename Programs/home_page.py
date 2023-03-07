import tkinter
from tkinter import *
from PIL import ImageTk, Image

window = Tk()  # creating the default tkinter page

window.title("Home Page")  # title of the page

window.geometry('1500x750+300+200')  # setting the geometry of the page

window.config(bg='#fff')  # setting the background color

window.resizable(False, False)  # setting non-resizable page
# gui connective
def donatepage():
    import fund_donate


def user_profile():
    import user_profile


def organise():
    import organise_events


def ngo_history():
    window.destroy()
    import knowour


def welfare_page():
    import welfaredonation


def login():
    window.destroy()
    import log_in


def register():
    window.destroy()
    import signin


def about_us():
    root = Tk()
    root.geometry('500x500')
    root.title("About Us Page")
    info = Label(root, text="A Mini Project based on Donation for Specific OLD AGE HOME's")
    info.place(x=10,y=10)

    root.mainloop()


# creating main frame window
frame = Frame(window, width=1500, height=750, bg='#fff')
frame.place(x=0, y=0)

# background image
bg_image = PhotoImage(file="C:\\Users\\ACER\\PycharmProjects\\Old Age Home\\Images\\image.png")
bg_label = Label(frame, image=bg_image)
bg_label.place(x=0, y=0)

# login button
login_button = Button(frame, width=10, height=1, pady=7, text="Login", bg='#57a1f8', fg='white', border=0,
                      cursor='hand2', font=('Microsoft YaHei UI Light', 7, 'bold'),command=login)
login_button.place(x=1315, y=24)

# register button
register_button = Button(frame, width=20, height=1, pady=7, text="Register Now", bg='#57a1f8', fg='white', border=0,
                         cursor='hand2', font=('Microsoft YaHei UI Light', 7, 'bold'), command=register)
register_button.place(x=1145, y=24)

# creating a user profile icon
profile = PhotoImage(file='C:\\Users\\ACER\\PycharmProjects\\Old Age Home\\Images\\profile.png')
Button(window, image=profile, border=0, bg='white', cursor='hand2', command=user_profile).place(x=1425, y=0)

# creating system heading
heading = Label(frame, text="HAPPY HOME", fg='#57a1f8', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=675, y=5)

# creating a donation button
donate_button = Button(frame, width=39, pady=7, text="Fund Donation", bg='#57a1f8', fg='white', border=0, cursor='hand2',
                       command=donatepage)
donate_button.place(x=50, y=400)

# creating welfare donation button
welfare_button = Button(frame, width=39, pady=7, text="Welfare Donation", bg='#57a1f8', fg='white', border=0,
                        cursor='hand2', command=welfare_page)
welfare_button.place(x=50, y=470)

# event organisation button
event_button = Button(frame, width=39, pady=7, text='Organize Events', bg='#57a1f8', fg='white', border=0,
                      cursor='hand2', command=organise)
event_button.place(x=50, y=540)

# know ngo history
ngo_button = Button(frame, width=39, pady=7, text="NGO History's", bg='#57a1f8', fg='white', border=0,
                    cursor='hand2',command=ngo_history)
ngo_button.place(x=50, y=610)


# about us
about_us = Button(frame, text='About Us', bg='#57a1f8', fg='white', cursor='hand2', bd=0, command=about_us)
about_us.place(x=1435, y=725)

window.mainloop()
