t=int(input())
for i in range(t):
    num=int(input())
    arr=list(map(int,input().split()))
    average=0

    for i in arr:
        average+=i
    average=average/num
    xmen=0
    for i in range(num):
        if(arr[i]>average):
            xmen+=1
    print(xmen)