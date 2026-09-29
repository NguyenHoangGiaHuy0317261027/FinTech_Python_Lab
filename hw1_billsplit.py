# Nhập các giá trị đầu vào từ bàn phím
X = float(input("Nhập tổng hóa đơn X (đồng): "))
Y = float(input("Nhập phần trăm tip Y (%): "))
N = int(input("Nhập số người chia tiền N: "))

# 1. Tính tổng số tiền sau khi đã cộng thêm tiền tip
tong_tien_gom_tip = X * (1 + Y / 100)

# 2. Chia đều cho N người và làm tròn đến số nguyên (0 chữ số thập phân)
so_tien_moi_nguoi = round(tong_tien_gom_tip / N)

# In kết quả ra màn hình
print(f"👉 Số tiền thực tế mỗi người phải trả là: {so_tien_moi_nguoi} đồng")

