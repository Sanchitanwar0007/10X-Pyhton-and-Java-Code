# your code goes here
n=int(input())
list=[]
for i in range(n):
	list.append([int(i) for i in input().split(' ')])
sum=0
for i in range(n):
    for j in range(n):
        if(i==j):
            # print(list[i][j])
            sum+=list[i][j]
        if(i+j==n-1):
            # print(list[i][j])
            sum+=list[i][j]
print(sum)