# def cutRope(arr):
#     list=[]
#     while(True):
#         f1=True
#         if(len(arr)>0):
#             mini=min(arr)
#         i=0
#         while(i<len(arr)):
#             f1=False
#             arr[i]=arr[i]-mini
#             if(arr[i]==0):
#                 arr.remove(0)
#                 i-=1
#             i+=1
#         if(len(arr)>0):
#             list.append(len(arr))
#         if(f1==True):
#             break
#     return list
# # Do not change anything below this line
# if __name__ == '__main__':
#     input_numbers = []
#     for _ in range(int(input())):
#         input_numbers.append(int(input()))

#     for i in cutRope(input_numbers):
#         print(i)



def cutRope(arr):
    arr.sort()
    mini=arr[0]
    ans=[]
    for i in range(len(arr)):
        if(arr[i]-mini>0):
            ans.append(len(arr)-i)
        mini=arr[i]
    return ans
# Do not change anything below this line
if __name__ == '__main__':
    input_numbers = []
    for _ in range(int(input())):
        input_numbers.append(int(input()))

    for i in cutRope(input_numbers):
        print(i)