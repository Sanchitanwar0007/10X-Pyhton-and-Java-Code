import math
def round(n):
    k=int(n)
    j=n-k
    if(n>=(k+0.5)):
        return math.ceil(n)
    else:
        return math.floor(n)
n=int(input())
for i in range(n):
    num=int(input())
    roundL=[]
    flag=0
    if(num==0 or num==1):
        print(-1)
        continue
    arr=list(map(int,input().split()))
    for i in range(len(arr)-1):
        if(arr[i]!=0):
            m=arr[i+1]/arr[i]
            roundL.append(round(m))
        else:
            flag=1
    if(arr[len(arr)]==0):
        flag=1
    if(flag==1):
        print(-1,end="")
    else:
        for i in roundL:
            print(i,end=" ")
    print()
        