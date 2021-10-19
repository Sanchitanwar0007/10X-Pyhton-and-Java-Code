# def findLuckyNumber(nums):
#     # implement this function
#     count=1
#     flag=0
#     if(len(nums)==1 and nums[0]==1):
#         flag=1
#     else:
#         for i in range(len(nums)):
            
#             for j in range(len(nums)):
#                 if(nums[i]==nums[j] and i!=j):
#                     count+=1
#             if(count==nums[i]):
#                 flag=1
#                 break
#             else:
#                 count=1
#     if(flag==1):
# 	    return 1
#     else:
# 	    return -1
# # DO NOT change anything below this line
# if __name__ == "__main__":
#     num_elems = int(input())
#     input_arr = []
#     for index in range(num_elems):
#         input_arr.append(int(input()))
    
#     print(findLuckyNumber(input_arr))


# def findLuckyNumber(nums):
#     maxi=max(nums)
#     flag=0
#     number=0
#     arr=[0 for i in range(maxi+1)]
#     for i in range(len(nums)):
#      if(nums[i]!=0):
#         arr[nums[i]-1]+=1
#     for i in range(len(arr)):
#         if((i+1)==arr[i]):
#             number=i+1
#             flag=1
#             break
#     if(flag==1):
#         return number
#     else:
#         return -1



# # DO NOT change anything below this line
# if __name__ == "__main__":
#     num_elems = int(input())
#     input_arr = []
#     for index in range(num_elems):
#         input_arr.append(int(input()))
    
#     print(findLuckyNumber(input_arr))

import array
def findLuckyNumber(nums):
    # implement 9this function
    max=nums[len(nums)-1]# List rage out of index
    arr=[0 for i in range(max+1)]
    flag=0
    for i in range(len(nums)):
        arr[nums[i]]+=1
    
    for i in range(1,len(arr)):

        if(i==arr[i]):
            number=i
            flag=1
            break
    if(flag==1):
        return number
    else:
        return -1
# DO NOT change anything below this line
if __name__ == "__main__":
    num_elems = int(input())
    input_arr = []
    for index in range(num_elems):
        input_arr.append(int(input()))
    
    print(findLuckyNumber(input_arr))