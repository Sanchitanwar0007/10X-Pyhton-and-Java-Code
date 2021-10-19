def count_add(arr,target,i):
    if(target==0 and i==len(arr)):
        return 1
    if(i>=len(arr)):
        return 0
    # count=0
    return count_add(arr,target,i+1)+count_add(arr,target-arr[i],i+1)+count_add(arr,target+arr[i],i+1)
    
target=int(input())
size=int(input())
arr=list(map(int,input().split()))
print(count_add(arr,target,0))

