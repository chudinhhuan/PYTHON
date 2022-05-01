# ax + b = 0
from os import access


class giai_pt():
    def __init__(self,a:float,b:float):
        self.a = a
        self.b = b
        
        assert a != 0
    def giai(self):
        return -self.b / self.a
pt1 = giai_pt(3,-5)
pt2 = giai_pt(2,6)    

print(pt1.giai())
print(pt2.giai())