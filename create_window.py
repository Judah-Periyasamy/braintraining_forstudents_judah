"""
Creation and modify window
Created by Judah Periyasamy
15/12/23
"""


import tkinter as tk
from tkinter import ttk, messagebox
import geo01
import info02
import info05
from database import *
from tkinter import *
import tkinter.font
from tkinter.messagebox import *

def create_result():
    global entry_user, entry_date, entry_time, entry_nb_ok, entry_nb_total, cbo_entry_exercice_create, create_win

    create_win = Tk()

    # window's parameters
    create_win.title("Create")
    create_win.geometry("1920x1080")

    # color définition
    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color  # translation in hexa
    create_win.configure(bg=hex_color)
    create_win.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

    # Title of the results display
    lbl_title_create = tk.Label(create_win, text="CREATION", font=("Arial", 15))
    lbl_title_create.grid(row=0, column=1, ipady=5, padx=40, pady=40)

    # Frames
    up_frame = Frame(create_win, bg="white")
    filter_frame = Frame(up_frame, bg="white", padx=10)

    # Filters Label
    lbl_user = Label(filter_frame, text="Pseudo :", bg="white", padx=40, font=("Arial,11"))
    lbl_date= Label(filter_frame, text="Date et Heure :", bg="white", padx=40, font=("Arial,11"))
    lbl_time = Label(filter_frame, text="Temps :", bg="white", padx=40, font=("Arial,11"))
    lbl_exercice = Label(filter_frame, text="Exercice :", bg="white", padx=40, font=("Arial,11"))
    lbl_nb_ok = Label(filter_frame, text="nb_ok :", bg="white", padx=40, font=("Arial,11"))
    lbl_nb_total = Label(filter_frame, text="nb_Total :", bg="white", padx=40, font=("Arial,11"))

    button_create_valid = Button(create_win, text="Valider", font=("Arial,11"), command=creation)

    #Label info spec
    lbl_info_title = tk.Label(create_win, text="INFORMATION CONCERNANT LES FORMATS", font=("Arial", 15))
    lbl_info_title.grid(row=4, column=1, ipady=5, padx=40, pady=40)

    lbl_infos = Label(create_win, text="Pour la date et heure : format YY-MM-DD HH:MM:SS", bg="white", padx=40, font=("Arial,11"))
    lbl_infos.grid(row=5, column=1, ipady=5, padx=40)

    lbl_infos2 = Label(create_win, text="Pour le temps : format HH:MM:SS", bg="white", padx=40, font=("Arial,11"))
    lbl_infos2.grid(row=6, column=1, ipady=5, padx=40, pady=40)

    # Filters Entry
    entry_user = Entry(filter_frame)
    entry_date = Entry(filter_frame)
    entry_time = Entry(filter_frame)

    exercise_value = tk.StringVar()
    cbo_entry_exercice_create = ttk.Combobox(filter_frame, textvariable=exercise_value, font=("Arial", 10), width=15)
    cbo_entry_exercice_create['values'] = ('GEO01', 'INFO02', 'INFO05')
    cbo_entry_exercice_create['state'] = 'readonly'

    entry_nb_ok = Entry(filter_frame)
    entry_nb_total = Entry(filter_frame)

    # Place the elements
    up_frame.grid(row=1, column=0, columnspan=3)
    filter_frame.grid(row=1, columnspan=3)

    lbl_user.grid(row=0, column=2, padx=(0, 10))
    entry_user.grid(row=0, column=3)

    lbl_date.grid(row=0, column=4, padx=(0, 10))
    entry_date.grid(row=0, column=5)

    lbl_time.grid(row=0, column=6, padx=(0, 10))
    entry_time.grid(row=0, column=7)

    lbl_exercice.grid(row=1, column=2, padx=(0, 10))
    cbo_entry_exercice_create.grid(row=1, column=3)

    lbl_nb_ok.grid(row=1, column=4, padx=(0, 10))
    entry_nb_ok.grid(row=1, column=5)

    lbl_nb_total.grid(row=1, column=6, padx=(0, 10))
    entry_nb_total.grid(row=1, column=7)

    button_create_valid.grid(row=3, column=1, ipady=5, padx=40, pady=40)

    # main loop
    create_win.mainloop()

# Function for the colors for progress bar
def get_color(percentage):
    if percentage >= 70:
        return "#00FF00"  # Green
    elif 40 <= percentage < 70:
        return "#FFA500"  # Orange
    else:
        return "#FF0000"  # Red

def creation():
    open_dbconnection()
    global entry_user, entry_date, entry_time, entry_nb_ok, entry_nb_total, cbo_entry_exercice_create, create_win
    username = entry_user.get()
    date_hour = entry_date.get()
    duration = entry_time.get()
    nb_ok = entry_nb_ok.get()
    nb_total = entry_nb_total.get()
    exercice_value = 0

    exercice = cbo_entry_exercice_create.get()
    if exercice == 'GE001':
        exercice_value = 1
    elif exercice == 'INFO02':
        exercice_value = 2
    elif exercice == 'INFO05':
        exercice_value = 3

    if username == "" or date_hour == "" or duration =="" or nb_ok == "" or nb_total == "" or exercice == "":
        print("TEST")
        messagebox.showinfo("Message", "Veuillez entrez toutes les valeurs!!")

    else:
        try:
           res = create_results(username,date_hour,duration,nb_ok,nb_total,exercice_value)
           if res:
               messagebox.showinfo("Message", "Validé !!!")
               print("dans save")
               create_win.destroy()
           else:
                print("Echec de l'ajout.\n")
        except Exception:
            print("Echec de l'ajout.\n")

    close_dbconnection()
