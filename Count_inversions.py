def merge(arr,left,mid,right):
    i=left
    j=mid+1
    k=0
    temp=[0]*(right-left+1)
    count=0
    while(i<=mid and j<=right):
        if(arr[i]<=arr[j]):
            
            temp[k]=arr[i]
            i+=1
            # count+=right-j+1
        else:
            temp[k]=arr[j]
            count+=(mid-i+1)
            
            j+=1
        k+=1
    while(i<=mid):
        temp[k]=arr[i]
        i+=1
        k+=1
        # count+=1
    while(j<=right):
        temp[k]=arr[j]
        j+=1
        k+=1
    for i in range(left,right+1):
        arr[i]=temp[i-left]
    return count

def inversion_count(arr,left,right):
    in_count=0
    if(left<right):
        mid=(left+right)//2
        in_count+=inversion_count(arr,left,mid)
        in_count+=inversion_count(arr,mid+1,right)
        in_count+=merge(arr,left,mid,right)
    return in_count
n=int(input())
arr=list(map(int,input().split()))
print(inversion_count(arr,0,len(arr)-1))
