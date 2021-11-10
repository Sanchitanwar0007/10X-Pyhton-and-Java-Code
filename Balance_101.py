def min_number(arr,n):
    left_sum=0
    right_sum=0
    mid=n//2
    for i in range(mid):
        left_sum+=arr[i]
    for i in range(mid,n):
        right_sum+=arr[i]

        
    ans=abs(right_sum-left_sum)
    return ans
for _ in range(int(input())):
    n=int(input())
    
    arr=list(map(int,input().split()))
    arr.sort()
    print(min_number(arr,n))