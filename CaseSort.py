n=int(input())
s=input()
small=[]
capital=[]
for i in range(len(s)):
    if(ord(s[i])<=90):
        capital.append(s[i])
    else:
        small.append(s[i])
small.sort()
capital.sort()
# print(small,capital)
s_i=0
c=0
ans=""
for i in range(len(s)):
    if(ord(s[i])<=90):
        ans+=capital[c]
        c+=1
    else:
        ans+=small[s_i]
        s_i+=1
print(ans)