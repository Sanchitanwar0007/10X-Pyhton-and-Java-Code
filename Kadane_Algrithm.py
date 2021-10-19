def rank(arr):
    max=float('-inf')
    max_till_now=0
    for i in range(len(arr)):
        max_till_now=max_till_now+arr[i]
        if(max<max_till_now):
            max=max_till_now
        if(max_till_now<0):
            max_till_now=0
    return max
n=int(input())
for i in range(n):
    l=int(input())
    arr=list(map(int,input().split()))
    print(rank(arr))

# 3
# 6
# 12 35 1 10 34 -1
# 3
# 10 5 12
# 1
# 10