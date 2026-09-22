PHI_MO_VI = 50000  # Phí mở tài khoản (VND)

# 1. Nhập thông tin
ho_ten = input("Nhập họ tên khách hàng: ")
so_dien_thoai = input("Nhập số điện thoại: ")
cccd = input("Nhập số CCCD: ")
so_tien_nap = float(input("Nhập số tiền nạp ban đầu (VND): "))

# 2. Tự động trừ phí mở tài khoản
so_du_kha_dung = so_tien_nap - PHI_MO_VI

# 3. In biên lai
print("=== BIÊN LAI KHỞI TẠO VÍ ===")
print(f"Họ tên         : {ho_ten.upper()}")
print(f"4 số cuối CCCD : {cccd[-4:]}")
print(f"Số tiền nạp    : {so_tien_nap:,.0f} VND")
print(f"Phí mở ví      : {PHI_MO_VI:,.0f} VND")
print(f"Số dư khả dụng : {so_du_kha_dung:,.0f} VND")
