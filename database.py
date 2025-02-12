"""
PROJ_DBPY
Datbase MYSQL
Modified by Judah Periyasamy
15/12/23
"""

import mysql.connector, bcrypt
import time
from geo01 import *


# Function that will open a connection in MySQL
def open_dbconnection():
    global db_connection
    db_connection = mysql.connector.connect(host='127.0.0.1', port='3306',
                                            user='judah', password='Pa$$w0rd', database='projet_dbpy',
                                            buffered=True, autocommit=True)
    return db_connection


# Function that will close the connection in MySQL
def close_dbconnection():
    db_connection.close()


# Function that will add a value row in the table results for each time we finish an exercice
def add_results(username, duration, nb_ok, nb_total, title_exercice):
    cursor = db_connection.cursor()
    # Here we will create the now time
    date_hour = time.strftime('%Y-%m-%d %H-%M-%S')
    query = "insert into results (username, start_date_hour, duration, nb_ok, nb_total, exercice_id, user_id) values (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (username, date_hour, duration, nb_ok, nb_total, title_exercice, 1))
    affected_rows = cursor.rowcount
    cursor.close()
    if affected_rows == 1:
        return True
    else:
        return False


# Funtion that will get the name using the exercice id
def get_exercice_name(id):
    open_dbconnection()
    try:
        cursor = db_connection.cursor()
        query = "Select name from exercices where id=%s"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
    except:
        result = 200
    close_dbconnection()
    return result


# Funtion that will get the id using the exercice name
def get_exercise_id(name):
    try:
        cursor = db_connection.cursor()
        query = "Select id from exercices where name=%s"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
    except:
        result = "Failed"
    return result


# Function that will get all the values stocked in the table results
def infos_results(pseudo, exercise):
    open_dbconnection()
    infos = []
    cursor = db_connection.cursor()

    query = "SELECT username, start_date_hour, duration, exercice_id, nb_ok, nb_total, id FROM results "

    # Here we are gonna separates conditions for each scenario using the where condition and then added to the main query
    if pseudo != "" and exercise != "":
        query += "where username = %s AND exercice_id = %s"
        cursor.execute(query, (pseudo, get_exercise_id(exercise)))
    elif pseudo != "":
        query += "where username = %s"
        cursor.execute(query, (pseudo,))
    elif exercise != "":
        query += "where exercice_id = %s"
        cursor.execute(query, (get_exercise_id(exercise),))
    else:
        # No conditions specified, fetch all results
        cursor.execute(query)

    result = cursor.fetchall()
    infos.append(result)
    cursor.close()
    close_dbconnection()
    return infos


# Function that will get all the values stocked in the table results and make totals values
def total_result(pseudo, exercise):
    open_dbconnection()
    cursor = db_connection.cursor()
    query = "SELECT count(results.id), sum(duration),  sum(nb_ok), sum(nb_total) FROM results"

    # Here we are gonna separates conditions for each scenario using the where condition and then added to the main query
    if pseudo != "" and exercise != "":
        query += " where username = %s AND exercice_id = %s"
        cursor.execute(query, (pseudo, get_exercise_id(exercise)))
    elif pseudo != "":
        query += " where username = %s"
        cursor.execute(query, (pseudo,))
    elif exercise != "":
        query += " where exercice_id = %s"
        cursor.execute(query, (get_exercise_id(exercise),))
    else:
        # No conditions specified, fetch all results
        cursor.execute(query)

    results = cursor.fetchall()[0]
    total_time = time.strftime("%H:%M:%S", time.gmtime(float(results[1])))
    total_data = (results[0], total_time, int(results[2]), int(results[3]))
    cursor.close()
    return total_data


# Function that will delete results depending on the user
def result_deletion(id):
    open_dbconnection()
    cursor = db_connection.cursor()
    query = "DELETE FROM results WHERE id=%s"
    cursor.execute(query, (id,))
    return


# # Function that will modify results depending on the user
def result_modification(user_id, dataset):
    open_dbconnection()
    data = []
    for info in dataset:
        data.append(info)
    data.append(user_id)
    cursor = db_connection.cursor()
    query = "UPDATE results SET username = %s, start_date_hour = %s, duration = %s, nb_ok = %s, nb_total = %s, exercice_id = %s WHERE id=%s"
    cursor.execute(query, data)


# # Function that will create results depending on the user
def create_results(username, date_hour, duration, nb_ok, nb_total, title_exercice, user_id):
    open_dbconnection()
    cursor = db_connection.cursor()
    # Here we will create the now time
    # date_hour = time.strftime('%Y-%m-%d %H-%M-%S')
    query = "insert into results (username, start_date_hour, duration, nb_ok, nb_total, exercice_id, user_id) values (%s, %s, %s, %s, %s, %s,%s)"
    cursor.execute(query, (username, date_hour, duration, nb_ok, nb_total, title_exercice, user_id))
    affected_rows = cursor.rowcount
    cursor.close()
    close_dbconnection()
    if affected_rows == 1:
        return True
    else:
        return False


# Function that will check if the user exists in the database
def login_user(username, password):
    open_dbconnection()
    cursor = db_connection.cursor()

    query = "SELECT id, password, level FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    user_data = cursor.fetchone()
    cursor.close()
    close_dbconnection()

    if user_data and bcrypt.checkpw(password.encode('utf-8'), user_data[1].encode('utf-8')):
        return {'id': user_data[0], 'username': username, 'level': user_data[2]}
    else:
        return False


# Function that will create a new user
def create_user(username, password, level=1):
    open_dbconnection()
    cursor = db_connection.cursor()
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    query = "INSERT INTO users (username, password, level, salt) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (username, hashed_password.decode('utf-8'), level, salt.decode('utf-8')))

    cursor.close()
    close_dbconnection()


# Function that will update users level
def update_user_info(username, level):
    open_dbconnection()
    try:
        cursor = db_connection.cursor()
        query = "UPDATE users SET level = %s WHERE username = %s"
        cursor.execute(query, (level, username))
        db_connection.commit()
        cursor.close()
    except Exception as e:
        print("ERROR")
    close_dbconnection()


# Function that will check if there's already an admin account
def check_admin_exists():
    open_dbconnection()
    cursor = db_connection.cursor()
    query = "SELECT * FROM users WHERE username = 'Admin' AND level = 2"
    cursor.execute(query)
    admin_exists = cursor.fetchone()
    cursor.close()
    close_dbconnection()
    return admin_exists


def get_user_info(username):
    try:
        open_dbconnection()
        cursor = db_connection.cursor()

        query = "SELECT id, level FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user_data = cursor.fetchone()
        cursor.close()
        close_dbconnection()

        print("User data:", user_data)  # Ajout de cette ligne pour déboguer

        if user_data:
            return user_data[0], user_data[1]
        else:
            return None
    except Exception as e:
        print("Error in get_user_info:", e)
        return None
