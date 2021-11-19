for _ in range(int(input())):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    i=0
    while(arr[i]<m):
        i+=1
    arr.insert(i,m)
    print(*arr)