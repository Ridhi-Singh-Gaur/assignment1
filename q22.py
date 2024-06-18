l=int(input("enter length of list"))
l1=[]
for i in range(0,l):
    y=int(input("enter element"))
    l1.append(y)
max=l1[0]
min=l1[0]
for i in range(1,l):
    if(l1[i]>max):
        max=l1[i]
print("maximum  element is :",max)
for i in range(1,l):
    if(l1[i]<min):
        min=l1[i]
print("minimum  element is :",min)

