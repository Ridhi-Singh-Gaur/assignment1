x=int(input("enter first no"))
y=int(input("enter second no"))
print("choices are: \n 1.prefix \n 2.suffix" )
choice=int(input("enter choice from above"))
if(choice==1):
    prefix=input("enter prefix")
    if(x[0]==prefix):
        print("prefix is present in the given string")
elif(choice==2):
    suffix = input("enter suffix")
    if (x[-1] == suffix):
        print("suffix is present in the given string")
else:
    print("wrong choice entered")