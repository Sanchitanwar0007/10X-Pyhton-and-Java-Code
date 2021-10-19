for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    b=[]
    for i in range(len(arr)):
        b.append(arr[i])
    b.sort()
    if(n==2):
        print(abs(arr[0]-arr[1]))
    elif(b[n-1]==arr[0] and arr[n-1]==b[0]):
        print(max(b[n-2]-b[0],b[n-1]-b[1]))
    else:
        print(b[n-1]-b[0])