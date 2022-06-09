# Tuples

filename = "dataset/mbox-short.txt"
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if line.startswith("From "):
        lin=line.split()
        lines=lin.sort()
        #x=tuple(lin[0])
        x=lin[0]
        hour = x[0:2]
        '''for x in hour:
             if x in hour:
                  
             else:
                  count=1'''
        h=hour.sort()
        print(h)