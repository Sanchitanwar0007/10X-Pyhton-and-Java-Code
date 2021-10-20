n=int(input())
arr=list(map(int,input().split()))
dic={}
dic[0]=1
sum=0
ans=0
for i in range(n):
    if(arr[i]%2==0):
        sum+=1
    else:
        sum-=1
    if(sum in dic):
        ans+=dic[sum]
        dic[sum]+=1
    else:
        dic[sum]=1
# print(dic)
print(ans)
