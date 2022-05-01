class Item():
    # khai bao attribute
    def __init__(self,name:str,price:float,quantity:int):
        # self.ten = name
        self.name = name 
        self.price = price
        self.quantity = quantity

        # kiem tra  dieu kien attribute
        assert price >= 0
    def Tong_gia(seft):
        return seft.price * seft.quantity

    # StaticMethod - phương thức tĩnh
    @staticmethod
    def Check_gia(gia):
        if gia <= 500:
            return "Cheap,dat o tang 1"
        else:
            return "expensive, dat o tang 2"


item1 = Item("Phone",1000,4)
item2 = Item("Laptop",12000,5)

print(item1.Tong_gia())
print(Item.Check_gia(1000))