import sqlite3
import pandas as pd
from sqlalchemy import create_engine, event
from sqlalchemy.engine import URL

# 1. Kết nối SQLite
sqlite_conn = sqlite3.connect("Chinook_Sqlite.sqlite")

# 2. Kết nối SQL Server
url = URL.create(
    "mssql+pyodbc",
    host=r"localhost",
    database="Chinook",
    query={
        "driver": "ODBC Driver 17 for SQL Server",
        "trusted_connection": "yes",
    },
)

engine = create_engine(url)

# 3. Lấy danh sách bảng
tables = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table' "
    "AND name NOT LIKE 'sqlite_%'",
    sqlite_conn,
)

# 4. Chuyển dữ liệu
for table in tables["name"]:
    print(f"Đang chuyển bảng: {table}")

    df = pd.read_sql_query(
        f'SELECT * FROM "{table}"',
        sqlite_conn,
    )

    df.to_sql(
        name=table,
        con=engine,
        if_exists="replace",
        index=False,
        chunksize=1000,
    )

    print(f"Hoàn thành: {len(df)} dòng")

sqlite_conn.close()
engine.dispose()

print("Đã chuyển dữ liệu!")