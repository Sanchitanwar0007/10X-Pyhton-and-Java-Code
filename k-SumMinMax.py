# # your code goes here
# n,k=map(int,input().split())
# list=list(map(int,input().split()))
# arr=[]
# i=0
# j=k
# # while(j<=len(list)):
# #     sum=0
# count=1
# sum=0
# for m in range(n):
    
#     if(m<=j and j<len(list)):
#         sum+=list[m]
#         count+=1
#     if(count==k):
#         arr.append(sum)
#         sum=0
        
#         m=m-j+1
#         count=1
#     j+=1
# print(arr)
# print(max(arr),end=" ")
# print(min(arr))



n,k=map(int,input().split())
list=list(map(int,input().split()))
sum=0
arr=[]
for i in range(k):
    sum+=list[i]
arr.append(sum)
for i in range(k,n):
    sum+=list[i]-list[i-k]
    arr.append(sum)
# print(arr)
print(max(arr),end=" ")
print(min(arr))

#  O(n) approach an accepted 100%
