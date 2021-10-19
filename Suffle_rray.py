def shuffle(arr):
    # Implement this function
    i=0
    n=len(arr)//2
    j=len(arr)//2
    # print(j)
    list=[]
    while(i<n):
       list.append(arr[i])
       list.append(arr[j])
       i+=1
       j+=1
    return list
# Do not edit anything below
if __name__ == "__main__":
    n = int(input())
    nums = []
    for index in range(2 * n):
        nums.append(int(input()))
    for elem in shuffle(nums):
        print(elem)
        