def delete(arr,k):
    temp=[]
    for i in range(len(arr)):
        while(k>0 and len(temp)>0 and temp[-1]<arr[i]):
            temp.pop()
            k-=1
        temp.append(arr[i])
    for i in temp:
        print(i,end=" ")
for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    delete(arr,k)
