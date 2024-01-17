#############################
# Training (Menu)
# JCY oct 23
# PRO DB PY
"""
Modified by Judah Periyasamy
15/12/23
"""
#############################

import geo01
import info02
import info05
from database import *
import subprocess
from tkinter import *
from register import *

# exercises array
a_exercise = ["geo01", "info02", "info05"]
albl_image = [None, None, None]  # label (with images) array
a_image = [None, None, None]  # images array
a_title = [None, None, None]  # array of title (ex: GEO01)

dict_games = {"geo01": geo01.open_window_geo_01, "info02": info02.open_window_info_02,
              "info05": info05.open_window_info_05}


# call results.py file
def display_results(event, username, privilege):
    from results import display_result
    display_result(username, privilege)


# call other windows (exercices)
def exercise(event, exer, username):
    dict_games[exer](window, username)

def logout():
    # Fermer la fenêtre principale
    window.destroy()

    # Relancer la fenêtre de connexion
    login_account()


def launch_main_window(username, privilege):
    global window, entry_username
    # Main window
    window = tk.Tk()
    window.title("Training, entrainement cérébral")
    window.geometry("1100x900")

    # color définition
    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color  # translation in hexa
    window.configure(bg=hex_color)
    window.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

    # Title création
    lbl_title = tk.Label(window, text="TRAINING MENU", font=("Arial", 15))
    lbl_title.grid(row=0, column=1, ipady=5, padx=40, pady=40)

    # labels creation and positioning
    for ex in range(len(a_exercise)):
        a_title[ex] = tk.Label(window, text=a_exercise[ex], font=("Arial", 15))
        a_title[ex].grid(row=1 + 2 * (ex // 3), column=ex % 3, padx=40, pady=10)  # 3 label per row

        a_image[ex] = tk.PhotoImage(file="img/" + a_exercise[ex] + ".gif")  # image name
        albl_image[ex] = tk.Label(window, image=a_image[ex])  # put image on label
        albl_image[ex].grid(row=2 + 2 * (ex // 3), column=ex % 3, padx=40, pady=10)  # 3 label per row
        albl_image[ex].bind("<Button-1>",
                            lambda event, ex=ex: exercise(event=None, exer=a_exercise[ex], username=username))  # link to others .py
        print(a_exercise[ex])

    # Buttons, display results & quit
    btn_display = tk.Button(window, text="Display results", font=("Arial", 15))
    btn_display.grid(row=1 + 2 * len(a_exercise) // 3, column=1)
    btn_display.bind("<Button-1>", lambda e: display_results(e, username, privilege))

    btn_finish = tk.Button(window, text="Quitter", font=("Arial", 15))
    btn_finish.grid(row=2 + 2 * len(a_exercise) // 3, column=1)
    btn_finish.bind("<Button-1>", quit)

    btn_logout = tk.Button(window, text="Logout", font=("Arial", 15), command=logout)
    btn_logout.grid(row=5, column=1, pady=10)

    return window


def start_main_window(user):
    window_bis = launch_main_window(user["username"], user["level"])
    window_bis.mainloop()