# This is O(n) approach and O(n) time complexity
n=int(input())
zero=0
one=0
two=0
for i in range(n):
    n=int(input())
    if(n==0):
        zero+=1
    elif(n==1):
        one+=1
    else:
        two+=1
# print(zero,one,two)
for i in range(zero):
    print(0)
for i in range(one):
    print(1)
for i in range(two):
	print(2)
# If List Is necessaory then Approch for list is 
# your code goes here
# n=int(input())
# list=[]
# for i in range(n):
# 	list.append(int(input()))
# zero=0
# one=0
# two=0
# for i in range(n):
# 	if(list[i]==0):
# 		zero+=1
# 	elif(list[i]==1):
# 		one+=1
# 	else:
# 		two+=1
# # print(zero,one,two)
# ele=0
# for i in range(zero):
#     ele+=1
#     list[i]=0
    
# for i in range(ele,ele+one):
#     list[i]=1
#     ele+=1
# for i in range(ele,ele+two):
# 	list[i]=2
# for i in range(len(list)):
#     print(list[i])