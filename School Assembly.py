n=int(input())
arr=list(map(int,input().split()))
ans=1
for i in range(len(arr)-1):
    if(arr[i]>arr[i+1]):
        ans+=1
print(ans)