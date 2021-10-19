from collections import Counter
def intersect_three(arr1,arr2,arr3):
    dict=Counter(arr1)
    dict2=Counter(arr2)
    dict3=Counter(arr3)
    for i in dict:
        if i in dict2:
            dict[i]=min(dict[i],dict2[i])
        else:
            dict[i]=-1
    for i in dict:
        if i in dict3:
            dict[i]=min(dict[i],dict3[i])
        else:
            dict[i]=-1
    flag=0
    for i,j in sorted(dict.items()):
        if(j!=-1):
            flag=1
            print(i)
    if(flag==0):
        print(-1)

    
n=int(input())
arr1=[]
for i in range(n):
    arr1.append(int(input()))
n2=int(input())
arr2=[]
for i in range(n2):
    arr2.append(int(input()))
n3=int(input())
arr3=[]
for i in range(n3):
    arr3.append(int(input()))
intersect_three(arr1,arr2,arr3)
# for i in res:
#     print(i)