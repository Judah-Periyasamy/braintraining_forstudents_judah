import database
import tkinter as tk
import tkinter.font
from tkinter import *


def admin_window(parent_frame, user_id=None):
    new_result_window = Toplevel(parent_frame)
    new_result_window.title("New Result")
    new_result_window.geometry("1000x150")

    # Color definition
    new_result_window.configure(bg="blue")
    new_result_window.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

    # Frames
    main_frame = tk.Frame(new_result_window, bg="white", padx=10)
    main_frame.pack()

    # Widgets
    items = ["Pseudo", "Date heure", "Temps", "Exercise", "nb OK", "nb Total"]
    for item in range(len(items)):
        info_item = Label(main_frame, text=items[item])
        info_item.grid(row=0, column=0 + item)

    name_entry = tkinter.Entry(main_frame)

    date_entry = Entry(main_frame)

    temps_entry = Entry(main_frame)

    exercise_entry = Entry(main_frame)

    ok_entry = Entry(main_frame)

    total_entry = Entry(main_frame)

    entries = [name_entry, date_entry, temps_entry, exercise_entry, ok_entry, total_entry]

    for ins_entry in range(len(entries)):
        entries[ins_entry].grid(row=1, column=ins_entry)

    finish_button = Button(main_frame, text="Finish",
                           command=lambda: modify_or_destroy(user_id,
                                                             data=[name_entry.get(),
                                                                   date_entry.get(),
                                                                   temps_entry.get(),
                                                                   ok_entry.get(),
                                                                   total_entry.get(),
                                                                   database.get_exercise_id(exercise_entry.get())],
                                                             window=new_result_window))
    finish_button.grid(row=2, column=4)
    new_result_window.mainloop()


def modify_or_destroy(user_id, data=None, window=None):
    if data is not None:
        database.result_modification(user_id, data)
        window.destroy()
    else:
        database.result_deletion(user_id)
