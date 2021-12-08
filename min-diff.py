n=int(input())
arr=list(map(int,input().split()))
arr.sort()
min=float('inf')
for i in range(1,len(arr)):
    if(arr[i]-arr[i-1]<min):
        min=arr[i]-arr[i-1]
print(min)