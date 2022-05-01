class sinhvien_nuocngoai():
    def __init__(self,hoten,mssv,que_quan):
        self.hoten = hoten
        self.mssv = mssv
        self.que_quan = que_quan
    
    def chao(seft):
        print('hello')

class sinhvien_vietnam():
    def __init__(self,hoten,mssv,que_quan):
        self.hoten = hoten
        self.mssv = mssv
        self.que_quan = que_quan
    
    def chao(seft):
        print('xin chao')

def hi(sinhvien_vietnam):
    sinhvien_vietnam.chao()

sv1 = sinhvien_nuocngoai('jack',123,'use')
sv2 = sinhvien_vietnam('Huan',432,'HO CHI MINH')
# sv1.chao()
# sv2.chao()

hi(sv1)
hi(sv2)