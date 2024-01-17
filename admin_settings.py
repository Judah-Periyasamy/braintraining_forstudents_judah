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

    # Entry for help
    label_player_level = ttk.Label(window_settings, text="Niveaux :1 = Eleve | 2 = Prof ")
    label_player_level.pack(pady=5)

    # Button to save player info
    save_button = ttk.Button(window_settings, text="Sauvegarder", command=save_player_info)
    save_button.pack(pady=20)

    window_settings.mainloop()

def save_player_info():
    # Récupérer les valeurs des entrées et de la combobox
    player_name = entry_player_name.get()
    player_level = combo_player_level.get()

    # Vérifier si les champs ne sont pas vides
    if not player_name or not player_level:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        return

    # Sauvegarder les informations du joueur dans la base de données ou le fichier de configuration
    # (en fonction de la façon dont vous souhaitez stocker ces informations)

    # Fermer la fenêtre des paramètres
    window_settings.destroy()


