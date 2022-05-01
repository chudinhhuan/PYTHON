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

# tinh ke thua
# khoi tao class con

class Phone(Item): #tuc la Phone la class con cua class cha Item
    def __init__(self, name: str, price: float, quantity: int,loai="4G"):
        super().__init__(name, price, quantity)
        self.loai = loai


phone1 = Phone("Samsung note20",10000,3,"5G")
phone2 = Phone("Samsung note22",13000,3)
print(f"{phone1.name} co gia la {phone1.price}")
print(f"{phone2.name} loai {phone2.loai}")

