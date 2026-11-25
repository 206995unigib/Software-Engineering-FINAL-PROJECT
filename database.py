# database.py - the only file that talks to the SQLite database (app.db).
# Planned functions:
#   get_connection()      -> opens app.db
#   create_table()        -> CREATE TABLE IF NOT EXISTS
#   add_vehicle(...)      -> INSERT
#   get_vehicle(search)   -> SELECT (all, or by brand/plate)
#   delete_vehicle(plate) -> DELETE

import sqlite3

# Reversibility: all the SQL is in this file, so changing the database only touches here.
DB_NAME = "app.db"


# creating a function that returns the connection with the database.
# as i am using the connection in multiple functions, the DRY principle is applied.
def get_connection():
    return sqlite3.connect(DB_NAME)
# it creates the database the first time it runs,
# that is, in create_table. then, every time it runs
# in other functions, it opens that connection.
# the first time it creates it, then it opens it.
# conn = get_connection lets conn access
# the database through functions
# conn.execute, conn.close, conn.commit......


def create_table():
    conn = get_connection()  # 'conn' now has access to the database. it can send requests.
    conn.execute("""
        CREATE TABLE IF NOT EXISTS vehicles (
            plate TEXT PRIMARY KEY,
            brand TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL,
            price REAL NOT NULL,
            km INTEGER NOT NULL
        )
    """)
    conn.commit()  # SAVES CHANGES ON THE disc
    conn.close()  # CLOSES THE CONNECTION


def add_vehicle(plate, brand, model, year, price, km):
    conn = get_connection()
    conn.execute("""
        INSERT INTO vehicles (plate, brand, model, year, price, km) VALUES (?, ?, ?, ?, ?, ?)
    """, (plate, brand, model, year, price, km))
    conn.commit()  # SAVE CHANGES ON THE DISC
    conn.close()  # CLOSE CONNECTION


def delete_vehicle(plate):  # ab 038 hk
    conn = get_connection()
    conn.execute(" DELETE FROM vehicles WHERE plate = ?", (plate,))
    conn.commit()
    conn.close()

# row = [tuple,] -- so the list is not empty != 0 -- so true.


def plate_exists(plate):
    conn = get_connection()
    row = conn.execute("SELECT plate FROM vehicles WHERE plate = ?", (plate,)).fetchall()
    conn.close()
    if len(row) == 0:
        return False
    else:
        return True


def get_vehicle(search=""):  # default value.
    # fetchall() brings the results of the query and stores them as a list (of rows.)
    conn = get_connection()  # opening the connection to the database.
    if search == "":  # if this is true, the user didn't type a brand to filter
        rows = conn.execute("SELECT * FROM vehicles").fetchall()
    else:
        rows = conn.execute("SELECT * FROM vehicles WHERE brand = ? OR plate = ?", (search, search)).fetchall()
    conn.close()
    return rows
