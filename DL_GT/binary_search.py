
def binary_search(lst,x):
    l = 0
    r = len(lst) - 1
    while l <= r:
        mid = (r+l) // 2 
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            l = mid +1
        else:
            r = mid -1
        
lst = [1,3,4,5,7,8,9,10,12,14,16,20]
print(binary_search(lst,20))
        

