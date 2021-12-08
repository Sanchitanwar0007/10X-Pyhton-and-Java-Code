n=int(input())
arr=list(map(int,input().split()))
d={}
count=0
for i in range(len(arr)):
    val=arr[i]
    if(val in d):
        d[val]+=1
    else:
        d[val]=1

    if(val<0 and val!=0):
        if(-1*val in d):
            count+=d[-1*val]
    else:
        if(-1*val in d and val!=0):
            count+=d[-1*val]
print(count)
