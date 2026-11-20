# database.py - the only file that talks to the SQLite database (app.db).
# Planned functions:
#   get_connection()      -> opens app.db
#   create_table()        -> CREATE TABLE IF NOT EXISTS
#   add_vehicle(...)      -> INSERT
#   get_vehicles()        -> SELECT *
#   delete_vehicle(plate) -> DELETE

import sqlite3

DB_NAME = "app.db"

# creating a function that returns the connection with the database.
# as i am using the connection in multiple functions, the DRY principle is applied. 
def get_connection(): 
    return sqlite3.connect(DB_NAME)
# crea la base de datos la primera vez que la ejectuan'
# osea, en create_table. luego, cada vez que la ejecutan
# en otras funciones, abre esa conexion
# la primera vez la crea, luego la abre.
# conn = getconecction hace que conn pueda acceder a 
# a la base de datos mediante funciones
# conn.execute, conn.close, conn.commit......

def create_table():
    conn = get_connection() # 'conn' now has access to the database. it can send requests.
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
    conn.commit() # SAVES CHANGES ON THE disc
    conn.close() # CLOSES THE CONNECTION


def add_vehicle(plate, brand, model, year, price, km):
    conn = get_connection()
    conn.execute("""
        INSERT INTO vehicles (plate, brand, model, year, price, km) VALUES (?, ?, ?, ?, ?, ?)
    """, (plate, brand, model, year, price, km))
    conn.commit() # SAVE CHANGES ON THE FILE
    conn.close() # CLOSE CONNECTION



def get_vehicle(search=""): # valor por defecto.

    #fetchall() trae los resultados de la consulta y los guarda como lista (en raws. )

    conn = get_connection() # estableciendo conexion a la base de datos. 
    if search == "": # si ese valor se cumple, es decir, el usuario no ingresa brand para filtrar
        rows = conn.execute("SELECT * FROM vehicles").fetchall()

    else: 
        rows = conn.execute("SELECT * FROM vehicles WHERE brand = ? OR plate = ?", (search,search)).fetchall()

    conn.close()
    return rows

res = get_vehicle("Nissan")
print(res)



def delete_vehicle(plate): # ab 038 hk
    conn = get_connection()
    conn.execute(" DELETE FROM vehicles WHERE plate = ?", (plate,))
    conn.commit()
    conn.close()




def plate_exists(plate):
    conn = get_connection()
    row = conn.execute("SELECT plate FROM vehicles WHERE plate = ?", (plate,)).fetchall()
    conn.close()
    if len(row) == 0:
        return False
    else:
        return True


