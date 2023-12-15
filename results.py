import tkinter as tk
from database import *
from tkinter import *
import tkinter.font
from create_window import *
import admin_window as admin


class DeleteButton:
    def __init__(self, res_frame, student_id, rowD, columnD):
        self.destroy_button = Button(res_frame, text="Effacer", command=lambda: refresh_data(student_id))
        self.destroy_button.grid(row=rowD, column=columnD, sticky="NSEW")


class ModifyButton:
    def __init__(self, res_frame, main_results_window, student_id, rowD, columnD):
        self.modify_button = Button(res_frame, text="Modifier", command=lambda: refresh_data(student_id,
                                                                                             main_results_window))
        self.modify_button.grid(row=rowD, column=columnD, sticky="NSEW")


def refresh_data(user_id, main_results_window=None):
    if main_results_window is not None:
        admin.admin_window(main_results_window, user_id)
    else:
        admin.modify_or_destroy(user_id)
    show_info()


def display_result():
    # INSIDE WE WILL CREATE A NEW PAGE FOR THE RESULTS DISPLAY
    global entry_user, entry_ex, up_frame, total_frame, results_frame, results_window
    # results_window's start
    results_window = Tk()

    # results_window's parameters
    results_window.title("Affichage braintraining")
    results_window.geometry("1920x1080")

    # color définition
    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color  # translation in hexa
    results_window.configure(bg=hex_color)
    results_window.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

    # Title of the results display
    lbl_title_results = tk.Label(results_window, text="TRAINING:AFFICHAGE", font=("Arial", 15))
    lbl_title_results.grid(row=0, column=1, ipady=5, padx=40, pady=40)

    # Frames
    up_frame = Frame(results_window, bg="white")
    down_frame = Frame(results_window, bg="white")
    filter_frame = Frame(up_frame, bg="white", padx=10)
    results_frame = Frame(up_frame, bg="white", padx=10)
    title_total_frame = Frame(down_frame, bg="white", padx=10)
    total_frame = Frame(down_frame, bg="white", padx=10)

    # Filters Label
    lbl_user = Label(filter_frame, text="Pseudo :", bg="white", padx=40, font=("Arial,11"))
    lbl_ex = Label(filter_frame, text="Exercice :", bg="white", padx=40, font=("Arial,11"))
    lbl_startdate = Label(filter_frame, text="Date début :", bg="white", padx=40, font=("Arial,11"))
    lbl_enddate = Label(filter_frame, text="Date fin :", bg="white", padx=40, font=("Arial,11"))

    # Totals labels
    title_total = Label(title_total_frame, text="Total", bg="white", padx=40, font=("Arial,11"))

    lbl_tot = Label(total_frame, text="NbLignes", bg="white", padx=40, font=("Arial, 11"))
    lbl_time = Label(total_frame, text="Temps total", bg="white", padx=40, font=("Arial, 11"))
    lbl_nbok = Label(total_frame, text="Nb OK", bg="white", padx=40, font=("Arial, 11"))
    lbl_nbtotal = Label(total_frame, text="Nb Total", bg="white", padx=40, font=("Arial, 11"))
    lbl_purcenttot = Label(total_frame, text="% Total", bg="white", padx=40, font=("Arial, 11"))

    # Filters Entry
    entry_user = Entry(filter_frame)
    entry_ex = Entry(filter_frame)
    entry_startdate = Entry(filter_frame)
    entry_enddate = Entry(filter_frame)

    # Buttons
    button_result = Button(filter_frame, text="Voir résultats", font=("Arial,11"), command=show_info)
    button_create = Button(filter_frame, text="Créer un résultat", font=("Arial,11"), command=create_result)

    # Place the elements
    up_frame.grid(row=1, column=0, columnspan=3)
    down_frame.grid(row=2, column=0, pady=10, columnspan=3)
    # FILTER
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
    button_create.grid(row=1, column=7, pady=5)

    # TOTAL
    title_total_frame.grid(row=3, pady=10, columnspan=3)
    title_total.grid(row=3, pady=10, columnspan=3)

    total_frame.grid(row=4, pady=10, columnspan=3)

    lbl_tot.grid(row=0, column=0, padx=(0, 10))
    lbl_time.grid(row=0, column=1, padx=(0, 10))
    lbl_nbok.grid(row=0, column=2, padx=(0, 10))
    lbl_nbtotal.grid(row=0, column=3, padx=(0, 10))
    lbl_purcenttot.grid(row=0, column=4, padx=(0, 10))

    show_info()

    # main loop
    results_window.mainloop()
    print("display_result")


# call display_results

# Function for the colors for progress bar
def get_color(percentage):
    if percentage >= 70:
        return "#00FF00"  # Green
    elif 40 <= percentage < 70:
        return "#FFA500"  # Orange
    else:
        return "#FF0000"  # Red


# Function that we will destroy each time the results values and it creates a new one
def show_info():
    global total_frame
    open_dbconnection()
    name = infos_results(entry_user.get(), entry_ex.get())

    for widget in results_frame.winfo_children():
        if widget.grid_info()['row'] != 0:
            widget.destroy()

    # Results labels
    lbl_col_student = Label(results_frame, text="Élève", bg="white", padx=40, font=("Arial,11"))
    lbl_col_date_hour = Label(results_frame, text="Date heure", bg="white", padx=40, font=("Arial,11"))
    lbl_col_time = Label(results_frame, text="Temps", bg="white", padx=40, font=("Arial,11"))
    lbl_col_ex = Label(results_frame, text="Exercice", bg="white", padx=40, font=("Arial,11"))
    lbl_col_nbok = Label(results_frame, text="nb OK", bg="white", padx=40, font=("Arial,11"))
    lbl_col_nbtot = Label(results_frame, text="nb Total", bg="white", padx=40, font=("Arial,11"))
    lbl_col_reussi = Label(results_frame, text="% réussi", bg="white", padx=40, font=("Arial,11"))

    # RESULTS placements
    results_frame.grid(row=2, pady=10, columnspan=3)

    lbl_col_student.grid(row=0, column=0, padx=(0, 10))

    lbl_col_date_hour.grid(row=0, column=1, padx=(0, 10))

    lbl_col_time.grid(row=0, column=2, padx=(0, 10))

    lbl_col_ex.grid(row=0, column=3, padx=(0, 10))

    lbl_col_nbok.grid(row=0, column=4, padx=(0, 10))

    lbl_col_nbtot.grid(row=0, column=5, padx=(0, 10))

    lbl_col_reussi.grid(row=0, column=6, padx=(0, 10))

    # Progress
    lbl_col_progress = Label(results_frame, text="Progression", bg="white", padx=40, font=("Arial,11"))
    lbl_col_progress.grid(row=0, column=7, padx=(0, 10))

    lbl_col_progress_total = Label(total_frame, text="Progression", bg="white", padx=40, font=("Arial,11"))
    lbl_col_progress_total.grid(row=0, column=5)

    # Insert the values taken from MySQL into Tkinter
    for student in name:
        for j in range(len(student)):
            for data in range(len(student[j])):
                if data != 3:
                    values = Label(results_frame, width=10,
                                   text=student[j][data])  # values label creation for the results
                else:
                    values = Label(results_frame, width=10,
                                   text=get_exercice_name(student[j][data]))  # values label creation for the results
                values.grid(row=j + 1, column=data)
            try:
                success_percentage = round(float(student[j][4]) * 100 / float(student[j][5]),
                                           2)  # purcentage calculation
                values = Label(results_frame, width=10,
                               text=f"{success_percentage}%")  # values label creation for (réussi)
            except:
                values = Label(results_frame, width=10, text="0%")  # values label creation for (réussi)
            values.grid(row=j + 1, column=6)

            # Creation of the bar progression
            success_percentage = round(float(student[j][4]) * 100 / float(student[j][5]), 2)  # purcentage calculation
            progress_rect = Canvas(results_frame, width=100, height=20, bg="white", bd=0, highlightthickness=0)
            if success_percentage == 0:
                progress_rect.create_rectangle(0, 0, 1, 20, fill=get_color(success_percentage), outline="")
            else:
                progress_rect.create_rectangle(0, 0, success_percentage, 20, fill=get_color(success_percentage),
                                               outline="")
            progress_rect.grid(row=j + 1, column=7, pady=5)
            # https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/create_rectangle.html

            # Add buttons for actions
            destroy_button_name = f"destroy_button_{j}"
            modify_button_name = f"modify_button_{j}"
            exec(
                "%s = DeleteButton(results_frame, student[j][6], %d, %d)"
                % (destroy_button_name, j + 1, 8))
            exec(
                "%s = ModifyButton(results_frame, results_window, student[j][6], %d, %d)"
                % (modify_button_name, j + 1, 9))

    totals = total_result(entry_user.get(), entry_ex.get())
    for widget in total_frame.winfo_children():
        if widget.grid_info()['row'] != 0:
            widget.destroy()
    for total in range(len(totals)):
        values = Label(total_frame, width=10, text=totals[total])
        values.grid(row=1, column=total)
    try:
        total_purcentage = round(float(totals[2]) * 100 / float(totals[3]), 0)
        values = Label(total_frame, width=10, text=f"{total_purcentage}%")
    except:
        total_purcentage = 0
        values = Label(total_frame, width=10, text="0%")
    values.grid(row=1, column=4)

    progress_rect = Canvas(total_frame, width=100, height=20, bg="white", bd=0, highlightthickness=0)
    if total_purcentage == 0:
        progress_rect.create_rectangle(0, 0, 1, 20, fill=get_color(total_purcentage), outline="")
    else:
        progress_rect.create_rectangle(0, 0, total_purcentage, 20, fill=get_color(total_purcentage), outline="")
    progress_rect.grid(row=1, column=5)


if __name__ == "__main__":
    display_result()
