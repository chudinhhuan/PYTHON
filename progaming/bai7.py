# # can le trai phai giua
# # center , ljust , rjust
# s1 = 'http://dinhhuanchu.com'
# print(s1)
# print(len(s1))
# print(s1.__len__())

# print(s1.rjust(32,' '))
# print(s1.ljust(32,'*'))

# start1 = '*'
# start2 = '**'
# start3 = '***'
# start4 = '****'
# print(start1.center(4))
# print(start2.center(4))
# print(start3.center(4))
# print(start4.center(4))

# ----------------

# # xoa ky tu du thua
# s = '     hello huan     ok   '
# print(s,s.__len__())
# s1 = s.strip()
# print(s1,s1.__len__())

#  ***********

# startswith -> check chuoi co bat dau bang mot chuoi con khong
# endswith -> check chuoi co ket thuc bang mot chuoi con khong



# s = 'C:/mussic/bolero/longme.mp3'
# if s.endswith('.mp3'):
#     print('bai hat dinh dang mp3')
# else:
#     print('khong phai mp3')

# def LocSODienThoai(dauso):
#     ls_So = []
#     dsArr = ['0923454213','0923456432','0325776754','0902345654','0902456943']
#     for phone in dsArr:
#         if (phone.startswith(dauso)):
#             ls_So.append(phone)
#     return ls_So
# print(LocSODienThoai('090'))

# # **** format and subtring
# s = 'D:/tailieu/python/lamchupython.pdf'
# p = s.rfind('/')
# p2 = s.rfind('.')
# print(s[p+1:p2])

# #  tach chuoi - split
# s = 'sv009;Chu Dinh Huan;1/2/1999'
# arr = s.split(';')
# for x in arr:
#     print(x)

# s1 = """Obama
#     hahaha
#     ali333"""
# arr1 = s1.splitlines() #tach theo dong
# for line in arr1:
#     print(line,'a->',line.count('a'))

# sSV = """n19vt012;Chu Dinh Huan;2/2/1992
#     n19vt011;Nguyen Van A;9/09/2001
#     n19vt093;Nguyen Van B;1/2/1998
# """
# arrSV = sSV.splitlines()
# for line_sv in arrSV:
#     arrInforSV = line_sv.strip().split(';')
#     if len(arrInforSV) == 3:
#         print(arrInforSV)

# ******* Noi chuoi -join
# # Check chuoi doi xung
# # s = 'maam' -> doi xung
# s = 'maam'
# def check_doi_xung(s):
#     flag = True
#     for i in range(len(s)):
#         if s[i] != s[-1-i]:
#             flag = False
#             break
#     return flag
# def main():
#     print('nhap mot chuoi : ')
#     s = input()
#     if (check_doi_xung(s)):
#         print('chuoi ban nhap doi xung')
#     else:
#         print('chuoi ban nhap khong doi xung')

# while True:
#     main()
#     print('tiep tuc nhap ko: ')
#     s = input()
#     if (s == 'k'):
#         break
# print('thank')

# ===== TOI UU CHUOI =====
# -> khong chua cac khoang trang du thua vaf cac tu cach nhau boi motj khoang trang

# def toi_uu_chuoi(s):
#     s2 = s
#     s2 = s2.strip()

#     arr = s2.split(' ')
#     s2 = ''
#     for x in arr:
#         word = x
#         if len(word.strip()) != 0:
#             s2 += word + ' '
#     return s2.strip()

# s = '   Chu    dinh  huan      '
# print(s,s.__len__())
# s1 = toi_uu_chuoi(s)
# print(s1,s1.__len__())
 
#   tach chuoi
from itertools import count


s = '5;7;8;-2;8;11;-13;9;10'
arr1 = s.split(';')
arr1_num = []
for i in arr1:
        arr1_num.append(int(i))
sochan = 0


def checkPrime(x):
    dem = 0
    for i in range(1,x+1):
        if x % i == 0:
            dem += 1
    return dem == 2
songuyento = 0
for j in arr1_num:
    if checkPrime(j):
        songuyento += 1
print(songuyento)

    