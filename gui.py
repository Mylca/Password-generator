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


def copy_to_clipboard():
    text = pw_entry.get()
    root.clipboard_clear()
    root.clipboard_append(text)


def on_close():
    root.withdraw()
    root.clipboard_clear()
    root.clipboard_append("")
    root.update()
    root.destroy()



pw_entry = Entry(frame,
                 text='',
                 font=('Calibri', 30),
                 bg=bg_color,
                 fg='white'
                 )

pw_entry.grid(row=1,
              column=0,
              columnspan=3,
              padx=95,
              pady=50,
              sticky='w'
              )


generate_password_button = Button(frame,
                                  text='Generate',
                                  cursor='hand2',
                                  activebackground='#badee2',
                                  activeforeground='black',
                                  command=entry,
                                  font=('Calibri', 14),
                                  bg=bg_color,
                                  fg='white'

                                  )

generate_password_button.grid(row=2,
                              column=0,
                              padx=100,
                              pady=20,
                              sticky='w'
                              )


copy_to_clipboard_button = Button(frame,
                                  text='Copy',
                                  cursor='hand2',
                                  activebackground='#badee2',
                                  activeforeground='black',
                                  command=copy_to_clipboard,
                                  font=('Calibri', 14),
                                  bg=bg_color,
                                  fg='white'
                                  )

copy_to_clipboard_button.grid(row=2,
                              column=1,
                              padx=100,
                              pady=20,
                              sticky='e'
                              )


root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()
