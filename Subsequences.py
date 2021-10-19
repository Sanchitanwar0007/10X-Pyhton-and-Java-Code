from collections import Counter

def subsequences(count):
    ans=[]
    for i in range(arr[len(arr)-1],0,-1):
        temp=[]
        val=count[i]
        if(val>0):
            for j in range(1,i+1):
                temp.append(j)
                count[j]-=val
            for k in range(val):
                ans.insert(0,temp)
    return ans
n=int(input())
arr=list(map(int,input().split()))
# count=Counter(arr)
arr.sort()
count=Counter(arr)
# print(count[2])
flag=1
for i in range(2,arr[len(arr)-1]+1):
    if(count[i]>count[i-1]):
        flag=0   # Not complete Subsequences
        break
if flag==1:
    res=subsequences(count)
    print(len(res))
    [print(*j) for j in res]
if flag==0:
    freq=0
    ans=0
    for i in range(arr[len(arr)-1],0,-1):
        if(count[i]>=freq):
            freq=count[i]
        else:
            differnce=freq-count[i]
            ans+=differnce
    print(ans)

