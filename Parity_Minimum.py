n=int(input())
min=float('inf')
for i in range(n):
	num=int(input())
	if(num<min):
		min=num
sum=0
while(min>0):
	temp=min%10
	sum+=temp
	min=min//10
# print(sum)
if(sum%2==0):
	print(1)
else:
	print(0)