# Files

filename = "dataset/mbox-short.txt"
fhand=input("Enter the file")
fh=open(fhand)
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    num=float(line[line.find("0"):])  
    count=count+1
    total=total+num
    average=total/count
    
print("Average spam confidence:",average)

"""fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if  not line.startswith("X-DSPAM-Confidence:"):
     continue
    #print(line)
    num=float(line[line.find("0"):])
    count=count+1
    total=total+num
   
print("Average spam confidence:",total/count)"""
 
#RECAP
#RECAP2