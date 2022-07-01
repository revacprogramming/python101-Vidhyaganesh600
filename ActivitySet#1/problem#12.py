# Regular Expressions
# https://www.py4e.com/lessons/regex
import re
sum=0
file=input(" \033[1m Enter the filename -> \033[0m")
hand=open(file)
for line in hand:
           line=line.rstrip()
           x = re.findall('\d+',line)
           for k in x:
              y=float(k)
              sum+=y
print(sum)


