def selection_sort(arr):
    for i in range(0,len(arr)):
        my_list = i
        for j in range(i,len(arr)):
            if arr[j] < arr[my_list]:
                my_list = j
        arr [i],arr[my_list] = arr[my_list],arr[i]

       



        #return arr
li=[10,9,1,5,8]
selection_sort(li)



print(li)


#-----------------------
def Ktra_list_doi_xung(lst):
    ouput = 'doi xung'
    for i in range(len(lst)):
        left_num = lst[i]
        right_num = lst[len(lst)-i-1]
        if left_num == right_num:
            pass
        else:
            ouput = 'khong doi xung'
    return ouput

def ktra_dxung_chan(lst):
    ouput = 'valid'
    for i in range(len(lst)):
        num_left = lst[i]
        num_right = lst[len(lst)-i-1]
        num_sum = num_right + num_left
        if num_sum % 2 == 0:
            pass
        else:
            ouput = 'invalid'
    return ouput

def dich(lst,index):
    i = len(lst)-1
    while i >= index:
        lst[i] = lst [i-1]
        i-=1
    return lst

def insertion_sort(my_lst,num):

    flag = False
    for i,v in enumerate(my_lst):
        if num < v:
            flag = True
            break
    if flag:
        found_inx = i
    else:
        found_inx = len(my_lst)
    my_lst.append('')

    for i in range(len(my_lst)-1,found_inx,-1):
        my_lst[i] = my_lst[i-1]
    my_lst[found_inx] = num
    return my_lst

def sap_xep(lst1):
    lst1_ = []
    for j in range(len(lst1)):
        insertion_sort(lst1_,lst1[j])
    return lst1_

def selection_sort(lst):
    for i in range(0,len(lst)):
        min_tam = i
        for j in range(i+1,len(lst)):
            if lst[j] < lst[min_tam]:
                min_tam = j
        lst[i],lst[min_tam] = lst[min_tam],lst[i]

    return lst

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]