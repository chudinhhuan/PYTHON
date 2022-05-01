# chuyen doi thap phan sang nhi phan
n = 77
out_1= ""
while (n > 0):
    out_1 += str(n % 2)
    n = n // 2
print(out_1)
# chuyen doi nhi sang thap
n = '1011001'
li_num = []
for a in n:
    li_num.append(int(a))

sum = 0
for i in range(len(li_num)):
    if li_num[i] == 1:
        sum += pow(2,i)
print(sum)