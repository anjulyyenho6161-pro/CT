class Node:
    def __init__(self, matb, tentb, soluong, dongia):
        self.matb = matb
        self.tentb = tentb
        self.soluong = soluong
        self.dongia = dongia
        self.next = None

class Dslktb:
    def __init__(self):
        self.head = None

    # b. Thêm thiết bị vào cuối danh sách
    def themcuoi(self, matb, tentb, soluong, dongia):
        new_node = Node(matb, tentb, soluong, dongia)
        if self.head is None:
            self.head = new_node
            return
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = new_node

    # b. Xuất danh sách thiết bị
    def indstb(self):
        if self.head is None:
            print("Danh sách không có thiết bị nào!")
            return
        print(f"{'Mã TB':<10}{'Tên TB':<25}{'Số lượng':<15}{'Đơn giá':<10}")
        print("-" * 60)
        p = self.head
        while p is not None:
            print(f"{p.matb:<10}{p.tentb:<25}{p.soluong:<15}{p.dongia:<10}")
            p = p.next
        print("None")

    # b. Tìm thiết bị theo mã
    def timkiem(self, matb):
        p = self.head
        while p is not None:
            if p.matb == matb:
                return p
            p = p.next
        return None

    # c. Tính tổng giá trị tất cả thiết bị trong phòng thực hành
    def tinhtonggiatri(self):
        tong = 0
        p = self.head
        while p is not None:
            tong += p.soluong * p.dongia
            p = p.next
        return tong

    # d. Đếm số thiết bị có số lượng bằng X
    def demtheosoluong(self, x):
        dem = 0
        p = self.head
        while p is not None:
            if p.soluong == x:
                dem += 1
            p = p.next
        return dem

# --- CHẠY THỬ NGHIỆM CHƯƠNG TRÌNH ---
ds = Dslktb()

# Thêm dữ liệu mẫu
ds.themcuoi(1, "kéo", 6, 5000)
ds.themcuoi(3, "giấy", 500, 20000)
ds.themcuoi(2, "máy tính", 3, 8000000)
ds.themcuoi(4, "bảng", 2, 50000)

# Xuất danh sách
print("--- DANH SÁCH THIẾT BỊ ---")
ds.indstb()

# Tính tổng giá trị thiết bị trong phòng (Yêu cầu c)
tong_tien = ds.tinhtonggiatri()
print(f"\nTổng giá trị tất cả thiết bị trong phòng thực hành: {tong_tien:,.2f} VNĐ")

# Tìm kiếm thiết bị theo mã (Yêu cầu b)
ma_can_tim = 2
ket_qua = ds.timkiem(ma_can_tim)
if ket_qua is not None:
    print(f"\nTìm thấy thiết bị có mã {ma_can_tim}: {ket_qua.tentb} (Số lượng: {ket_qua.soluong}, Đơn giá: {ket_qua.dongia})")
else:
    print(f"\nKhông tìm thấy thiết bị có mã {ma_can_tim} trong danh sách.")

# Đếm thiết bị theo số lượng X (Yêu cầu d)
x = 6
so_luong_thiet_bi = ds.demtheosoluong(x)
print(f"Số lượng thiết bị có số lượng bằng {x} là: {so_luong_thiet_bi}")