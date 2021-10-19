# https://6793fdf6.widgets.sphere-engine.com/lp?hash=hGambFsYTS

# n=int(input())
# arr=[-1]*n
# for i in range(n):
#     pos,speed=map(int,input().split())
#     arr[pos]=speed
# count=0
# # for i in range(n):
# #     for j in range(i+1,n):
# #         if(arr[j]<arr[i]):
# #             count+=1
# dict={}
# temp=arr
# temp.sort()
# for i in range(n):
#     if(temp[i] not in dict):
#         dict[temp[i]]=i
# for i in arr:
#     count+=dict[i]
# print(count//2)


n=int(input())
arr=[0]*n
for i in range(n):
	pos,vel=map(int,input().split())
	arr[pos]=vel
vel_arr=[0]*11  #[0 1 2 3 4 5 6 7 8 9 10]
ans=0

for i in range(len(arr)):
	temp=arr[i]
	for j in range(temp+1,11):
		ans+=vel_arr[j]
	vel_arr[temp]+=1
print(ans)