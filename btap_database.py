import sqlite3
import pandas as pd
conn = sqlite3.connect("Chinook_Sqlite.sqlite")
hoa_don = pd.read_sql("SELECT * FROM Invoice", conn)
khach = pd.read_sql("SELECT * FROM Customer", conn)

print(hoa_don.head(10))
#tổng doanh thu
print(hoa_don.groupby("BillingState")["Total"].sum())
#hoa đơn trung bình
print(hoa_don["Total"].mean())
#Hóa đơn lớn nhất
print(hoa_don["Total"].max())

#2.Có bao nhiêu hóa đơn từ Brazil?
print((hoa_don["BillingCountry"]== "Brazil").sum())
#3.Lấy top 5 quốc gia có doanh thu cao nhất. Gợi ý: groupby, rồi sort_values, rồi head.
print((hoa_don.groupby("BillingCountry")["Total"]).sum().sort_values(ascending=False).head(5))
#4. Với bảng khach: mỗi quốc gia có bao nhiêu khách hàng? Gợi ý: value_counts().
print((khach["Country"]).value_counts())
#5 Vậy câu trả lời chuẩn là: and chỉ xử lý được một giá trị, còn & xử lý được từng dòng trong cột.
# cũng như nếu không đóng () sau & thì nó sẽ hiểu điều kiện (1 & 2) chứ không phải là điều kiện 1 & điều kiện 2