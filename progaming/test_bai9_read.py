from bai9 import *
dssp = ReadFile('D:\PYTHON\LEARN\progaming\databaseSP.txt')

def XuatSanPham(dssp):
    for row in dssp:
        for element in row:
            print(element,end="\t")
        print()

# XuatSanPham(dssp)

def SortSp(dssp):
    for i in range(len(dssp)):
        for j in range(len(dssp)):
            a = dssp[i]
            b = dssp[j]
            if a[2] > b[2]:
                dssp[i] = b
                dssp[j] = a

SortSp(dssp)
print('khi da sap xep \n')
XuatSanPham(dssp) 