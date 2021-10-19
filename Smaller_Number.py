def smaller(arr,k):
    left=0
    right=len(arr)-1
    pos=-1
    while(left<=right):
        mid=(left+right)//2
        if(arr[mid]==k):
            pos=mid
            right=mid-1
        elif(arr[mid]>k):
            right=mid-1
        else:
            left=mid+1
    return pos
n=int(input())
listt=[]
arr=[]
for i in range(n):
    num=int(input())
    listt.append(num)
    arr.append(num)
arr.sort()
# print(arr)
for i in range(len(listt)):
    k=listt[i]
    a=smaller(arr,k)
    print(a)


