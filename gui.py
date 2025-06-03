from generate_password import generate_password
import tkinter as tk
from tkinter import *
import os
import sys


# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

bg_color = '#2471A3'

root = Tk()
root.title('Password generator')
root.iconbitmap(resource_path('icons\key32x32.ico'))
root.eval("tk::PlaceWindow . center")


frame = tk.Frame(root,
                width=500,
                height=300,
                bg=bg_color
                )

frame.grid(row=0,
           column=0,
           columnspan=5
           )

frame.pack_propagate(False)

var = tk.StringVar(value='')


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