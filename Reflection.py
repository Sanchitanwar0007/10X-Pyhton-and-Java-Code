n=int(input())
for i in range(n):
    x0,y0,x1,y1=map(int,input().split())
    diffx=x1-x0
    diffy=y1-y0
    print(x1+diffx,y1+diffy)