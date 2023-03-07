from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Know NGO's History")
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

def home():
    root.destroy()
    import home_page


def article_read():
    article_img.config(file='C:\\Users\\ACER\\PycharmProjects\\Old Age Home\\Images\\art_out.png')
    article.config(command=article_show)


def article_show():
    article_img.config(file='C:\\Users\\ACER\\PycharmProjects\\Old Age Home\\Images\\art-1.png')
    article.config(command=article_read)


# article1
article_img = PhotoImage(file='C:\\Users\\ACER\\PycharmProjects\\Old Age Home\\Images\\art-1.png')
article = Button(root, width=250, height=250, text="Click Here", image=article_img, cursor='hand2', bd=0,
                 command=article_read)
article.place(x=35, y=70)

home_button = Button(root, width=15, height=2, text='Home Page', cursor='hand2', bg='#57a1f8', fg='white', border=0,
              command=home)
home_button.place(x=810, y=455)

root.mainloop()
