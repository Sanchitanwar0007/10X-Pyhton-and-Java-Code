def get_paths(arr,i,j,maxx,arr2):
    if(i==len(arr) or j==len(arr[0]) or arr[i][j]==-1):
        return
    if(i==len(arr)-1 and j==len(arr[0])-1):
        maxx+=arr[i][j]
        arr2.append(maxx)
        return
    get_paths(arr,i,j+1,maxx+arr[i][j],arr2)
    get_paths(arr,i+1,j,maxx+arr[i][j],arr2)
n,m=map(int,input().split())
arr=[]
for i in range(n):
    li=list(map(int,input().split()))
    arr.append(li)
arr2=[]
get_paths(arr,0,0,0,arr2)
if(len(arr2)==0):
    print("No way")
else:
    print(max(arr2))