#Lists
"""
Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""
"""filename="dataset/mbox-short.txt"
if len(filename) < 2 :
  filename='mbox-short.txt'
fopen=open(filename)
count=0
for line in fopen:
  if line.startswith('From:') :
    continue
  if line.startswith("From"):
    sp=line.split()
    print(sp[1])
    count+=1
print("There are",count,"lines in the file From as a First Word")"""
file_name=input("Enter the filename to open >>")
f_open=open(file_name)
if len(file_name)<2:
  f_open=open("dataset/mbox-short.txt")
count=0
for line in f_open:
  if line.startswith("From:"):
    continue
  if line.startswith("From"):
     spt=line.split()
     print(spt[1])
     count=count+1
print("There are",count,"lines  in the file as the line starts with From at begining")