# your code goes here
def is_good(arr,k,sum,idx,arr_len,target,arr2):
    if(len(arr)<k):
        return
    if(target>=len(arr)):
        if(sum==k and arr_len==k):
            arr2.append(sum)
        return
    if(len(arr2)==0):
        is_good(arr,k,sum+arr[idx],idx+1,arr_len+1,target+1,arr2)
        is_good(arr,k,sum,idx+1,arr_len,target+1,arr2)
n=int(input())
arr=list(map(int,input().split()))
k=int(input())
arr2=[]
is_good(arr,k,0,0,0,0,arr2)
if(len(arr2)==0):
    print(False)
else:
    print(True)