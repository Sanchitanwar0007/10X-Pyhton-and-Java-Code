def max_of_arr(arr,i,maxi):
    if(i==len(arr)):
        return maxi
    n=max_of_arr(arr,i+1,maxi)
    maxi=max(n,arr[i])
    return maxi
arr=list(map(int,input().split()))
print(max_of_arr(arr,0,float('-inf')))