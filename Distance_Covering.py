def distance(n):
    if(n<=1):
        return 1
    return distance(n-1)+distance(n-2)
t=int(input())
for i in range(t):
	num=int(input())
	print(distance(num))