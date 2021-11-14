dial=int(input())
max=int(input())
n=int(input())
arr=[0]*(dial+1)
flag=0
for j in range(n):
    i=int(input())
    arr[i]=arr[i]+1
    if(arr[i]==max and flag==0):
        flag=1
        print(i)
    
if(flag==0):
    print(0)