def count_smallest(arr,query):
    num=[]
    for i in range(len(query)):
        k=query[i]
        right=l_small(arr,k)
        left=r_small(arr,k)
        # print(left,right)
        if(left==right):
            num.append(left)
        elif(k-left<right-k):
            num.append(left)
        else:
            num.append(right)
    return num
#--------------------------------------------------------#
def l_small(arr,x):
    left=0
    right=len(arr)-1
    pos=-1
    while(left<=right):
        mid=(left+right)//2
        if(arr[mid]>=x):
            pos=mid
            right=mid-1
        if(arr[mid]>x):
            right=mid-1
        else:
            left=mid+1
    return arr[pos]
#---------------------------------------------------------#
def r_small(arr,x):
    if(x<arr[0]):
        return arr[0]
    left=0
    right=len(arr)-1
    pos=-1
    while(left<=right):
        mid=(left+right)//2
        if(arr[mid]<=x):
            pos=mid
            left=mid+1
        if(arr[mid]>x):
            right=mid-1
        else:
            left=mid+1
    return arr[pos]
#----------------------------------------------------------#
n,q=map(int,input().split())
arr=list(map(int,input().split()))
query=list(map(int,input().split()))
l=count_smallest(arr,query)
print(*l)
