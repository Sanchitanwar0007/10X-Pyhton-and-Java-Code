def min_elemnt(arr):
    left=0
    right=len(arr)-1
    while(left<right):
        mid=(left+right)//2
        if(arr[mid]<arr[right]):
            right=mid
        else:
            left=mid+1
    return arr[left]
    
            


n=int(input())
arr=list(map(int,input().split()))
print(min_elemnt(arr))