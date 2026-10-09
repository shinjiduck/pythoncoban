#Với gia_bai_hat = [0.99, 1.99, 0.99, 0.99, 1.99], in tổng tiền, giá cao nhất và số bài hát.
gia_bai_hat = [0.99, 1.99, 0.99, 0.99, 1.99]
def tinh_tien(gia_bai_hat):
    tong_tien = sum(gia_bai_hat)
    gia_cao_nhat = max(gia_bai_hat)
    so_bai_hat = len(gia_bai_hat)
    return tong_tien, gia_cao_nhat, so_bai_hat
tong_tien, gia_cao_nhat, so_bai_hat = tinh_tien(gia_bai_hat)
print("Tổng tiền:", tong_tien)
print("Giá cao nhất:", gia_cao_nhat)
print("Số bài hát:", so_bai_hat)

#Tạo dict hoa_don gồm ma_hd, quoc_gia, tong_tien. In quốc gia, sửa tong_tien thành 20, rồi in cả dict.
hoa_don = { "ma_hd": "HD001",
           "quoc_gia": "VN",
           "tong_tien":100}
hoa_don["tong_tien"] = 20
print(hoa_don["ma_hd"], hoa_don["quoc_gia"], hoa_don["tong_tien"])

#3. Dùng for để đếm xem trong gia_bai_hat có bao nhiêu bài giá 1.99. Gợi ý: tạo biến dem = 0, gặp bài giá 1.99 thì cộng thêm 1.

dem = 0
for gia in gia_bai_hat:
    if gia == 1.99:
        dem += 1
print(f"số bài hát giá 1.99: {dem}")

#4. Với ds_khach ở mục 3, in ra tên và hạng của từng khách, dùng hàm xep_hang. Kết quả mong muốn:
ds_khach = [
    {"ten": "Nam", "quoc_gia": "Vietnam", "tong_chi": 45},
    {"ten": "John", "quoc_gia": "USA", "tong_chi": 12},
    {"ten": "Anna", "quoc_gia": "Germany", "tong_chi": 30}
]

def xep_hang(tong_chi):
    if tong_chi >= 40:
        return "Kim Cuong"
    elif tong_chi >= 20:
        return "Vang"
    else:
        return "Thường"

for khach in ds_khach:
    ten = khach["ten"]
    hang = xep_hang(khach["tong_chi"])
    print (f"{ten} -> {hang}")
    