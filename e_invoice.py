# e_invoice.py
# Bài tập 2: Tính hóa đơn bán lẻ thương mại điện tử
#
# Chương trình nhận tên sản phẩm, số lượng, đơn giá, sau đó tính:
#   Tổng tiền hàng  = Số lượng x Đơn giá
#   Thuế VAT        = 8% x Tổng tiền hàng
#   Tổng thanh toán = Tổng tiền hàng + Thuế VAT
# và in hóa đơn có định dạng số tiền phân cách hàng nghìn.

from datetime import datetime

# ----------------------------------------------------------------------
# HẰNG SỐ
# ----------------------------------------------------------------------
THUE_VAT = 0.08          # Thuế VAT 8%


# ----------------------------------------------------------------------
# CÁC HÀM NHẬP DỮ LIỆU (có kiểm tra, nhập sai thì yêu cầu nhập lại)
# ----------------------------------------------------------------------
def nhap_ten_san_pham(thong_bao):
    """Nhập tên sản phẩm, không được để trống."""
    while True:
        ten = input(thong_bao).strip()
        if ten != "":
            return ten
        print("  ! Tên sản phẩm không được để trống.")


def nhap_so_luong(thong_bao):
    """Nhập số lượng: phải là số nguyên (int) lớn hơn 0."""
    while True:
        try:
            so_luong = int(input(thong_bao))
        except ValueError:
            print("  ! Số lượng phải là số nguyên (ví dụ: 3).")
            continue

        if so_luong <= 0:
            print("  ! Số lượng phải lớn hơn 0.")
            continue

        return so_luong


def nhap_don_gia(thong_bao):
    """Nhập đơn giá: phải là số thực (float) lớn hơn 0."""
    while True:
        try:
            don_gia = float(input(thong_bao))
        except ValueError:
            print("  ! Đơn giá phải là một con số (ví dụ: 349000).")
            continue

        if don_gia <= 0:
            print("  ! Đơn giá phải lớn hơn 0.")
            continue

        return don_gia


# ----------------------------------------------------------------------
# CHƯƠNG TRÌNH CHÍNH
# ----------------------------------------------------------------------
print("=" * 52)
print("          LẬP HÓA ĐƠN BÁN LẺ ĐIỆN TỬ")
print("=" * 52)

# Bước 1: Nhập thông tin
ten_san_pham = nhap_ten_san_pham("Nhập tên sản phẩm     : ")
so_luong = nhap_so_luong("Nhập số lượng         : ")
don_gia = nhap_don_gia("Nhập đơn giá (VND)    : ")

# Bước 2: Tính toán
tong_tien_hang = so_luong * don_gia              # Tổng tiền hàng
tien_thue_vat = tong_tien_hang * THUE_VAT        # Thuế VAT 8%
tong_thanh_toan = tong_tien_hang + tien_thue_vat # Tổng thanh toán
thoi_gian = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Bước 3: In hóa đơn
print()
print("=" * 52)
print("               HÓA ĐƠN BÁN HÀNG")
print("=" * 52)
print(f"Ngày lập hóa đơn : {thoi_gian}")
print("-" * 52)
print(f"Sản phẩm         : {ten_san_pham}")
print(f"Số lượng         : {so_luong}")
print(f"Đơn giá          : {don_gia:>16,.0f} VND")
print("-" * 52)
print(f"Tổng tiền hàng   : {tong_tien_hang:>16,.0f} VND")
print(f"Thuế VAT (8%)    : {tien_thue_vat:>16,.0f} VND")
print("-" * 52)
print(f"TỔNG THANH TOÁN  : {tong_thanh_toan:>16,.0f} VND")
print("=" * 52)
print("Cảm ơn quý khách đã mua hàng!")
