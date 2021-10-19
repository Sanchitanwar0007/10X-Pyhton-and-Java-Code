n=int(input())
for p in range(n):
    num=int(input())
    favor=[]
    anger=[]
    diff=[]
    for j in range(num):
        f,a=map(int,input().split())
        favor.append(f)
        anger.append(a)
        diff.append(f+a)
    # print(favor)
    # print(anger)
    # print(diff)

    max1=float('-inf')
    max2=float('-inf')
    # idx1=len(anger)
    # idx2=len(anger)
    for k in range(num):
        if(diff[k]>max1):
            max1=diff[k]
            idx1=k
    for l in range(num):
        if(diff[l]>=max2 and idx1!=l):
            max2=diff[l]
            idx2=l
    sum=0
    # print("index",idx1,idx2)
    # print("two max",max1,max2)
    # print("actual_max",favor[idx1],favor[idx2])
    for i in range(len(anger)):
        if(i==idx1 or i==idx2):
            continue
        else:
            # print(i)
            sum+=anger[i]
    total=favor[idx1]+favor[idx2]
    print(total-sum)
        









# 10
# 68 2
# 38 11
# 22 9
# 41 15
# 85 12
# 68 18
# 74 3
# 51 3
# 82 8
# 5 16
# two max 85 82
# # 90


    # max1=float('-inf')
    # max2=float('-inf')
    # # idx1=len(anger)
    # # idx2=len(anger)
    # for k in range(num):
    #     if(favor[k]>max1):
    #         max1=favor[k]
    #         idx1=k
    # for l in range(num):
    #     if(favor[l]>=max2 and idx1!=l):
    #         max2=favor[l]
    #         idx2=l
    # sum=0
    # # print("index",idx1,idx2)
    # print("two max",max1,max2)
    # for i in range(len(anger)):
    #     if(i==idx1 or i==idx2):
    #         continue
    #     else:
    #         # print(i)
    #         sum+=anger[i]
    # total=max1+max2
    # print(total-sum)
        

# 1
# 4
# 2 3
# 10 2
# 11 5
# 4 1