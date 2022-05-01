#Bai1: viet ham xu ly dem ki tu va so trong list 
print('bai 1 ')

def my_funct1(lst):
	#li=lst
	dem_so=0
	dem_chu=0
	for a in lst:
		if type(a) == int or type(a)==float :
			dem_so+=1
		else:
			dem_chu+=1
	print(['so chu so trong list:  ',dem_so,'so ki tu chuoi trong list : ',dem_chu])
	#return [dem_so,dem_chu]
lst=[1,2,3,4,6,7,8,'a','c','d']

#[b,c]=my_funct1(lst)
#print([b,c])

my_funct1(lst)

#Bai 2: biet ham tinh trung binh cong so chan va so le
print('bai 2')

def my_funct2(lib):
	li=lib
	dem_chan=0
	dem_le=0
	tong_chan=0
	tong_le=0
	for a in li:
		if a%2==0:
			tong_chan+=a
			dem_chan+=1
		else:
			tong_le+=a
			dem_le+=1
	tb_chan=tong_chan/dem_chan
	tb_le=tong_le/dem_le
	print('Tb chan le lan luot la : ',[tb_chan,tb_le])


lib=[1,2,3,4,5,6,7,8,9,10]
my_funct2(lib)

# Bai 3 : xoa ki tu thua va khoang trang trung lap 

def xoa_khoang_trang_lien_ke(s):
	s=s.strip()  #xoa  khoang thua   dau va cuoi char

	while '  'in s:
		s=s.replace('  ',' ')
	return s

def my_funct3(s):
	#s=xoa_khoang_trang(s)
	char_thua=set([',',':','<','>','|','?','/',';'])
	new_s=''
	for a in s:
		if a in char_thua:
			new_s+=''
		else:
			new_s+=a

	new_s=xoa_khoang_trang_lien_ke(new_s)
	print(new_s)
char='        I go       to school, that;;;;     school is::::    PTIT  '

print('Bai 3')
my_funct3(char)


#Bai 4 viet lai thuat toan buble sort

print('Bai4====')

m=[6,5,3,1,8,7,2,4]
lst=range(len(m)-1,-1,-1)
for i in lst:
	for j in range(0,i,1):   # for j=0 ;j<i;j++ 
		if m[j]<m[j+1]:
			tam=m[j]
			m[j]=m[j+1]
			m[j+1]=tam
print(m)


p=[1,0,4,7,5,2]
l=range(0,len(p),1)
for a in l:
	for b in range(0,len(p)-a-1,1):
		if p[b]<p[b+1]:
			tamp=p[b]
			p[b]=p[b+1]
			p[b+1]=tamp
print(p)

# bai 5 tron 2 dict voi nhau va tra ve dict moi  voi cac keys trung nhau
print('bai 5=============')

dict1 = {
	'a':5,
	'b':10,
	'c':3
}
dict2 = { 

	'e':2,
	'b':13
}

def my_funct5(dict1,dict2): 
	dict_new=dict()
	for key,value in dict1.items():
		dict_new[key]=value
	for key,value in dict2.items():
		dict_new[key]=value
	for key1,value1 in dict1.items():
		for key2,value2 in dict2.items():
			if key1==key2:
				dict_new[key1]=value1+value2

	return dict_new
print(my_funct5(dict1,dict2))


