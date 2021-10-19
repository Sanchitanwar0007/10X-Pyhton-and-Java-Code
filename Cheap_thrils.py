# for i in range(int(input())):
#     N=int(input())
#     arr=list(map(int,input().split()))
#     mp={}
#     for i in range(len(arr)):
#         mp[arr[i]]=i+1
#     print(mp)
#     arr.sort()
#     count=0
#     for i in range(len(arr)):
#         if mp[arr[i]]%2!=(i+1)%2:
#             count+=1
#     print(count//2)



n=int(input())
for i in range(n):
    num=int(input())
    arr=list(map(int,input().split()))
    res=[]
    for i in range(len(arr)):
        res.append(arr[i])
    # print(res,arr)
    
    # print(res,arr)
    arr_even_set=set()
    res_even_set=set()
    res.sort()
    for i in range(num):
        if(i%2==0):
            arr_even_set.add(arr[i])
            res_even_set.add(res[i])
    # print(arr_even_set,res_even_set)

    result=arr_even_set-res_even_set
    # print(result)
    print(len(result))
# 2
# 3
# 3 2 1
# 5
# 2 8 5 9 7

