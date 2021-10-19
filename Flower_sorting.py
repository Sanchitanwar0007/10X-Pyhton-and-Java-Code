n=int(input())
arr=list(map(int,input().split()))
max1=float('-inf')
max2=float('-inf')
max3=float('-inf')
max4=float('-inf')
max5=float('-inf')
idx1=0
idx2=0
max1=max(arr)
for i in range(n):
    if(arr[i]>max1):
        max1=arr[i]
        idx1=i

for i in range(n):
    if((max2<arr[i] and max2<=max1) and i !=idx1):
        max2=arr[i]
        idx2=i
print(max1,max2)