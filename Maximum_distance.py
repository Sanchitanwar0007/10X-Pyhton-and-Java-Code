n=int(input())
arr=list(map(int ,input().split()))
max1=float('-inf')
min1=float('inf')
for i in range(n):
    temp=arr[i]*(i-1)
    if(temp>max1):
        max1=temp
    temp2=arr[i]*(i+1)
    if(temp2<min1):
        min1=temp2
print(max1-min1)