x=int(input("enter a first no"))
y=int(input("enter a second no"))
print("choices are: \n 1.+ \n 2.- \n 3.* \n 2 ./" )
choice=int(input("enter choice from above"))
if(choice==1):
    print(x+y)
elif(choice==2):
    print(x-y)
elif (choice == 2):
    print(x*y)
elif(choice==3):
    print(x/y)
else:
    print("wrong choice entered")