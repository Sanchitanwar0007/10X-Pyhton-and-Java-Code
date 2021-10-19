for _ in range(int(input())):
    n,m=map(int,input().split())
    arr=[]
    for i in range(n):
        t=list(map(int,input().split()))
        arr.append(t)
    
    print(arr[n//2][m//2])