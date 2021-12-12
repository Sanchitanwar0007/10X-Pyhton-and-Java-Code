def merge(arr,left,mid,right):
    # print(arr,left,mid,right)
    temp=[0]*(right-left+1)
    i=left
    j=mid+1
    k=0
    while(i<=mid and j<=right):
        if(arr[i]<arr[j]):
            temp[k]=arr[i]
            i+=1
        else:
            temp[k]=arr[j]
            j+=1
        k+=1
    if(i<=mid):
        while(i<=mid):
            temp[k]=arr[i]
            i+=1
            k+=1
    if(j<=right):
        while(j<=right):
            temp[k]=arr[j]
            j+=1
            k+=1
    # print(temp)
    for i in range(left,right+1):
        arr[i]=temp[i-left]
def merge_sort(arr,left,right):
    if(left<right):
        mid=left+(right-left)//2
        print(mid)
        merge_sort(arr,left,mid)
        merge_sort(arr,mid+1,right)
        merge(arr,left,mid,right)
    # print(s_arr)
arr=list(map(int,input().split()))
merge_sort(arr,0,len(arr)-1)
print(arr)