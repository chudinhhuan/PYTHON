
dic_10 = {
    'value':4,
    'name':'A',
    'next':'T'
}

dic_20 = {
    'value':5,
    'name':'B',
    'next':'A'

}

dic_30 = {
    'value':10,
    'name':'I',
    'next':None
}
dic_40 = {
    'value':6,
    'name':'T',
    'next':'I'
}
#  note danh sach lien ket gom co
# ten node bieu dien bang name , ten node ke tiep bieu dien bang next , gia tri cua node bieu dien bang value

# out: [('B',5),('T',6),('I',10)]

# gop cac dic vao mot list
li_dics = [dic_10,dic_20,dic_30,dic_40]

# tim node dau tien trong list 
# node dau tien thi khong co node nao dung truoc no // node B
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
def find_name_node_next(current,li_dics):
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

# print(find_value('A',li_dics))

li_name_node = []
li_name_node.append(find_head(li_dics))
node_now = find_head(li_dics)
while True:
    next_node = find_name_node_next(node_now,li_dics)
    if next_node == None:
        break
    li_name_node.append(next_node)
    node_now = next_node
print(li_name_node)
out_put = []
for name_node in li_name_node:
    value = find_value(name_node,li_dics)
    name_node_tupple = (name_node,value)
    out_put.append(name_node_tupple)

print(out_put)




