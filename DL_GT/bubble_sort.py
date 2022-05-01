lst  = [5,2,1,4,3]
def doi_cho(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            lst[i] , lst[i+1] = lst[i+1] , lst[i]

def bubble_sort(lst):
    for i in range(len(lst)-1):
        doi_cho(lst)

bubble_sort(lst)
print(lst)