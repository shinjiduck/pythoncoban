import matplotlib.pyplot as plt
import sqlite3
import pandas as pd
conn = sqlite3.connect("Chinook_Sqlite.sqlite")
hoa_don = pd.read_sql("SELECT * FROM Invoice", conn)
khach = pd.read_sql("SELECT * FROM Customer", conn)

top5 = (hoa_don.groupby("BillingCountry")["Total"]
               .sum()
               .sort_values(ascending=False)
               .head(5))

top5.plot(kind="bar", color="steelblue")
plt.title("Top 5 quốc gia theo doanh thu")
plt.xlabel("Quốc gia")
plt.ylabel("Doanh thu ($)")
plt.xticks(rotation=0)        # tên nước nằm ngang, không bị xoay
plt.tight_layout()            # tự căn lề để chữ không bị cắt
plt.show()

hoa_don["InvoiceDate"] = pd.to_datetime(hoa_don["InvoiceDate"])

theo_thang = hoa_don.groupby(hoa_don["InvoiceDate"].dt.to_period("M"))["Total"].sum()

theo_thang.plot(kind="line", marker="o", figsize=(12, 5))
plt.title("Doanh thu theo tháng")
plt.ylabel("Doanh thu ($)")
plt.grid(alpha=0.3)
plt.show()

hoa_don["Total"].plot(kind="hist", bins=20, edgecolor="black")
plt.title("Phân bố giá trị hóa đơn")
plt.xlabel("Giá trị hóa đơn ($)")
plt.ylabel("Số hóa đơn")
plt.show()

plt.savefig("top5_quoc_gia.png", dpi=150)
plt.show()