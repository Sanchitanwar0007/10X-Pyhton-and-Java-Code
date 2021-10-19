# def rotate(list,m):
#     for i in range(m):
#         temp=list[0]
#         list.remove(list[0])
#         list.append(temp)
#     for i in list:
#     	print(i)
# list=list(map(int,input().split()))
# m=int(input())
# rotate(list,m)


# O(n) approach for this problem is
# [2,1,3,4,5,10] => [1,3,4,5,10,2] =>[3,4,5,10,2,1]=> [4,5,10,2,1,3] when m=0,1,2and 3 respectively
# but when m>1 then using formulae directly convert into resulted matrix :=> if m=3 thne [2,1,3,4,5,10] => [4,5,10,2,1,3]

arr=[int(x) for x in input().split()]
m=int(input())
list=[0]*len(arr)
for i in range(len(arr)):
    final_pos=abs(i-m+len(arr))%len(arr)
    list[final_pos]=arr[i]
print(list)
