import mysql.connector
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


def add_results(username, duration,nb_ok, nb_total, title_exercice):
    cursor = db_connection.cursor()
    # Here we will create the now time
    date_hour = time.strftime('%Y-%m-%d %H-%M-%S')

    query = "insert into results (username, start_date_hour, duration, nb_ok, nb_total, exercice_id) values (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query,(username, date_hour, duration, nb_ok, nb_total, title_exercice))
    affected_rows = cursor.rowcount
    cursor.close()
    if affected_rows == 1:
        return True
    else:
        return False

def get_exercice_name(id):
    open_dbconnection()
    try:
        cursor = db_connection.cursor()
        query = "Select name from exercices where id=%s"
        cursor.execute(query, (id, ))
        result = cursor.fetchone()
    except:
        result=200
    close_dbconnection()
    return result



def get_exercise_id(name):
    try:
        cursor = db_connection.cursor()
        query = "Select id from exercices where name=%s"
        cursor.execute(query, (name, ))
        result = cursor.fetchone()[0]
    except:
        result = "Failed"
    return result

def infos_results(pseudo, exercise):
    open_dbconnection()
    infos = []
    cursor = db_connection.cursor()

    query = "SELECT username, start_date_hour, duration, exercice_id, nb_ok, nb_total FROM results "

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