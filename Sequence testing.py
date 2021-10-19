from collections import Counter

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
dict=Counter(arr)
flag=1
for i in range(1,arr[len(arr)-1]):
    if(dict[i])