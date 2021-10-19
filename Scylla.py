n,k=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
minn=float('inf')
k=k-1
for i in range(len(arr)-k):
    temp=arr[i+k]-arr[i]
    if(temp<minn):
        minn=temp
print(minn)