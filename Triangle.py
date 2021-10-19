import math
n=int(input())
for i in range(n):
    b,a=map(int,input().split())
    temp=2*a
    h=math.ceil(temp/b)
    print(h)