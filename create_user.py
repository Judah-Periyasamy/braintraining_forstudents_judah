import tkinter as tk
from tkinter import ttk
from database import *
from passlib.hash import bcrypt


def show():
    entry_new_pass.configure(show='')
    check.configure(command=hide, text='hide password')


def hide():
    entry_new_pass.configure(show='*')
    check.configure(command=show, text='show password')


def create_user_window():
    global entry_new_pass, check
    def create_user_action():
        new_username = entry_new_username.get()
        new_password = entry_new_pass.get()
        level = level_combobox.get()  # Get the selected level from the combobox

        if level == 'Prof':
            level = 2
        else:
            level = 1
        # Perform validation on the input if needed

        # Create the new user
        create_user(new_username, new_password, level)
        print(f"Utilisateur créé avec le nom {new_username} et le niveau {level}")
        messagebox.showinfo("Creation réussie",f"Utilisateur créé avec le nom {new_username} et le niveau {level}")

        # Close the create user window
        create_user_window.destroy()

    create_user_window = tk.Tk()

    create_user_window.title("Créer un utilisateur")
    create_user_window.geometry("500x300")

    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color
    create_user_window.configure(bg=hex_color)
    create_user_window.grid_columnconfigure((0, 1), minsize=250, weight=1)

    lbl_title_create = tk.Label(create_user_window, text="CRÉEZ UN UTILISATEUR", font=("Arial", 15))
    lbl_title_create.grid(row=0, column=0, columnspan=2, pady=20)

    infos_frame = tk.Frame(create_user_window, bg="white")

    lbl_new_username = tk.Label(infos_frame, text="Nom d'utilisateur: ", bg="white", padx=40, font=("Arial,11"))
    lbl_new_password = tk.Label(infos_frame, text="Mot de passe: ", bg="white", padx=40, font=("Arial,11"))
    lbl_level = tk.Label(infos_frame, text="Niveau: ", bg="white", padx=40, font=("Arial,11"))

    entry_new_username = tk.Entry(infos_frame)
    entry_new_pass = tk.Entry(infos_frame, show="*")

    # Combobox for level (Prof or Eleve)
    level_options = ["Prof", "Eleve"]
    level_combobox = ttk.Combobox(infos_frame, values=level_options, state="readonly")
    level_combobox.set(level_options[0])  # Default value

    check = tk.Checkbutton(infos_frame, text='Afficher le mot de passe', command=show)
    btn_create_user = tk.Button(infos_frame, text="Créer utilisateur", command=create_user_action)

    infos_frame.grid(row=1, column=0, columnspan=2)

    lbl_new_username.grid(row=0, column=0, padx=(0, 10))
    entry_new_username.grid(row=0, column=1)

    lbl_new_password.grid(row=1, column=0, padx=(0, 10))
    entry_new_pass.grid(row=1, column=1)

    lbl_level.grid(row=2, column=0, padx=(0, 10))
    level_combobox.grid(row=2, column=1)

    check.grid(row=3, column=0, columnspan=2)
    btn_create_user.grid(row=4, column=1, pady=10)

    create_user_window.mainloop()



