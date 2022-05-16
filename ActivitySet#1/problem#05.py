# Functions

def computepay(h, r):
   if h>40:
    p=(h-40)*r/2+h*r
    p= print("Pay", p)
    
   else: 
    p = h*r
    p= print("Pay", p)
    return p

h = input("Enter Hours:")
r = input("Enter rate:")
fh = float(h)
fr = float(r)

computepay(fh,fr)


