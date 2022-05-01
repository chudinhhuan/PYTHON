print('bai1')
def my_function1(lst):
	li=lst
	dem_so=0
	dem_chu=0
	tong=0
	for a in li:
		if type(a)==int or type(a)==float:
			dem_so+=1
			tong+=a
		else:
			dem_chu+=1
	print([tong,dem_chu])
lst=[1,2,4,'a','b',3]
my_function1(lst)

print('bai5')

dict1={
	'a':5,
	'b':10,
	'c':3
}
dict2={
	'a':2,
	'b':13,
	'e':2
}

def my_function5(dict1,dict2):
	dict_new=dict()
	for key1,value1 in dict1.items():
		for key2,value2 in dict2.items():
			if key1==key2 :
				dict_new[key1]=min(value1,value2)

	return dict_new
print(my_function5(dict1,dict2))
