# n=int(input())
# list=[]

# for i in range(n):
# 	list.append(int(input()))
# list.reverse()
# ele=[]
# max=list[0]
# ele.append(list[0])
# for i in range(1,n):
#     if(list[i]>max):
#        ele.append(list[i])
#        max=list[i]
# # print(ele)
# for i in range(len(ele)):
#     print(ele[i])

n=int(input())
list=[]
for i in range(n):
	list.append(int(input()))
list2=[]

for i in range(len(list)-1,-1,-1):
	list2.append(list[i])
# print(list2)
max=list2[0]
print(max)
for i in range(len(list2)):
    if(max<list2[i]):
        max=list2[i]
        print(list2[i])
