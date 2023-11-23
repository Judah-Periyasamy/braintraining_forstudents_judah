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

def infos_results():
    infos = []
    cursor = db_connection.cursor()
    query = "Select username, start_date_hour, duration, nb_ok, nb_total, exercice_id from results"
    cursor.execute(query)
    name = cursor.fetchall()
    infos.append(name)
    cursor.close()
    return infos