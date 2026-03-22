#import pandas as pd
#import numpy as np
import sqlite3

conn = sqlite3.connect('./assets/bds.db')
# Leer datos desde una tabla
#df = pd.read_sql_query("SELECT * FROM mi_tabla", conn)

cursor = conn.cursor()
#imprime el nombre de las tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()