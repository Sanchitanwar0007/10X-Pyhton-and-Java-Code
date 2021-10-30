def paint(a,n,k):
    max=sum(a)
    start=0
    end=max
    while start<=end:
        mid=(start+end)//2
        if can(a,k,mid):
            res=mid
            end=mid-1
        else:
            start=mid+1
    return res
def can(a,k,mid):
    divisions=1
    running=0
    for x in a:
        if x>mid:
            return False
        if (running+x)>mid:
            divisions+=1  
            running=x
            if divisions>k:
                return False
        else:
            running+=x    
    return True      
a=[int(x) for x in input().split()]
k=int(input())
n=len(a)
print(paint(a,n,k) if k<=n else -1)