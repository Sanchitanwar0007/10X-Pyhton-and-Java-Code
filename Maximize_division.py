n=int(input())
arr=list(map(int,input().split()))
max_i=float('-inf')
min_j=float('inf')
for i in range(len(arr)):
    val=abs(arr[i]-i)
    max_i=max(val,max_i)
    min_j=min(val,min_j)
print(max_i/min_j)