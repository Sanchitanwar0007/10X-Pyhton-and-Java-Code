n=int(input())
arr=list(map(int,input().split()))
arr.sort()
count=0
for i in range(len(arr)-1):
    if(arr[i]!=arr[i+1]):
        count+=1
if(arr[len(arr)-1]==arr[len(arr)-1]):
    count+=1
print(count)