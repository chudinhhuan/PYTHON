
from bai9 import *
masp = input('Nhap ma san pham:')
name_sp = input('Nhap ten san pham:')
dongia = float(input('Nhap gia san pham:'))
line = masp + ';' + name_sp + ';' + str(dongia)

SaveFile('D:\PYTHON\LEARN\progaming\databaseSP.txt',line)
