def repeat_sum(arr,n,k,i):
    if(k==0):
        return 1
    if(i==n or k<0):
        return 0
    return repeat_sum(arr,n,k-arr[i],i)+repeat_sum(arr,n,k,i+1)
m,n=map(int,input().split())
arr=list(map(int,input().split()))
print(repeat_sum(arr,len(arr),n,0))
