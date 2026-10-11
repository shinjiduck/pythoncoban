import os
import sqlite3

import matplotlib.pyplot as plt
import pandas as pd

# Chạy từ bất kỳ thư mục nào vẫn tìm đúng database và thư mục images
THU_MUC = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(THU_MUC, "images"), exist_ok=True)

conn = sqlite3.connect(os.path.join(THU_MUC, "Chinook_Sqlite.sqlite"))
hoa_don = pd.read_sql("SELECT * FROM Invoice", conn)
khach = pd.read_sql("SELECT * FROM Customer", conn)
conn.close()

# Biểu đồ 1: top 8 quốc gia có nhiều khách hàng nhất (cột ngang)
top8 = khach["Country"].value_counts().head(8).sort_values()
plt.figure()
top8.plot(kind="barh", color="steelblue", edgecolor="black")
plt.title("Top 8 quốc gia có nhiều khách hàng nhất")
plt.xlabel("Số lượng khách")
plt.ylabel("Quốc gia")
plt.tight_layout()
plt.savefig(os.path.join(THU_MUC, "images", "top8_quoc_gia.png"), dpi=150)

# Biểu đồ 2: doanh thu theo năm (đường)
hoa_don["InvoiceDate"] = pd.to_datetime(hoa_don["InvoiceDate"])
theo_nam = hoa_don.groupby(hoa_don["InvoiceDate"].dt.year)["Total"].sum()
plt.figure()
theo_nam.plot(kind="line", color="blue", marker="o")
plt.title("Doanh thu theo năm")
plt.xlabel("Năm")
plt.ylabel("Doanh thu ($)")
plt.xticks(theo_nam.index)
plt.tight_layout()
plt.savefig(os.path.join(THU_MUC, "images", "doanh_thu_theo_nam.png"), dpi=150)

plt.show()
