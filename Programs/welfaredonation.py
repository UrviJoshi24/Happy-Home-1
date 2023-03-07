from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('Welfare Donation')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

'''
def home_page():
    root.destroy()
    import home_page
'''

heading = Label(root, text='Welfare Donation', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=350, y=30)

food_button = Button(root, width=30, height=3, text='Food Donation', cursor='hand2', bg='#57a1f8', fg='white', border=0)
food_button.place(x=370,y=160)

clothes_button = Button(root, width=30, height=3, text='Clothes Donation', cursor='hand2', bg='#57a1f8', fg='white', border=0)
clothes_button.place(x=370,y=280)

'''
home = Button(root, width=15, height=2, text='Home Page', cursor='hand2', bg='#57a1f8', fg='white', border=0,
              command=home_page)
home.place(x=810, y=455)
'''

root.mainloop()
