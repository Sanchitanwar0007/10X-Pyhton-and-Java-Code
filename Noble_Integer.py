n=int(input())
list=[]
count=0
flag=0
for i in range(n):
	list.append(int(input()))
for i in range(len(list)):
	for j in range(len(list)):
		if(list[i]<list[j]):
			count+=1
	if(count==list[i]):
		flag=1
		print(1)
		break
	else:
		count=0
if(flag==0):
	print(-1)
