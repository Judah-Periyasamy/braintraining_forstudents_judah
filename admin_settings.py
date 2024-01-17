"""
PROJ_DBPY
Settings
Created by Judah Periyasamy
15/12/23
"""

import tkinter as tk
from tkinter import ttk, messagebox
import database

def settings():
    global entry_player_level, entry_player_name, window_settings, combo_player_level

    # Window parameters
    window_settings = tk.Tk()
    window_settings.title("Paramètre")
    window_settings.geometry("600x400")
    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color
    window_settings.configure(bg=hex_color)

    # Title for the settings window
    label_title_settings = ttk.Label(window_settings, text="Paramètre", font=("Arial", 20))
    label_title_settings.pack(pady=10)

    # Entry for player name
    label_player_name = ttk.Label(window_settings, text="Pseudo du Joueur:")
    label_player_name.pack(pady=5)
    entry_player_name = ttk.Entry(window_settings)
    entry_player_name.pack(pady=10)

    # Combobox for player level
    label_player_level = ttk.Label(window_settings, text="Niveau du joueur:")
    label_player_level.pack(pady=5)
    levels = ["Eleve", "Prof"]
    combo_player_level = ttk.Combobox(window_settings, values=levels, state="readonly")
    combo_player_level.pack(pady=10)

    # Button to save player info
    save_button = ttk.Button(window_settings, text="Sauvegarder", command=save_player_info)
    save_button.pack(pady=20)

    window_settings.mainloop()

def save_player_info():
    # Retrieve input and combobox values
    player_name = entry_player_name.get()
    player_level = combo_player_level.get()

    # Check if the fields are not empty
    if not player_name or not player_level:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        return
    else:
        messagebox.showinfo("Succès", "Les informations de l'utilisateur ont été mises à jour avec succès.")

    # Save player information to database
    database.update_user_info(player_name, 2 if player_level == "Prof" else 1)

    # Close settings window
    window_settings.destroy()


