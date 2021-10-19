# def pivotIndex(arr):
#     # Implement this function
#     sumFromLeft = []
#     sumFromRight = []
#     sumL = 0
#     sumR = 0
#     for i in arr:
#         sumL+=i
#         sumFromLeft.append(sumL)
#     for i in range(len(arr)-1,-1,-1):
#         sumR+=arr[i]
#         sumFromRight.append(sumR)
#     sumFromRight = sumFromRight[::-1]
#     # print(sumFromLeft)
#     # print(sumFromRight)
#     for i in range(len(arr)):
#         if(sumFromLeft[i]==sumFromRight[i]):
#             return i
#     return -1
# if __name__ == "__main__":
#     num_elems = int(input())
#     nums = []
#     for i in range(num_elems):
#         nums.append(int(input()))
        
#     print(pivotIndex(nums))


def pivotIndex(arr):
    # Implement this function
    
    sum=0
    currsum=0
    
    for i in range(len(arr)): 
        sum+=arr[i]
    for i in range(len(arr)):
        sum-=arr[i]
        if(currsum==sum):
            return i
        currsum+=arr[i]

    return -1
    # Do not edit anything below
if __name__ == "__main__":
    num_elems = int(input())
    nums = []
    for i in range(num_elems):
        nums.append(int(input()))
    print(pivotIndex(nums))