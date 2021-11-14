def replaceElements(arr):
    # Implement this function
    ans=[0]*len(arr)
    ans[len(arr)-1]=-1
    maxi=arr[len(arr)-1]
    for i in range(len(arr)-1,-1,-1):
        if(i>0):
            ans[i-1]=max(maxi,arr[i])
        maxi=max(arr[i],maxi)
    return ans
# Do not edit anything below
if __name__=="__main__":
    num_elems = int(input())
    arr = []
    for index in range(num_elems):
        arr.append(int(input()))
    replaceElements(arr)
    for elem in replaceElements(arr):
        print(elem)