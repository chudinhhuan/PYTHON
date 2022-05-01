
dict_10 = {'name': 'A', 'value': 5, 'next': 'C'}
dict_20 = {'name': 'C', 'value': 7, 'next': 'Z'}
dict_30 = {'name': 'Z', 'value': 8, 'next': None}

linked_list_01 = [dict_10,dict_20,dict_30]

# the second linked_list
dict_40 = {'name': 'O', 'value': 2, 'next': 'B'}
dict_50 = {'name': 'B', 'value': 3, 'next': 'V'}
dict_60 = {'name': 'V', 'value': 1, 'next': None}

linked_list_02 = [dict_40,dict_50,dict_60]

def find_head(li_dics):
    # pop name in a list
    li_name = []
    # them cac  node vao mot list
    for name in li_dics:
        li_name.append(name['name'])
    # duyet tung key trong list ten node moi lay ra
    for key in li_name:
        flag = False
        # so sanh tung cai ten node trong cai list_dic ( danh sach )
        for next in li_dics:
            # neu nhu node ke tiep ma bang node hien tai thi co se bat true (tuc la khong phai node dau tien)
            if next['next'] == key:
                flag = True
        if flag:
            pass
        else:
            # tra ve node dau tien trong link list
            # print(key)
            return key

#  tim node ke tiep trong danh sach 
def find_next_node_name(current,li_dics):
    #  dat bien gan gia tri None (null)
    result = None
    # duyet tung key trong li_dics
    for key in li_dics:
        if key['name'] == current:
            result = key['next']
            break
    return result

#  find value in node
def find_value(node_name,li_dics):
    for chose in li_dics:
        if chose['name'] == node_name:
            return chose['value']


# step 1 : tim tail trong link list 1
# head01 = find_head(linked_list_01)
# name_node_now = head01
# while True:
#     name_node_next = find_next_node_name(name_node_now,linked_list_01)
#     if name_node_next == None:
#         tail01 = name_node_now
#         break
#     name_node_now = name_node_next
# step 2 tim head trong link list 2s
def find_tail(link_list):
    head = find_head(link_list)
    node_now = head
    while True:
        node_next = find_next_node_name(node_now,link_list)
        if node_next == None:
            return node_now
        node_now = node_next

head02 = find_head(linked_list_02)
# step3 : thay doi next value tail 1 toi head 2
for chosee in linked_list_01:
    if chosee['name'] == find_tail(linked_list_01):
        chosee['next'] = head02

link1_2 = linked_list_01 + linked_list_02
# print(link1_2)

li_names = []
head = find_head(link1_2)
li_names.append(head)
node_name_now = head
while True:
    node_name_next = find_next_node_name(node_name_now,link1_2)
    if node_name_next == None:
        break
    li_names.append(node_name_next)
    node_name_now = node_name_next

out_put = []
for chose in li_names:
    value = find_value(chose,link1_2)
    tuple_my = (chose,value)
    out_put.append(tuple_my)

print(out_put)