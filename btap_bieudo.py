import matplotlib.pyplot as plt
import sqlite3
import pandas as pd
conn = sqlite3.connect("Chinook_Sqlite.sqlite")
hoa_don = pd.read_sql("SELECT * FROM Invoice", conn)
khach = pd.read_sql("SELECT * FROM Customer", conn)
#Vẽ biểu đồ cột nằm ngang cho số khách hàng theo quốc gia (dùng kết quả câu 4 hôm trước), chỉ lấy top 8 nước. Có tiêu đề, tên trục.
top8 = khach["Country"].value_counts().sort_values(ascending = False).head(8)

top8.plot(kind="barh", color="steelblue", edgecolor="black")
plt.title("biểu đồ thanh")
plt.xlabel("Số lượng khách")
plt.ylabel("Đất nước")
plt.tight_layout()
plt.savefig("top8_quoc_gia_co_so_luong_khach.png", dpi=150)
plt.show()
#Vẽ biểu đồ doanh thu theo năm (gợi ý: "Y" thay cho "M"). Nên dùng cột hay đường? Vì sao?
hoa_don["InvoiceDate"] = pd.to_datetime(hoa_don["InvoiceDate"])
theo_nam = hoa_don.groupby(hoa_don["InvoiceDate"].dt.to_period("Y"))["Total"].sum()
theo_nam.plot(kind="line", color="Blue")
plt.title("Doanh thu theo năm")
plt.xlabel ("Năm")
plt.ylabel ("Doanh thu")
plt.savefig("Biểu đồ đường thể hiện số quốc gia theo doanh thu.png", dpi=150)
plt.show()
#Lưu cả hai biểu đồ thành file .png.
#Viết 2 câu nhận xét cho mỗi biểu đồ theo mẫu: dữ liệu nói gì, ý nghĩa với kinh doanh.
#Nhận xét về biểu đồ thanh: dữ liệu cho thấy rằng nhóm cao là nhóm thuộc các nước Bắc Mỹ và Nam mỹ gồm Brazil, Canada và Mỹ và nó chiếm tỷ trọng cao. Còn nhóm thấp bao gồm Portugal Czech và Anh chiếm số lượng khách ít hơn so với phần còn lại
#Biểu đồ đường đạt đỉnh doanh thu theo năm từ các năm 2010-2012 nguyên do chắc là do .... và cùng với đó doanh thu giảm dần tiếp theo từ 2012-2013 giảm 25...$