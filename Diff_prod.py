def minDiff(arr, arr_size):
    arr.sort()
    min_dif=float('inf')
    for i in range(arr_size-1):
        if(arr[i+1]-arr[i]<min_dif):
            min_dif=arr[i+1]-arr[i]
    return min_dif

def maxDiff(arr, arr_size):
    max_val=max(arr)
    min_val=min(arr)
    return max_val-min_val
    
def prodDiff(arr, arr_size):
    if(arr_size==1):
        return 'NA'
	### Complete this and the above functions!
    return maxDiff(arr,arr_size)*minDiff(arr,arr_size)

for _ in range(int(input())):
    length = int(input())
    arr = [int(x) for x in input().split()]
    print(prodDiff(arr, length))