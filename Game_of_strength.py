n=int(input())
for i in range(n):
    num=int(input())
    arr=list(map(int,input().split()))
    maxx=max(arr)
    left_to_right_sum=0
    rigth_to_left_sum=0
    arr.sort()
    mul=len(arr)-1
    
    for i in range(len(arr)-1,0,-1):
        # print(arr[i],mul)
        left_to_right_sum+=arr[i]*mul
        mul-=1
    # print(left_to_right_sum)
    # %1000000007
    # left_to_right_sum=left_to_right_sum%1000000007
    mul=len(arr)-1
    for i in range(len(arr)):
        rigth_to_left_sum+=arr[i]*mul
        mul-=1
    # rigth_to_left_sum=rigth_to_left_sum%1000000007
    overall_power=(abs(left_to_right_sum-rigth_to_left_sum)*maxx)%1000000007
    print(overall_power)