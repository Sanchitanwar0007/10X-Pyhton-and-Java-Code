n=int(input())
arr=list(map(int,input().split()))
end=-1
start=-1
for i in range(len(arr)-1,-1,-1):
    if(arr[i]<arr[i-1] and i!=0):
        # print("cos")
        end=i
        break

for i in range(len(arr)-1):
    if(arr[i]>arr[i+1]):
        start=i
        break
if(end-start==0):
    print(-1,-1,-1)
else:
    print(start,end,end-start+1)
