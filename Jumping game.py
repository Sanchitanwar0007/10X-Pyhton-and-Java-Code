n=int(input())
arr=[int(x) for x in input.split()]
steps=0
i=0
b=len(arr)
for j in range(len(arr)):
    if(arr[j]+i>=b):
        steps+=1
    