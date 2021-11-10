n=int(input())
arr=list(map(int,input().split()))
bricks=0

arr2=[0]*len(arr)
for i in range(len(arr)):
    arr2[i]=arr[i]
for i in range(1,len(arr)):
    if(arr[i]<=arr[i-1]):
        arr[i]=arr[i-1]+1
    # else:
    #     arr2[i]=arr[i]

for i in range(len(arr)):
    bricks+=arr[i]-arr2[i]

print(bricks)