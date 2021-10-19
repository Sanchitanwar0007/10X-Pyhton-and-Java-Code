t=int(input())
for i in range(t):
    n=int(input())
    arr=[0]*(n+1)
    for i in range(1,len(arr)):
        arr[i]=((i*i)-i+2)//2
    mul=1
    sum=0
    k=1
    for i in range(1,len(arr)):
        m=arr[i]
        mul=1
        for j in range(k):
            # print(j,end=" ")
            mul=mul*m
            # print("m=",m)
            m+=1
        # print()
        k+=1
        # print("Mul",mul)
        sum+=mul
    print(sum)
