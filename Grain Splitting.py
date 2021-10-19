n=int(input())
for i in range(n):
    arr=list(map(int,input().split()))
    summ=sum(arr)//2
    idx=-1
    s=0
    arr.sort()
    for i in range(len(arr)):
        if(summ==s):
            idx=i
            break
        else:
            s+=arr[i]
    print(n)
    for i in range(idx,len(arr)):
        print(arr[i],end=" ")
    