f = open("PYTHON/work_file/sinhvien.txt","a",encoding="utf-8")
while True:
    mssv = input('Nhap mssv: ')
    if mssv == "":
        break
    ten_sv = input('Nhap ten: ')
    lop = input('Nhap lop: ')
    que_quan = input('Nhap que quan: ')
    f.write('\t'.join([mssv,ten_sv,lop,que_quan])+ "\n")
f.close()

f= open("PYTHON/work_file/sinhvien.txt","r",encoding="utf-8")
print("\t".join(["MSSV","Ten","Lop","Que quan"]))
for sv in f.readlines():
    print(sv.replace("\n",""))
f.close()