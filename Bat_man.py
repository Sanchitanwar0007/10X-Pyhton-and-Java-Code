def rotate_left(arr,r):  #1 2 3 4 5 ==> 5 1 2 3 4
    right=[]
    r=r%len(arr)
    for i in range(r):
        right.append(arr[i])
    left=[]
    for i in range(r,len(arr)):
        left.append(arr[i])
    j=0
    for i in range(len(left)):
        
        arr[j]=left[i]
        j+=1
    for i in range(len(right)):
        arr[j]=right[i]
        j+=1
    return arr

for _ in range(int(input())):
    n,r=map(int,input().split())
    arr=[int(x) for x in input().split()]
    rotate_left(arr,r)
    print(*arr)