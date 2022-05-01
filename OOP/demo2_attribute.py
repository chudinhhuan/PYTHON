class SinhVien():
    def __init__(self,hoten,mssv,que_quan):
        self.hoten = hoten
        self.mssv = mssv
        self.que_quan = que_quan

sv1 = SinhVien("Chu Dinh Huan","N19DCVT013","Nghe An")
sv2 = SinhVien("Huan Dinh Chu","N19DCVT016","Ha Noi")
sv2 = SinhVien("Nguyen Van A","N19DCVT019","Lap Cai")

print(f'Sinh vien 1 te la {sv1.hoten},que o {sv1.que_quan}')

