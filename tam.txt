# PYHON - MỘT SỐ GIẢI THUẬT VÀ PROGAMMING
![photo demo](https://sharecs.net/wp-content/uploads/2020/08/Lap-Trinh-Python.jpg)
## link demo de xem online 
[click de xem](https://www.facebook.com/Ng%C6%B0%E1%BB%9Di-l%C3%ADnh-H%E1%BB%93-Ch%C3%AD-Minh-1963536370356022/)

### huong dan cai dat moi truong
> Huong dai tai va cai dat moi truong python 
> dùng các tool code như anacoda , visual stadion code có cài đặt môi trường pytho

## 1.Giải thuật tìm kiếm cây nhị phân xây dựng node thông qua kiểu dict 
### Khái quát về tìm kiếm cây nhị phân 
![cay nhi phan](https://user-images.githubusercontent.com/90398366/164951050-dcd4baeb-b485-4eeb-a879-5cc02ea8a6f6.png)
![tim kiem cay nhi phan](https://user-images.githubusercontent.com/90398366/164951068-57ac4200-411b-495f-b891-5066ce93aebd.png)
>Cấu trúc cây (Tree) là một tập hợp các phần tử gọi là nút (node), mỗi cây có một nút gốc (root) chứa nhiều nút con, mỗi nút con lại là một tập hợp các nút khác gọi là cây con (subtree).

>Giải thuật có :
- Cách lấy ra node
- Cách lấy ra giá trị của node
- Cách lấy ra thông tin các node  bên trái, bên phải 
- Hàm trả về cây nhị phân con, cây bên trái và cây bên phải 
## Code demo như sau : 
```
node_01 = {'name': 'A', 'value': 12, 'left': 'B', 'right': 'C'}
node_02 = {'name': 'B', 'value': 7, 'left': 'D', 'right': 'E'}
node_03 = {'name': 'C', 'value': 19, 'left': None, 'right': None}
node_04 = {'name': 'D', 'value': 5, 'left': None, 'right': None}
node_05 = {'name': 'E', 'value': 9, 'left': None, 'right': 'F'}
node_06 = {'name': 'F', 'value': 10, 'left': None, 'right': None}

binary_tree = [node_01,node_02,node_03,node_04,node_05,node_06]
root_node = node_01.copy()

# Ham lay ra node
def get_info_node(give_name):
    global binary_tree,root_node
    for node in binary_tree:
        if node['name'] == give_name:
            return node

# Ham lay ra value trong cua node dua vao
def get_value_node(give_name):
    global binary_tree, root_node
    for node in binary_tree:
        if node['value'] == give_name['value']:
            return node['value']

def get_left_node_infor(give_name):
    global binary_tree,root_node
    # lay thong tin tin node dua vao
    node_infor = get_info_node(give_name)
    # lay ten node nam ben trai cua node dua vao
    left_node_name = node_infor['left']
    # lay ra left node bang cach lay infor tuong ung left node name
    if left_node_name == None:
        return {}
    else:
        left_node_name = get_info_node(left_node_name)
        return left_node_name
# print(get_left_node_infor('A'))

def get_right_node_infor(give_name):
    global binary_tree,root_node
    # lay thong tin node input
    node_infor = get_info_node(give_name)
    # lay ra ten node ben phai cua node dua vao
    right_node_name = node_infor['right']
    # lay ra right node bang cach lay infor tuong ung right node name
    if right_node_name == None:
        return {}
    else:
        right_node_name = get_info_node(right_node_name)
        return right_node_name
# print(get_right_node_infor('E')) 
# Tra ve toan bo cay con tu node input
# del xoa theo index, remove xoa theo value , pop loai bo phan tu do va tra lai phan tu loai bo

def get_whole_subtree(give_name):
    global binary_tree,root_node
    out_tree = [] 
    # creat stack  va add give_name vao
    my_stack = [give_name]
    # check len mystack 
    while len(my_stack) != 0: 
        # neu khac rong thi se 
        give_name = my_stack.pop()
        # lay infor cua cai node vua moi pop ra
        node_info = get_info_node(give_name)
        # kiem tra xem ben trong out_tree co give_name chua 
        # neu chua co thi them node do vao out_tree
        if node_info not in out_tree:
            out_tree.append(node_info)
        else:
            pass
        # kiem tra node left va add vao out_tree
        left_node  = get_left_node_infor(give_name)
        if len(left_node) == 0:
            pass
        else:
            # lay cai name left node ra
            left_name_node = left_node['name']
            # them name_node vao stack
            my_stack.append(left_name_node)
            #  cap nhat  infor left node vao out_tree 
            out_tree.append(left_node)
            
        # kiem tra right node va cap nhat them vao out_tree
        right_node = get_right_node_infor(give_name)
        if len(right_node) == 0:
            pass
        else:
            # lam tuong tu left_node
            right_name_node = right_node['name']
            my_stack.append(right_name_node)
            out_tree.append(right_node)
    return out_tree

# print(get_whole_subtree('B'))
def get_left_subtree(give_name):
    # lay ra thong tin node dua vao
    node_infor = get_info_node(give_name)
    # dung get() lay ra gia tri left kiem tra 
    # neu None thi return []
    # neu co gia tri ben trong thi lay gia tri ben trong gan vao left_node_name 
    # sau do se dung ham tra ve cay con truyen gia tri left_node_name vao
    if node_infor.get('left') == None:
        return[]
    else:
        left_node_name = node_infor['left']
        return(get_whole_subtree(left_node_name))
        
# print(get_left_subtree('B'))

def get_right_subtree(give_name):
    node_info  = get_info_node(give_name)
    if node_info.get('right') == None:
        return[]
    else:
        rigt_node_name = node_info['right']
        return(get_whole_subtree(rigt_node_name))
print(get_right_subtree('B'))
```
### Thanks ! 
