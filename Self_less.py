def self_less(arr):
    left_to_rigth=[0]*len(arr)
    rigth_to_left=[0]*len(arr)
    left_to_rigth[len(arr)-1]=1
    rigth_to_left[0]=1
    for i in range(len(arr)-2,-1,-1):
        left_to_rigth[i]=left_to_rigth[i+1]*arr[i+1]
    for i in range(1,len(arr)):
        rigth_to_left[i]=rigth_to_left[i-1]*arr[i-1]
    for i in range(len(arr)):
        print(left_to_rigth[i]*rigth_to_left[i],end=" ")

n=int(input())
for i in range(n):
    num=int(input())
    arr=list(map(int,input().split()))
    self_less(arr)