def find_index(arr,k):
    if(arr[0]>k):
        return 0
    left=0
    right=len(arr)-1
    pos=0
    while(left<=right):
        mid=(left+right)//2
        if(arr[mid]<=k):
            pos=mid
            left=mid+1
        if(arr[mid]>k):
            right=mid-1
        else:
            left=mid+1
    if(arr[pos]==k):
        return pos
    else:
        return pos+1
n=int(input())
for i in range(n):
    arr=[int(x) for x in input().split()]
    m=int(input())
    arr2=list(map(int,input().split()))
    for j in range(len(arr2)):
        k=arr2[j]
        ans=find_index(arr,k)
        print(ans)
