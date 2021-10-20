n=int(input())
arr=list(map(int,input().split()))
arr2=list(map(int,input().split()))
arr.sort()
arr2.sort(reverse=True)
ans=0
for i in range(len(arr)):
    ans+=arr[i]*arr2[i]
print(ans)