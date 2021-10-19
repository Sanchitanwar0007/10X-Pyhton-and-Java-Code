# your code goes here
n=int(input())
arr=list(map(int,input().split()))
for i in range(len(arr)):
	arr[i]=abs(arr[i])
rev_prefix_sum=[0]*n
rev_prefix_sum[n-1]=arr[n-1]
for i in range(len(arr)-2,-1,-1):
    rev_prefix_sum[i]=rev_prefix_sum[i+1]+arr[i]
result=0
for i in range(len(arr)-1):
    result+=arr[i]*rev_prefix_sum[i+1]
print(result)