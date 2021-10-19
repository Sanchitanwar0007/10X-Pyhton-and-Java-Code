n=int(input())
arr=list(map(int,input().split()))
min=arr[0]
max=arr[0]
count_min=0
count_max=0
for i in range(1,len(arr)):
    if(min>arr[i]):
        min=arr[i]
        count_min+=1
    elif(max<arr[i]):
        max=arr[i]
        count_max+=1
print(count_max,count_min)