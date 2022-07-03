# Object Oriented Programming
# https://www.py4e.com/lessons/Objects
cart=list()
cart.append("Soaps")
cart.append("Bottles")
cart.append("Box")
cart.sort()
print(cart[0])
print(cart.__getitem__(1))
print(list.__getitem__(cart,2))