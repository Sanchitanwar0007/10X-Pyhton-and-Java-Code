n=int(input())
arr1=[]
for i in range(n):
    temp=list(map(int,input().split()))
    arr1.append(temp)
m=int(input())
arr2=[]
for i in range(m):
    temp2=list(map(int,input().split()))
    arr2.append(temp2)
ans=[]
# print(len(arr1[0]),len(arr2))

for i in range(len(arr1)):
    temp=[]
    for j in range(len(arr2)):
        print(arr1[i][j],arr2[j][i])
        temp.append(arr1[i][j]*arr2[j][i]+arr1[i][j]*arr2[j][i])
    # print(temp)    
