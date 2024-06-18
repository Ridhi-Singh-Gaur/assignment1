n=int(input("enter no of terms"))
count=b=1
a=0
if(n==1):
    print(a,"\n")
elif(n>=2):
    print(a,"\n")
    print(b)
    for i in range(1, n - 1):
        c = a + b
        print(c, "\n")
        temp = a
        a = b
        b = c
else:
    print("cant make a fibonacci series")
