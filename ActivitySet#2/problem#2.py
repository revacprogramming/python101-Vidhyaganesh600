
'''def add(a, b):
    pass  # ...


def output(a, b, sum):
    pass  # ...


def main():
    a, b = input_two_numbers()
    sum = add(a, b)

    output(a, b, sum)


if __name__ == '__main__':
    main()'''


def add(a, b):
   return a+b


def output(a, b, sum):
   #print("sum of %d + %d is %d"%(a,b,sum))
   #print(f'sum of {a}+{b}={sum}')
   s='{}+{} ={}'
   print(s.format(a,b,sum))

def main():
    a=int(input("enter the numbers"))
    b=int(input("enter the numbers"))
    sum=add(a,b)
    output(a, b, sum)


if __name__ == '__main__':
     main()


