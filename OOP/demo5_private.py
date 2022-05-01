class Bank():
    def __init__(self,hoten,cmt):
        self.hoten = hoten
        self.cmt = cmt

class NhanVien(Bank):
    def __init__(self, hoten, cmt):
        super().__init__(hoten, cmt)
        self.__luong = 5000  # dùng 2 dấu gạch dưới __ gán private không cho phép truy cập từ bên ngoài

        # code giups HR-department - pHòng ban - có thể truy cập , can thiệp vào lương
    def get_luong(seft):
        return seft.__luong
    
    def set_luong(seft,luong_moi):
        seft.__luong = luong_moi


nv1 = NhanVien("Mai",1234)
# print(nv1.cmt,nv1.hoten)
# print(dir(nv1)) # dùng dir để check các attribute trong object

nv1.set_luong(88888888)
print('luong moi nhan vien 1 la : ',nv1.get_luong())