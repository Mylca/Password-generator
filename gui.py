from generate_password import generate_password
from tkinter import *


def entry():
    pw_entry.delete(0, END)
    my_password = generate_password()
    pw_entry.insert(0, my_password)


root = Tk()
root.title('Password generator')
root.geometry('500x300')


pw_entry = Entry(root, text='', font=('Calibri', 24))
pw_entry.pack(pady=20, padx=20)


my_frame = Frame(root)
my_frame.pack(pady=20)


my_button = Button(my_frame, text='Generate', command=entry)
my_button.grid(row=0, column=0, padx=10)


clip_button = Button(my_frame, text='Copy')
clip_button.grid(row=0, column=1, padx=10)


root.mainloop()