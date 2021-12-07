# # # # 1 2 3 
# # # # 4 5 6 
# # # # 7 8 9

# # # # 7 4 1
# # # # 8 5 2 
# # # # 9 6 3


# # # arr=[[1,2,3],
# # #      [4,5,6],
# # #     [7,8,9]]
# # # for i in range(len(arr)):  # 0,1
# # #     for j in range(len(arr)-1): # 2,1,0,2,1,0
# # #         print(arr[j][i],end=" ") #7,4,1,8,5,
    
# # l1=list(map(int,input().split()))
# # l2=list(map(int,input().split()))
# # d={}
# # for v,i in enumerate(l2):
# #     if i in d:
# #         d[i].append(v)
# #     else:
# #         d[i]=[v]
# # re=[]
# # for i in l1:
# #     re.append(d[i][0])
# #     d[i].pop(0)
# # print(re)
# # values=[[3,4,5,1],[33,6,1,2]]

# # v = values[0][0]

# # for i in range(len(values)):

# #     for j in range(len(values[i])):

# #         if v > values[i][j]:

# #             v = values[i][j]
# #     if(i==0 and j==3):
# #         print(v)
# def selectSwap(arr, n):
#     maxi=float("-inf")
#     mini=float("inf")
#     max_index=-1
#     min_index=-1
#     for i in range(len(arr)):
#         if(arr[i]>maxi):
#             maxi=arr[i]
#             max_index=i
#         if(arr[i]<mini):
#             mini=arr[i]
#             min_index=i
#     arr[max_index]=mini
#     arr[min_index]=maxi
#     return arr

# if __name__ == '__main__':
#     m=int(input())
#     print(m+"-")
#     for _ in range(m):
#         n = int(input())
#         arr = [int(x) for x in input().split()]
#         print(*selectSwap(arr, n))



# c://docs

arr=[0,0,0,0,1,1,1,1,0,0,0,0,1,1,1]
start=0
end=len(arr)-1
for i in range(len(arr)):
    if(arr[i]==0):
        arr[start]=arr[i]
        start+=1
    else:
        arr[end]=arr[i]
        end-=1
print(arr)
