# your code goes here
n=int(input())
arr=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))
sett=set()
settt=set()
# print(arr)
# print(arr2)
for i in range(len(arr)):
    sett.add(arr[i])
for i in range(len(arr2)):
    settt.add(arr2[i])
ans=[]
for i in range(len(arr)):
    if(arr[i] not in settt):
        ans.append(arr[i])
for i in range(len(arr2)):
    if(arr2[i] not in sett):
        ans.append(arr2[i])
set1=set()
for i in range(len(ans)):
	set1.add(ans[i])
ans2=list(set1)
ans2.sort()
for i in range(len(ans2)):
	print(ans2[i])
	