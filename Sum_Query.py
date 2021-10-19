n,q=i=map(int,input().split())
arr=list(map(int,input().split()))
sum=[0]*(len(arr))
sum[0]=arr[0]
for i in range(1,len(arr)):
    sum[i]=sum[i-1]+arr[i] # Prefix Sum Array
# print(sum)
for i in range(q):
    l,r=map(int,input().split())
    if(l==1):
        s=sum[r-1]
        print(s)
    else:
        l=l-1
        r=r-1
        s=sum[r]-sum[l-1]
        print(s)

