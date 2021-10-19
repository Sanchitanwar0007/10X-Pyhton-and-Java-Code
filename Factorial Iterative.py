n=int(input())
fact=1
for i in range(1,n+1):
	fact=fact*i
if(n==0):
	print(fact)
elif(n<0):
	print('undefined')
else:
	print(fact)