import tkinter as tk
from database import *
from tkinter import *
import tkinter.font
from passlib.hash import bcrypt


def show():
    entry_pass.configure(show='')
    check.configure(command=hide, text='hide password')


def hide():
    entry_pass.configure(show='*')
    check.configure(command=show, text='show password')


def create_user_window():
    def create_user_action():
        new_username = entry_new_username.get()
        new_password = entry_new_pass.get()
        level = int(entry_level.get())  # Assuming you want to capture the user's level as well

        # Perform validation on the input if needed

        # Create the new user
        create_user(new_username, new_password, level)
        print(f"Utilisateur créé avec le nom {new_username} et le niveau {level}")

        # Close the create user window
        create_user_window.destroy()

    create_user_window = Tk()

    create_user_window.title("Créer un utilisateur")
    create_user_window.geometry("500x300")

    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color
    create_user_window.configure(bg=hex_color)
    create_user_window.grid_columnconfigure((0, 1), minsize=250, weight=1)

    lbl_title_create = tk.Label(create_user_window, text="CRÉEZ UN UTILISATEUR", font=("Arial", 15))
    lbl_title_create.grid(row=0, column=0, columnspan=2, pady=20)

    infos_frame = Frame(create_user_window, bg="white")

    lbl_new_username = Label(infos_frame, text="Nom d'utilisateur: ", bg="white", padx=40, font=("Arial,11"))
    lbl_new_password = Label(infos_frame, text="Mot de passe: ", bg="white", padx=40, font=("Arial,11"))
    lbl_level = Label(infos_frame, text="Niveau: ", bg="white", padx=40, font=("Arial,11"))

    entry_new_username = Entry(infos_frame)
    entry_new_pass = Entry(infos_frame, show="*")
    entry_level = Entry(infos_frame)

    check = Checkbutton(infos_frame, text='Afficher le mot de passe', command=show)
    btn_create_user = Button(infos_frame, text="Créer utilisateur", command=create_user_action)

    infos_frame.grid(row=1, column=0, columnspan=2)

    lbl_new_username.grid(row=0, column=0, padx=(0, 10))
    entry_new_username.grid(row=0, column=1)

    lbl_new_password.grid(row=1, column=0, padx=(0, 10))
    entry_new_pass.grid(row=1, column=1)

    lbl_level.grid(row=2, column=0, padx=(0, 10))
    entry_level.grid(row=2, column=1)

    check.grid(row=3, column=0, columnspan=2)
    btn_create_user.grid(row=4, column=1, pady=10)

    create_user_window.mainloop()


create_user_window()
