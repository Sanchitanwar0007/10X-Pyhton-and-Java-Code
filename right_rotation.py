arr=list(map(int,input().split()))
m=int(input())
# list=[0]*len(arr)
m=m%len(arr)
temp=[0]*m
j=0
for i in range(len(arr)-m,len(arr)):
    temp[j]=arr[i]
    j+=1

list=[0]*len(arr)
for i in range(len(temp)):
    list[i]=temp[i]

for i in range(len(arr)-m):
    list[j]=arr[i]
    j+=1
print(list)
# for i in range(len(arr)):
    
# print(list)