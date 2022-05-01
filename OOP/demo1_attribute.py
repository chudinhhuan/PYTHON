class Item():
    # khai bao attribute
    def __init__(self,name,price,quantity):
        # self.ten = name
        self.name = name 
        self.price = price
        self.quantity = quantity
        
item1 = Item("Phone",1000,4)
item2 = Item("Laptop",12000,5)

print('mat hang co ten la : ',item1.name)
print('mat hang co gia la : ',item1.price)
print(f'mat hang 2 co ten la {item2.name}, co gia la {item2.price}')