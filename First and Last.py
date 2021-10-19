def first_occurance(arr,k):
    left=0
    right=len(arr)-1
    pos=-1
    while(left<=right):
        mid=(left+right)//2
        if(arr[mid]==k):
            pos=mid
            right=mid-1
        if(arr[mid]<k):
            left=mid+1
        else:
            right=mid-1
    return pos
def last_occurance(arr,k):
    left=0
    right=len(arr)-1
    pos=-1
    while(left<=right):
        mid=(left+right)//2
        if(arr[mid]==k):
            pos=mid
            left=mid+1
        if(arr[mid]>k):
            right=mid-1
        else:
            left=mid+1
    return pos

n=int(input())
arr=list(map(int,input().split()))
k=int(input())
first=first_occurance(arr,k)
last=last_occurance(arr,k)
print(first,last)