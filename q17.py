s=input("enter a string")
y=s.split()
m=""
for i in range(len(y)):
    y[i]=y[i].title();
for i in range(len(y)):
    m+=y[i]
    m+=" "
print(m)
