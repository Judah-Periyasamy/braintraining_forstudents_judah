"""
PROJ_DBPY
Modify and Delete
Created by Judah Periyasamy
15/12/23
"""

import database
import tkinter as tk
import tkinter.font
from tkinter import *
from tkinter import ttk, messagebox


# Creation of a new window to modify a row
def admin_window(parent_frame, user_id=None):
    new_result_window = Toplevel(parent_frame)
    new_result_window.title("Modifcation")
    new_result_window.geometry("1000x150")

    # Color definition
    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color  # translation in hexa
    new_result_window.configure(bg=hex_color)
    new_result_window.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

    # Frames
    main_frame = tk.Frame(new_result_window, bg="white", padx=10)
    main_frame.pack()

    # Filters Label
    lbl_user = Label(main_frame, text="Pseudo :", bg="white", padx=40, font=("Arial,11"))
    lbl_date = Label(main_frame, text="Date et Heure :", bg="white", padx=40, font=("Arial,11"))
    lbl_time = Label(main_frame, text="Temps :", bg="white", padx=40, font=("Arial,11"))
    lbl_exercice = Label(main_frame, text="Exercice :", bg="white", padx=40, font=("Arial,11"))
    lbl_nb_ok = Label(main_frame, text="nb_ok :", bg="white", padx=40, font=("Arial,11"))
    lbl_nb_total = Label(main_frame, text="nb_Total :", bg="white", padx=40, font=("Arial,11"))

    # Filters Entry
    name_entry = Entry(main_frame)
    date_entry = Entry(main_frame)
    temps_entry = Entry(main_frame)

    exercise_entry = tk.StringVar()
    cbo_entry_exercice_create = ttk.Combobox(main_frame, textvariable=exercise_entry, font=("Arial", 10), width=15)
    cbo_entry_exercice_create['values'] = ('GEO01', 'INFO02', 'INFO05')
    cbo_entry_exercice_create['state'] = 'readonly'

    ok_entry = Entry(main_frame)
    total_entry = Entry(main_frame)

    # Place the elements

    lbl_user.grid(row=0, column=2, padx=(0, 10))
    name_entry.grid(row=0, column=3)

    lbl_date.grid(row=0, column=4, padx=(0, 10))
    date_entry.grid(row=0, column=5)

    lbl_time.grid(row=0, column=6, padx=(0, 10))
    temps_entry.grid(row=0, column=7)

    lbl_exercice.grid(row=1, column=2, padx=(0, 10))
    cbo_entry_exercice_create.grid(row=1, column=3)

    lbl_nb_ok.grid(row=1, column=4, padx=(0, 10))
    ok_entry.grid(row=1, column=5)

    lbl_nb_total.grid(row=1, column=6, padx=(0, 10))
    total_entry.grid(row=1, column=7)

    exercice = cbo_entry_exercice_create.get()
    if exercice == 'GE001':
        exercise_entry = 1
    elif exercice == 'INFO02':
        exercise_entry = 2
    elif exercice == 'INFO05':
        exercise_entry = 3

    # Button
    finish_button = Button(main_frame, text="Valider", font=("Arial,11"),
                           command=lambda: modify_or_destroy(user_id,
                                                             data=[name_entry.get(),
                                                                   date_entry.get(),
                                                                   temps_entry.get(),
                                                                   ok_entry.get(),
                                                                   total_entry.get(),
                                                                   database.get_exercise_id(exercise_entry.get())],
                                                             window=new_result_window))
    finish_button.grid(row=2, column=7)

    new_result_window.mainloop()


# Function will use the functions in database to modify or delete
def modify_or_destroy(user_id, data=None, window=None):
    if data is not None:
        database.result_modification(user_id, data)
        window.destroy()
    else:
        database.result_deletion(user_id)
