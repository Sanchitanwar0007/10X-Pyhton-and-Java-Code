# your code goes here
n=int(input())
list=[]
for i in range(n):
	list.append(int(input()))
index=[]
for i in range(n):
	index.insert(int(input()),list[i])
for i in index:
	print(i)