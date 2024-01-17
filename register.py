"""
PROJ_DBPY
Register
Created by Judah Periyasamy
18/01/24
"""

import tkinter as tk
from tkinter import messagebox

from database import *
from create_user import *

import menu as menu_api

def show():
    entry_pass.configure(show='')
    check.configure(command=hide, text='hide password')

def hide():
    entry_pass.configure(show='*')
    check.configure(command=show, text='show password')

def authenticate_user():
    username = entry_username.get()
    password = entry_pass.get()

    user = login_user(username, password)

    if user != False:
        # Utilisateur authentifié, afficher un message de réussite
        messagebox.showinfo("Connexion réussie", f"Connexion réussie en tant que {username} avec le niveau {user['level']}")

        # Lancer la fenêtre principale avec le nom d'utilisateur
        login_window.destroy()
        menu_api.start_main_window(user)


    else:
        # Échec de la connexion, afficher un message d'erreur
        messagebox.showerror("Échec de la connexion", "Échec de la connexion. Vérifiez les informations d'identification.")


def login_account():
    global entry_username, login_window, entry_pass, check

    login_window = tk.Tk()

    # new_account_window's parameters
    login_window.title("Sign Up")
    login_window.geometry("900x300")

    # color définition
    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color  # translation in hexa
    login_window.configure(bg=hex_color)
    login_window.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

    # Title of the results display
    lbl_title_new = tk.Label(login_window, text="CONNECTEZ_VOUS", font=("Arial", 15))
    lbl_title_new.grid(row=0, column=1, ipady=5, padx=40, pady=40)

    # Frames
    infos_frame = tk.Frame(login_window, bg="white")

    # Labels
    lbl_username = tk.Label(infos_frame, text="username: ", bg="white", padx=40, font=("Arial,11"))
    lbl_password = tk.Label(infos_frame, text="password: ", bg="white", padx=40, font=("Arial,11"))

    # Entry
    entry_username = tk.Entry(infos_frame)
    entry_pass = tk.Entry(infos_frame, show="*")

    # Button
    check = tk.Checkbutton(infos_frame, text='show password', command=show)
    btn_login = tk.Button(infos_frame, text="Login", command=authenticate_user)
    btn_create_user = tk.Button(infos_frame, text="Créer un utilisateur", command=create_user_window)

    # Place the elements
    infos_frame.grid(row=1, column=0, columnspan=3)

    lbl_username.grid(row=0, column=0, padx=(0, 10))
    entry_username.grid(row=0, column=1)

    lbl_password.grid(row=1, column=0, padx=(0, 10))
    entry_pass.grid(row=1, column=1)

    check.grid(row=1, column=2)
    btn_login.grid(row=2, column=1, pady=10)
    btn_create_user.grid(row=4, column=1, pady=10)

    # main loop
    login_window.mainloop()


# Appeler la fonction pour lancer la fenêtre de connexion
if __name__ == "__main__":
    login_account()