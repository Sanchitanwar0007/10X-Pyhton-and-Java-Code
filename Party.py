for _ in range(int(input())):
    n=int(input())
    arr=[]
    for i in range(n):
        n,m=map(int,input().split())
        arr.append((n*60)+m)
    arr.sort()
    count=1
    ans=1
    for j in range(len(arr)-1):
        if((arr[j+1]-arr[j])==0):
            count+=1
        else:
            ans=max(ans,count)
            count=1
        ans=max(count,ans)
        
    print(ans)
