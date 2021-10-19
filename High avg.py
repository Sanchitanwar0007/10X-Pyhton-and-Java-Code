def Where_to_place(l, x):
    # print(l)
    left=0
    right=len(l)-1
    ans=0
    while(left<=right):
        mid=(left+right)//2
        # print(l[mid],left,right)
        if(l[mid]<x):
            # print("a")
            ans=max(ans,mid+1)
        if(l[mid]<x):
            left=mid+1
        else:
            right=mid-1
    return ans
   # Implement This
n=int(input())
l=list(map(int,input().split()))[:n]
sum=0
l.sort()
for i in range(n):
    sum+=l[i]
    avg=sum//(i+1)
    l[i]=avg   
t=int(input())    
for k in range(t):
    x=int(input())
    print(Where_to_place(l,x))