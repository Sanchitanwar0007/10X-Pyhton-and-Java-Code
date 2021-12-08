for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    i=0
    j=1
    while(j<len(arr)):
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        i+=2
        j+=2
    print(*arr)