

class Menu:
    """fill in class definition here"""


m = Menu()
m = m + ("idly", 10) + ("vada", 20)  # Hint: operator overloading special methods (__add__, __sub__, etc.)

print(m)  # should print the menu properly

m=input("enter the items")


class Menu():
  """fill in class definition here"""
  def __init__(self,item,rate):
    self.item=item
    self.rate=rate
  def __add__(self,other):
    return self.item + str(self.rate),other.item+str(other.rate)


m1=Menu('idly',10)
m2=Menu('vada', 20)
m3=Menu('dosa',30)
# Hint: operator overloading special methods (__add__, __sub__, etc.)
print("__________Menu___________")  # should print the menu properly
print(m1 +m2)