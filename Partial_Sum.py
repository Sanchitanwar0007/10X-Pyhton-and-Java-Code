n,m=map(int,input().split())
arr=list(map(int,input().split()))
sum=0
for i in arr:
    sum+=i
flag=0
for i in range(len(arr)):
	if(sum-arr[i]==m):
		flag=1
		break
if(flag==0):
	print(0)
else:
	print(1)