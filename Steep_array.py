# n=int(input())
# arr=list(map(int,input().split()))
# ss_list=[]
# for i in range(len(arr)):
# 	max=arr[i]
# 	for j in range(i+1,len(arr)):
# 		if(max<=arr[j]):
# 			max=arr[j]
# 	ss_list.append(max-arr[i])
# total=0
# print(ss_list)
# for i in ss_list:
# 	total+=i
# print(total)

n=int(input())
a=list(map(int,input().split()))[:n]
max=float('-inf')
sum=0
a.reverse()
for i in range(0,n):
    if(a[i]>max):
        max=a[i]
        sum+=max-a[i]
    else:
        sum+=max-a[i]
print(sum)