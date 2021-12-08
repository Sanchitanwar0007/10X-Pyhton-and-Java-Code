n=int(input())
arr=list(map(int,input().split()))
d={}
for i in range(len(arr)):
    if(arr[i] in d):
        d[arr[i]]+=1
    else:
        d[arr[i]]=1
maxx=0
for i in d:
    if(d[i]>maxx):
        maxx=d[i]
minn=float("inf")
for i in d:
    if(d[i]==maxx):
        if(i<minn):
            minn=i
print(minn)
