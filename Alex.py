string=input()
ans=""
for i in range(len(string)):
    if(ord(string[i])>=97 and ord(string[i])<=122):
        ans+=string[i].upper()
    else:
        ans+=string[i].lower()
print(ans)