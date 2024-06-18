s=input("enter a string ..")
m=""
for i in range(len(s)):
    if(s[i].isalnum()==True or s[i].isspace()==True):
        m+=s[i]
print(m)
