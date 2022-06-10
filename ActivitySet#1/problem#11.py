# Tuples

filename = "dataset/mbox-short.txt"
'''name = input("Enter file:")
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
        for x in hour:
             if x in hour:
                  
             else:
                  count=1
        h=hour.sort()
        print(h)'''
l=list()
d=dict()
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for info in handle:
    if info.startswith("From "):
        inf=info.split()
        part=inf[5]
        par=part[ :2]
        l.append(par)
        l.sort()
for x in l:
       if x not in d:
              d[x] =1
       else:
              d[x]=d[x] + 1

for k,v in d.items():
   print(k,v)
   
        
