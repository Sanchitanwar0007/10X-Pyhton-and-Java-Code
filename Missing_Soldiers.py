# n=int(input())
# list=[]
# temp_pos=[0]*n
# width_arr=[0]*n
# for i in range(n):
#     x,y,width=map(int,input().split())
#     temp_pos[i]=x
#     width_arr[i]=width
# print(temp_pos,width_arr)
# for i in range(n):
#     if(i==0):
#         list.append(temp_pos[i])
#         list.append(temp_pos[i]+width_arr[i]+1)
#     else:
#         if(temp_pos[i]<list[-1]):
#             list.append(temp_pos[i]+width_arr[i]+1)
#         else:
#             last=list[-1]
#             list.append(temp_pos[i])
#             list.append(temp_pos[i]+width_arr[i]+1-(temp_pos[i]-last))
# print(list)
# list.sort()
# print(list[-1]-list[0])

n=int(input())
arr=[]
for i in range(n):
	x,y,w=map(int,input().split())
	start=x
	end=x+w
	arr.append((start,end))
arr.sort(key=lambda x:x[0])
res=0
res+=arr[0][1]-arr[0][0]+1
m=arr[0][1]
for i in range(1,n):
	if(arr[i][1]<=m):
		continue
	if(arr[i][0]<=m):
		res+=arr[i][1]-m
	else:
		res+=arr[i][1]-arr[i][0]+1
	m=arr[i][1]
print(res)
