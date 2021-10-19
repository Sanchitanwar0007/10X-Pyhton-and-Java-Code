def max_sum(arr):
    max_so_far=0
    max=float('-inf')
    start=-1
    end=-1
    temp=0
    for i in range(len(arr)):
        max_so_far+=arr[i]
        if(max_so_far>max):
            start=temp
            end=i
            max=max_so_far
        if(max_so_far<0):
            max_so_far=0
            temp=i+1
    print(start,end,max)
n=int(input())
arr=list(map(int,input().split()))
max_sum(arr)