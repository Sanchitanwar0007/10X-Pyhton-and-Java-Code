# # 1 2 3 
# # 4 5 6 
# # 7 8 9

# # 7 4 1
# # 8 5 2 
# # 9 6 3


# arr=[[1,2,3],
#      [4,5,6],
#     [7,8,9]]
# for i in range(len(arr)):  # 0,1
#     for j in range(len(arr)-1): # 2,1,0,2,1,0
#         print(arr[j][i],end=" ") #7,4,1,8,5,
    
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
d={}
for v,i in enumerate(l2):
    if i in d:
        d[i].append(v)
    else:
        d[i]=[v]
re=[]
for i in l1:
    re.append(d[i][0])
    d[i].pop(0)
print(re)