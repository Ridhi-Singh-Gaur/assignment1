l=int(input("enter length of list"))
l1=[]
for i in range(l):
    y=int(input("enter element"))
    l1.append(y)
ch=int(input("enter a no to search in the list"))
sum=0
for i in range(l):
    if(l1[i]==ch):
        sum+=1
print(sum)
