from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('Organize Events')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)


heading = Label(root, text='Organize Events', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=350, y=30)

medical_button = Button(root, width=30, height=3, text='Organize Medical Camps', cursor='hand2', bg='#57a1f8',
                        fg='white', border=0)
medical_button.place(x=370,y=160)

other_button = Button(root, width=30, height=3, text='Yoga Session and Many more', cursor='hand2', bg='#57a1f8',
                      fg='white', border=0)
other_button.place(x=370,y=280)



root.mainloop()