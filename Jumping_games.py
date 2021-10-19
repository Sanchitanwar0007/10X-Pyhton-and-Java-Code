def findpath(arr,i,jumps,all_jumps):
	if(i>=len(arr)):
		all_jumps.append(jumps)
		return
	findpath(arr,i+1,jumps+1,all_jumps)
	findpath(arr,i+arr[i],jumps+1,all_jumps)
n=int(input())
arr=[int(x) for x in input().split()]
all_jumps=[]
findpath(arr,0,0,all_jumps)
print(all_jumps)
print(min(all_jumps))