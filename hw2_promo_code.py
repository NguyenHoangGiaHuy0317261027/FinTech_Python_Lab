# hw2_promo_code.py
# Máy phát sinh mã ưu đãi cá nhân hóa cho khách hàng

# 1. Nhập họ tên đầy đủ
full_name = input("Nhập họ tên đầy đủ: ").strip()

# 2. Nhập năm sinh
birth_year = input("Nhập năm sinh: ").strip()

# 3. Lấy từ cuối cùng (Tên) bằng split()
first_name = full_name.split()[-1]

# Lấy 3 chữ cái đầu của Tên (slicing) và viết hoa
prefix = first_name[0:3].upper()

# Ghép mã ưu đãi bằng f-string
promo_code = f"{prefix}-{birth_year}-VIP"

print("Mã ưu đãi của bạn:", promo_code)
