print("1. C to F \n 2. F to C")
choice=int(input("enter choices from above choices "))
if(choice==1):
    c=int(input("enter temp in c"))
    print("temperature in fahrenheit is ",((9*c)/5) + 32)
elif(choice==2):
    f = int(input("enter temp in f"))
    print("temperature in fahrenheit is ", ((f-32)*5)/9)
else:
    print("wrong choice entered")
