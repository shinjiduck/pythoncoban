# BÀI TẬP TUẦN 1 - Quản lý điểm học sinh
# Làm xong, nhắn "chấm bài" để mình chấm nhé!

# ---------- Bài 1: Biến, input, in ra (1 điểm) ----------
# Nhập tên và tuổi của bạn, in ra: "Xin chào <tên>, năm sau bạn <tuổi+1> tuổi!"
from itertools import count

from pgvector.sqlalchemy import avg


print(f"tên: {input('Nhập tên:')}, năm sau mình: {int(input('Nhập tuổi:'))+1} tuổi")

# ---------- Bài 2: Chẵn / lẻ (2 điểm) ----------
# Nhập 1 số nguyên. In ra "chan" nếu chẵn, "le" nếu lẻ.
songuyen = int(input("nhập số nguyên: "))
if songuyen % 2==0:
    print("chẵn")
else:
    print("lẻ")

# ---------- Bài 3: Vòng lặp (2 điểm) ----------
# In ra tổng các số từ 1 đến 100.
# In ra các số chia hết cho 3 trong khoảng 1..30 (trên 1 dòng, cách nhau dấu cách).
x = 1
while x<=100:
    print(x, end=" ")
    x+=1

# ---------- Bài 4: Hàm (2 điểm) ----------
# Viết hàm xep_loai(diem) trả về:
#   >= 8.0 -> "Gioi", >= 6.5 -> "Kha", >= 5.0 -> "Trung binh", còn lại -> "Yeu"
# Test: xep_loai(9), xep_loai(7), xep_loai(5.5), xep_loai(3)
diem = float(input("Nhap diem: "))
if diem >= 8.0:
    print("gioi")
elif diem >= 6.5:
    print("kha")
elif diem >= 5.0:
    print("trung binh")
else:
    print("yeu")

# ---------- Bài 5: List (3 điểm) ----------
# Cho danh sách điểm: diem = [7.5, 8, 5, 9.5, 4, 6.5]
# a) In điểm cao nhất, thấp nhất, điểm trung bình (làm tròn 2 chữ số)
# b) Đếm có bao nhiêu bạn đạt từ 5 điểm trở lên
# c) In ra xếp loại của từng điểm bằng hàm ở Bài 4, dạng: "7.5 -> Kha"
diem = [7.5, 8, 5, 9.5, 4, 6.5]
#a
print(f"điểm cao nhất: {max(diem)}, điểm thấp nhất: {min(diem)}, điểm trung bình: {round(avg(diem), 2)}")
#b
count = sum(1 for d in diem if d >= 5)
print(f"Số bạn đạt từ 5 điểm trở lên: {count}")
#c
for d in diem:
    if d >= 8.0:
        print(f"{d} -> Gioi")
    elif d >= 6.5:
        print(f"{d} -> Kha")
    elif d >= 5.0:
        print(f"{d} -> Trung binh")
    else:
        print(f"{d} -> Yeu")