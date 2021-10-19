n,q= map(int,input().split())
time_arr=list(map(int,input().split()))
score_arr=list(map(int,input().split()))
# score_arr.sort()
time_arr.sort(reverse=True)
prefix_sum=[0]*len(time_arr)
prefix_sum[0]=time_arr[0]
for i in range(1,len(prefix_sum)):
    prefix_sum[i]=prefix_sum[i-1]+time_arr[i]
# print(prefix_sum)
for i in range(q):
    k=int(input())
    print(prefix_sum[k-1])

# 5 2
# 2 3 9 4 5
# 3 5 11 6 7
# 5
# 3
# 2


