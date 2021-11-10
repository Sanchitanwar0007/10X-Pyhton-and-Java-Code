def rotate(arr,n):
    
    for i in range(n,len(arr)):
        print(arr[i],end=" ")
    for i in range(n):
        print(arr[i],end=" ")
for _ in range(int(input())):
    m,n=map(int,input().split())
    arr=list(map(int,input().split()))
    n=n%len(arr)
    rotate(arr,n)
