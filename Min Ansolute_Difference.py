import math
n=int(input())
arr=list(map(int,input().split()))
min=float('inf')
arr.sort(reverse=True)
for i in range(n-1):
	if(arr[i]-arr[i+1]<min):
		min=arr[i]-arr[i+1]
print(min)