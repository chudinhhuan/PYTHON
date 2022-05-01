# lệnh  open()
#  <tên biến> = opend(file_name,mode,encoding)
#  có các mode sau:
#  r : mở file để đọc.con trỏ nằm ở bắt đầu file
#  r+ : mở file để đọc và ghi , con trỏ ở bắt đầu file
#  w : mở file chế độ ghi .nếu file tồn tại thì ghi đè lên tức là xóa và ghi content mới vào,chưa thì auto tạo file mới
#  w+ : đọc và ghi 
#  w chỉ mở file chứ ko cho phép đọc mà w+ mới vừa ghi vừa đọc
#  a : mở file chế độ append , trỏ cuối file ghi nối đuôi
# a++ : mở file đọc và append , trỏ cuối file



# nhap vao danh sach sinh vien
dssv = []
while True:
    mssv = input('Nhap mssv: ')
    if mssv == "":
        break
    ten_sv = input('Nhap ten: ')
    lop = input('Nhap lop: ')
    que_quan = input('Nhap que quan: ')
    dssv.append([mssv, ten_sv, lop, que_quan])
print('Danh sach sinh vien vua nhap: ')
print('\t'.join(['MSSV','Ho ten','Lop','Que quan']))
for i in dssv:
    print('\t'.join(i))

