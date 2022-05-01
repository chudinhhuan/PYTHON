#1 thao tac voi file
# open('myfile.txt','w') -> open file de write moi
# open('myfile.txt','a') -> open file de ghi noi duoi
# open('myfile.txt','r') -> open file de doc
# file.close()

def save_file(path):
    file = open(path,'w',encoding='utf-8')
    file.writelines('sinh vien1 ;Nguyen Van A;1998\n')
    file.writelines('sinh vien2;Nguyen Van B;1997\n')
    file.writelines('sinh vien3 ;Nguyen Van C;1996\n')

    file.close()

# save_file('D:\PYTHON\LEARN\progaming\csdlSinhVien.txt')

def ReadFile(path):
    file = open(path,'r',encoding='utf-8')
    for line in file:
        data = line.strip() #strip de xoa khoang trang du thua di
        print(data)
    file.close()
# ReadFile('D:\PYTHON\LEARN\progaming\csdlSinhVien.txt')
