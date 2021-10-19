n=int(input())
for i in range(n):
    arr=list(map(int,input().split()))
    arr.sort()

    b=1
    c=2
    max=0
    a=0
    while(c<len(arr)):
        if(arr[a]+arr[b]>arr[c]):
            if(arr[a]+arr[b]+arr[c]>max):
                max=arr[a]+arr[b]+arr[c]
        b+=1
        c+=1
        a+=1
    print(max)