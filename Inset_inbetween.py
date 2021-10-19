n,m=map(int,input().split())
arr=list(map(int,input().split()))
ans=[]
reach=0
flag=0
for i in range(n):
    if(arr[i]<m):
        ans.append(arr[i])
    elif(arr[i]>=m):
        ans.append(m)
        flag=1
        reach=i
        break
if(flag==0):
    ans.append(m)
else:
    for i in range(i,n):
        ans.append(arr[i])
print(ans)