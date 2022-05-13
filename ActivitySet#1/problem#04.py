# Conditional Execution

hrs = input("Enter Hours:")
h = float(hrs)
rat= input("Enter rate:")
r = float(rat)
if h>40:
    pay=print((h-40)*1.5*r+40*r)
else:
    pay=print(h*r)
    