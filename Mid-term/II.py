class HocSinh:
    def __init__ (self, ho_va_ten, dia_chi, chieu_cao, can_nang, hoc_luc):
        self.ho_va_ten = ho_va_ten
        self.dia_chi = dia_chi
        self.chieu_cao = chieu_cao 
        self.can_nang = can_nang
        self.hoc_luc = hoc_luc
    def Dia_Chi_Moi(self, dia_chi_moi):
        self.dia_chi = dia_chi_moi
    def Chieu_cao_va_Can_nang_moi(self, chieu_cao_moi, can_nang_moi):
        self.chieu_cao = chieu_cao_moi
        self.can_nang = can_nang_moi
    def Xuat_Info(self):
        print("Họ và tên:", self.ho_va_ten)
        print("Địa chỉ:", self.dia_chi)
        print("Chiều cao:", self.chieu_cao)
        print("Cân nặng:", self.can_nang)
        print("Học lực:", self.hoc_luc)

hocsinh1 = HocSinh("Phạm Nguyễn Minh Hoàng", "C10, Đường N1, Phường Hiệp Thành, Quận 12, Thành phố Hồ Chí Minh", 165, 70, "Giỏi")
hocsinh1.Xuat_Info()
