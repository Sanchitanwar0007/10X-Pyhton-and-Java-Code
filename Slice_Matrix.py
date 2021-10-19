n,m=map(int,input().split())
list=[]
for i in range(n):
    list.append([int(i) for i in input().split(' ')])
a,b,c,d=map(int,input().split())
for i in range(c-1,d):
    for j in range(a-1,b):
        print(list[i][j],end=" ")
    print()