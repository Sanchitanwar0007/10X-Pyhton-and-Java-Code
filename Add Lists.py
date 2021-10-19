tc = int(input())
for t in range(tc):
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	if len(b)>len(a):
		a,b = b,a
	c = 0
	j = 0
	for i in range(len(a)):
		if(j<len(b)):
			s = a[i] + b[j] + c
		else:
			s = a[i]+c
		if(s>=10):
			c = s//10
			s = s%10
		else:
			c = 0
		j +=1
		print(s,end="")
	if(c>0):
		print(c,end="")
	print()