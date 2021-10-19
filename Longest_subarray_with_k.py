n,k=map(int,input().split())
arr=[int(x) for x in input().split(' ')]
map={}
map[0]=-1
sum=0
long=0
for i in range(len(arr)):
    sum+=arr[i]
    temp=sum
    temp-=k
    if(sum not in map):
        map[sum]=i
    if(temp in map):
        idx=map[temp]
        long=max(i-idx,long)
# print(map)
print(long)