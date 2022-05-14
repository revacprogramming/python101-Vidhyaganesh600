# Conditional Execution(1)

hrs = input("Enter Hours:")
h = float(hrs)
rat= input("Enter rate:")
r = float(rat)
if h>40:
    pay=print((h-40)*1.5*r+40*r)
else:
    pay=print(h*r)


# Conditional Execution(2)

score = input("Enter Score: ")
i=float(score)
if i>0.0 and i<1.0:
    if i>=0.9:
       print('A')
    elif i>=0.8:
       print('B')
    elif i>=0.7:
       print('C')
    elif i>=0.6:
       print('D')
    elif i<0.6:
       print('F')
        
else:
     print('Error:The value is out of the range!!!!!')
        