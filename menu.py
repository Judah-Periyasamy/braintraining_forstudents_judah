#############################
# Training (Menu)
# JCY oct 23
# PRO DB PY
#############################

import tkinter as tk
import geo01
import info02
import info05
from database import *
from tkinter import *
import tkinter.font

# exercises array
a_exercise=["geo01", "info02", "info05"]
albl_image=[None, None, None] # label (with images) array
a_image=[None, None, None] # images array
a_title=[None, None, None] # array of title (ex: GEO01)

dict_games = {"geo01": geo01.open_window_geo_01, "info02": info02.open_window_info_02, "info05": info05.open_window_info_05}

# call other windows (exercices)
def exercise(event,exer):
    dict_games[exer](window)


#call display_results
def display_result(event):
    # INSIDE WE WILL CREATE A NEW PAGE FOR THE RESULTS DISPLAY
    # window's start
    window = Tk()

    # window's parameters
    window.title("Affichage braintraining")
    window.geometry("1100x900")

    # color définition
    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color  # translation in hexa
    window.configure(bg=hex_color)
    window.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

    # Title of the results display
    lbl_title_results = tk.Label(window, text="TRAINING:AFFICHAGE", font=("Arial", 15))
    lbl_title_results.grid(row=0, column=1, ipady=5, padx=40, pady=40)

    # Frames
    filter_frame = Frame(window,bg="white", padx=10)

    #Filters Label
    lbl_user = Label(filter_frame, text="Pseudo :", bg="white", padx=40, font=("Arial,11"))
    lbl_ex = Label(filter_frame, text="Exercice :", bg="white", padx=40, font=("Arial,11"))
    lbl_startdate = Label(filter_frame, text="Date début :", bg="white", padx=40, font=("Arial,11"))
    lbl_enddate = Label(filter_frame, text="Date fin :", bg="white", padx=40, font=("Arial,11"))

    #Filters Entry
    entry_user = Entry(filter_frame)
    entry_ex = Entry(filter_frame)
    entry_startdate = Entry(filter_frame)
    entry_enddate = Entry(filter_frame)

    #Buttons
    button_result = Button(filter_frame, text="Voir résultats", font=("Arial,11"))

    # Place the elements
    #FILTER
    filter_frame.grid(row=1, columnspan=3)

    lbl_user.grid(row=0, column=0, padx=(0, 10))
    entry_user.grid(row=0, column=1)

    lbl_ex.grid(row=0, column=2, padx=(0, 10))
    entry_ex.grid(row=0, column=3)

    lbl_startdate.grid(row=0, column=4, padx=(0, 10))
    entry_startdate.grid(row=0, column=5)

    lbl_enddate.grid(row=0, column=6, padx=(0, 10))
    entry_enddate.grid(row=0, column=7)

    button_result.grid(row=1, column=0, pady=5)

    # main loop
    window.mainloop()
    print("display_result")


# Main window
window = tk.Tk()
window.title("Training, entrainement cérébral")
window.geometry("1100x900")

# color définition
rgb_color = (139, 201, 194)
hex_color = '#%02x%02x%02x' % rgb_color # translation in hexa
window.configure(bg=hex_color)
window.grid_columnconfigure((0,1,2), minsize=300, weight=1)

# Title création
lbl_title = tk.Label(window, text="TRAINING MENU", font=("Arial", 15))
lbl_title.grid(row=0, column=1,ipady=5, padx=40,pady=40)

# labels creation and positioning
for ex in range(len(a_exercise)):
    a_title[ex]=tk.Label(window, text=a_exercise[ex], font=("Arial", 15))
    a_title[ex].grid(row=1+2*(ex//3),column=ex % 3 , padx=40,pady=10) # 3 label per row

    a_image[ex] = tk.PhotoImage(file="img/" + a_exercise[ex] + ".gif") # image name
    albl_image[ex] = tk.Label(window, image=a_image[ex]) # put image on label
    albl_image[ex].grid(row=2 + 2*(ex // 3), column=ex % 3, padx=40, pady=10) # 3 label per row
    albl_image[ex].bind("<Button-1>", lambda event, ex = ex :exercise(event=None, exer=a_exercise[ex])) #link to others .py
    print(a_exercise[ex])

# Buttons, display results & quit
btn_display = tk.Button(window, text="Display results", font=("Arial", 15))
btn_display.grid(row=1+ 2*len(a_exercise)//3 , column=1)
btn_display.bind("<Button-1>",lambda e: display_result(e))

btn_finish = tk.Button(window, text="Quitter", font=("Arial", 15))
btn_finish.grid(row=2+ 2*len(a_exercise)//3 , column=1)
btn_finish.bind("<Button-1>", quit)

# main loop
window.mainloop()
