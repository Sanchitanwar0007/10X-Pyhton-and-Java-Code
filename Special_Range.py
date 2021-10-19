n=int(input())
m=int(input())
if(n>m):
	n,m=m,n
if(m<0):
	print(-1)
else:
	for i in range(n,m+1):
		if(i>=0):
			print(i)