"""
PROJ_DBPY
Display results window
Created by Judah Periyasamy
15/12/23
"""

import tkinter as tk
from database import *
from tkinter import *
import tkinter.font
# https://stackoverflow.com/questions/10989819/hiding-password-entry-input-in-python
def show():
    entry_pass.configure(show='')
    check.configure(command=hide, text='hide password')

def hide():
    entry_pass.configure(show='*')
    check.configure(command=show, text='show password')


def login_account():
    global entry_pass, check

    login_window = Tk()

    # new_account_window's parameters
    login_window.title("Sign Up")
    login_window.geometry("1920x1080")

    # color définition
    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color  # translation in hexa
    login_window.configure(bg=hex_color)
    login_window.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

    # Title of the results display
    lbl_title_new = tk.Label(login_window, text="CONNECTEZ_VOUS", font=("Arial", 15))
    lbl_title_new.grid(row=0, column=1, ipady=5, padx=40, pady=40)

    #Frames
    infos_frame = Frame(login_window, bg="white")

    #Labels
    lbl_username = Label(infos_frame, text="username: ", bg="white", padx=40, font=("Arial,11"))
    lbl_password = Label(infos_frame, text="password: ", bg="white", padx=40, font=("Arial,11"))

    #Entry
    entry_username = Entry(infos_frame)
    entry_pass = Entry(infos_frame, show="*")

    # Button
    check = Checkbutton(infos_frame, text='show password', command=show)

    # Place the elements
    infos_frame.grid(row=1, column=0, columnspan=3)

    lbl_username.grid(row=0, column=0, padx=(0, 10))
    entry_username.grid(row=0, column=1)

    lbl_password.grid(row=1, column=0, padx=(0, 10))
    entry_pass.grid(row=1, column=1)

    check.grid(row=1, column=2)


    # main loop
    login_window.mainloop()

login_account()