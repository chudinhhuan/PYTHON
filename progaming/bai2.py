# kiem tra xem co 3 phan tu trong word 1 co trong word 2 ko 
# neu cos 3 thi return True con duoi return False
word1 = ''
word2 = 'abaaac'

def bai3(word1,word2):
    a = []
    b=[]
    for i in word1:
        a.append(i)
    for j in word2:
        b.append(j)   
    dem = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                dem += 1 
    dem = dem // 2
    flag = False
    if dem >= 3:
        flag = True
    return flag

print(bai3(word1,word2))

