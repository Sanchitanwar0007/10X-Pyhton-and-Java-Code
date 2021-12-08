# n,q=map(int,input().split())
# dictionary={}
# arr=[0]*n
# for i in range(q):
#     l,r,val=map(int,input().split())
#     key=str(l)+"#"+str(r)
#     if(key in dictionary):
#         dictionary[key]+=val
#     else:
#         dictionary[key]=val
# print(dictionary)
# for i in dictionary:
#     val=i
#     sum=dictionary[i]
#     s1=val.split("#")
#     s_range=s1[0]
#     e_range=s1[1]
#     for j in range(int(s_range),int(e_range)+1):
#         arr[j]+=sum
#     # print(arr)
# print(*arr)
# # 
n,q=map(int,input().split())
arr=[0]*n
for i in range(q):
    l,r,val= map(int,input().split())
    arr[l]+=val
    if(r!=n-1):
        arr[r+1]-=val
for i in range(1,n):
    arr[i]=arr[i-1]+arr[i]
print(*arr)
