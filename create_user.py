"""
PROJ_DBPY
Creation of new users
Created by Judah Periyasamy
18/01/24
"""

import tkinter as tk
from tkinter import messagebox
from database import *
from passlib.hash import bcrypt


# Function to see the password
def show():
    entry_new_pass.configure(show='')
    entry_confirm_pass.configure(show='')
    check.configure(command=hide, text='hide password')


# Function to hide the password
def hide():
    entry_new_pass.configure(show='*')
    entry_confirm_pass.configure(show='*')
    check.configure(command=show, text='show password')


# Function to sign in
def create_user_window():
    global entry_new_pass, entry_confirm_pass, check

    # Function that will create a new user
    def create_user_action():
        new_username = entry_new_username.get()
        new_password = entry_new_pass.get()
        confirm_password = entry_confirm_pass.get()

        # Check if passwords match
        if new_password != confirm_password:
            messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas.")
            return

        # Perform validation on the input if needed

        # Create the new user
        create_user(new_username, new_password)
        print(f"Utilisateur créé avec le nom {new_username}")
        messagebox.showinfo("Création réussie", f"Utilisateur créé avec le nom {new_username}")

        # Close the user creation window
        create_user_window.destroy()

    create_user_window = tk.Tk()

    create_user_window.title("Créer un utilisateur")
    create_user_window.geometry("500x350")

    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color
    create_user_window.configure(bg=hex_color)
    create_user_window.grid_columnconfigure((0, 1), minsize=250, weight=1)

    lbl_title_create = tk.Label(create_user_window, text="CRÉEZ UN UTILISATEUR", font=("Arial", 15))
    lbl_title_create.grid(row=0, column=0, columnspan=2, pady=20)

    infos_frame = tk.Frame(create_user_window, bg="white")

    lbl_new_username = tk.Label(infos_frame, text="Nom d'utilisateur: ", bg="white", padx=40, font=("Arial,11"))
    lbl_new_password = tk.Label(infos_frame, text="Mot de passe: ", bg="white", padx=40, font=("Arial,11"))
    lbl_confirm_password = tk.Label(infos_frame, text="Confirmer le mot de passe: ", bg="white", padx=40,
                                    font=("Arial,11"))

    entry_new_username = tk.Entry(infos_frame)
    entry_new_pass = tk.Entry(infos_frame, show="*")
    entry_confirm_pass = tk.Entry(infos_frame, show="*")

    check = tk.Checkbutton(infos_frame, text='Afficher le mot de passe', command=show)
    btn_create_user = tk.Button(infos_frame, text="Créer utilisateur", command=create_user_action)

    infos_frame.grid(row=1, column=0, columnspan=2)

    lbl_new_username.grid(row=0, column=0, padx=(0, 10))
    entry_new_username.grid(row=0, column=1)

    lbl_new_password.grid(row=1, column=0, padx=(0, 10))
    entry_new_pass.grid(row=1, column=1)

    lbl_confirm_password.grid(row=2, column=0, padx=(0, 10))
    entry_confirm_pass.grid(row=2, column=1)

    check.grid(row=4, column=0, columnspan=2)
    btn_create_user.grid(row=5, column=1, pady=10)

    create_user_window.mainloop()
