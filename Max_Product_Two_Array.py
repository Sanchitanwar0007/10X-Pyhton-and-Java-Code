n=int(input())
m=int(input())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
for i in range(len(arr1)):
    if(arr1[i]<0):
        arr1[i]=abs(arr1[i])
for i in range(len(arr2)):
    if(arr2[i]<0):
        arr2[i]=abs(arr2[i])
num1=max(arr1)
num2=max(arr2)
print(num1*num2)