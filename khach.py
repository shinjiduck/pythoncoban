import sqlite3
import pandas as pd
conn = sqlite3.connect("Chinook_Sqlite.sqlite")
hoa_don = pd.read_sql("SELECT * FROM Invoice", conn)
khach = pd.read_sql("SELECT * FROM Customer", conn)

print(khach.columns)