n=int(input())
arr=list(map(int,input().split()))
sett=set()
count=0
for i in range(n):
    if(arr[i] in sett):
        count+=1
    else:
        sett.add(arr[i])
l=len(sett)
if(l>n//2):
    print(n//2)  
else:
    print(len(sett))