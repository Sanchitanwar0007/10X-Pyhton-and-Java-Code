# your code goes here
n=int(input())
list=[]
for i in range(n):
	num=int(input())
	list.append(num*num)
list.sort()
[print(i) for i in list]