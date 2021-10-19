n=int(input())
arr=list(map(int,input().split()))
dict={}
for i in range(len(arr)):
	if arr[i] in dict:
		dict[arr[i]]+=1
	else:
		dict[arr[i]]=1
# print(dict)
count=0
for i in dict:
    # print(dict[i])
    if(dict[i]>1):
        count+=dict[i]//2
print(count)
