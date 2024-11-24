class PhuongTien: # đóng gói
    def __init__(self, loai_xe, hang_xe, mau_sac, so_cho_ngoi, so_banh_xe, gia_tien):
        self.loai_xe = loai_xe
        self.hang_xe = hang_xe
        self.mau_sac = mau_sac
        self.so_cho_ngoi = so_cho_ngoi
        self.so_banh_xe = so_banh_xe
        self.gia_tien = gia_tien
    def ThongTin(self):
        print("Loại xe:", self.loai_xe)
        print("Hãng xe:", self.hang_xe)
        print("Mùa sắc xe:", self.mau_sac)
        print("Số chỗ ngồi xe:", self.so_cho_ngoi)
        print("Số bánh xe:", self.so_banh_xe)
        print("Giá tiền xe:", self.gia_tien)
vehicle1 = PhuongTien("Xe_hoi", "Ford", "red", 7, 4, 50000000)
vehicle1.ThongTin()

# vehicle1 = PhuongTien("Xe_hoi", "Ford", "red", 7, 4, 50000000)
# print("Loại xe:", vehicle1.loai_xe)
# print("Hãng xe:", vehicle1.hang_xe)
# print("Màu sắc xe:", vehicle1.mau_sac)
# print("Số chỗ ngồi xe:", vehicle1.so_cho_ngoi)
# print("Số bánh xe:", vehicle1.so_banh_xe)
# print("Giá tiền của xe:", vehicle1.gia_tien)

class Pet:
    def __init__ (self, name, type, color, age, weight):
        self.name = name
        self.type = type
        self.color = color
        self.age = age
        self.weight = weight
    def Info(self): # viết hoa chữ cái đầu
     print("Tên thú cưng:", self.name)
     print("Giống thú cưng:", self.type)
     print("Màu sắc thú cưng:", self.color)
     print("Tuổi thú cưng:", self.age)
     print("Cân nặng thú cưng:", self.weight)
Animal1 = Pet("Lucky", "Husky", "white", 4, 10)
Animal1.Info()

class Xe:
    def __init__(self,hang_xe, mau_sac, gia_tien):
        self.hang_xe = hang_xe
        self.mau_sac = mau_sac
        self.gia_tien = gia_tien
    def Khoi_Dong(self):
        print("Xe", self.hang_xe, "đang khởi động.")

class XeHoi(Xe):
    def Chay_Bang_Bon_Banh(self):
        print("Xe", self.hang_xe, "đang chạy về phía trước bằng động cơ.")

class XeDap(Xe):
    def Chay_Bang_Hai_Chan(self):
        print("Xe", self.hang_xe, "đang chạy về phía trước bằng động cơ.")
        
xedap1 = XeDap("Martin", "red", 5000000)
xedap1.Khoi_Dong()
xedap1.Chay_Bang_Hai_Chan()

xehoi1 = XeHoi("Ford", "white", 50000000)
xehoi1.Khoi_Dong()
xehoi1.Chay_Bang_Bon_Banh()





