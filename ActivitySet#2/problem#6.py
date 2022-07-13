'''class Menu:
    """fill in class definition here"""


m = Menu()  # Menu is a class
m.add("idly", 10)
m.add("vada". 20)

m.show()'''

class Menu:
    """fill in class definition here"""
    def __init__(self,item,price):
           self.item=item
           self.price=price


m1=Menu("idly", 10)
m2=Menu("vada", 20)
print(m1.item, m1.price)
print(m2.item, m2.price)
